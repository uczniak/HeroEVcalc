from pt4models import (TourneyResults,TourneySummary,TourneyHandPlayerStatistics,
                       Player,TourneyTableType)
from hm2models import (Players,Tourneydata,Handhistories)
import matplotlib.pyplot as plt
import requests

class Hero:
    def __init__(self, name):
        self.ev_from_chips = 0
        self.chip_ev = 0
        self.bounty_ev = 0
        self.tourney_count = 0
        self.hand_count = 0
        self.bounty_count = 0
        self.rake_paid = 0
        self.buyins_paid = 0
        self.ev_line = [0]
        self.real_line = [0]
        self.rb_percentage = 0
        self.name = name

    def display_graph(self):
        plt.plot(self.ev_line, ls='solid', color='orange', label='$EV')
        plt.plot(self.real_line, ls='solid', color='green', label='real')
        plt.xlabel('Tournaments')
        plt.ylabel('$')
        plt.legend(loc = 'upper left')
        plt.show()

    def display_summary(self):
        if self.tourney_count == 0:
            print("No tournaments found for player {} in the specified period".format(self.name))
            input("Press enter to exit: ")
        else:
            print("""
Player: {}
Number of tournaments played: {:,}

Total buyins: ${:,.0f}
Avg BI: ${:.2f}

Number of hands played: {:,}
Number of hands per tournament: {:.2f}

cEV per tournament: {:.0f}
cEV per hand: {:.2f}

Number of bounties: {}
Total bounty percentage: {:.2%}

Total $EV (excluding RB): ${:,.2f}
Total EV ROI: {:.2%}
$EV per tournament: ${:.2f}

Rake paid: ${:,.2f}
""".format(self.name,
           self.tourney_count,
           self.buyins_paid,
           self.buyins_paid / self.tourney_count,
           self.hand_count,
           self.hand_count / self.tourney_count,
           self.chip_ev / self.tourney_count,
           self.chip_ev / self.hand_count,
           self.bounty_count,
           self.bounty_count / self.tourney_count,
           self.ev_from_chips + self.bounty_ev,
           (self.ev_from_chips + self.bounty_ev) / self.buyins_paid,
           (self.ev_from_chips + self.bounty_ev) / self.tourney_count,
           self.rake_paid))

            while not self.rb_percentage:
                try:
                    temp = input("Please enter a non-zero rakeback percentage (e.g. 30), empty to exit: ")
                    if temp == "":
                        break
                    else:
                        self.rb_percentage = float(temp) / 100
                except ValueError:
                    print("Something went wrong. Try again.")
                    self.rb_percentage = 0

            if self.rb_percentage:
                print("""
Total $EV+RB: ${:,.2f}
Total EV+RB ROI: {:.2%}
$EV+RB per tournament: ${:.2f}
""".format(self.ev_from_chips + self.bounty_ev + self.rb_percentage * self.rake_paid,
           (self.ev_from_chips + self.bounty_ev + self.rb_percentage * self.rake_paid) / self.buyins_paid,
           (self.ev_from_chips + self.bounty_ev + self.rb_percentage * self.rake_paid) / self.tourney_count))
                input("Press enter to exit: ")

class PT4Hero(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.id = (Player
                   .select(Player.id_player)
                   .where((Player.player_name_search == self.name.lower())
                          & (Player.id_site == 200))
                   .get()
                   .id_player)

    def add_half_bounty(self, tourney):
        self.bounty_count += 0.5
        self.bounty_ev += float(tourney.amt_buyin) * 0.5

    def read_data(self, start_date, end_date):
        tourneys = (TourneyResults.select(TourneyResults, TourneySummary, TourneyTableType)
                    .join(TourneySummary, on=(TourneyResults.id_tourney == TourneySummary.id_tourney))
                    .join(TourneyTableType, on=(TourneySummary.id_table_type == TourneyTableType.id_table_type))
                    .where((TourneyResults.id_player == self.id)
                           & (TourneySummary.date_start > start_date)
                           & (TourneySummary.date_start < end_date)
                           & (TourneyTableType.val_flags.contains('L')))
                    .order_by(TourneySummary.date_start)
                    .naive())

        for tourney in tourneys:
            tourney_chip_ev = 0
            self.tourney_count += 1
            tourney_hands = (TourneyHandPlayerStatistics
                             .select(TourneyHandPlayerStatistics.amt_expected_won)
                             .where((TourneyHandPlayerStatistics.id_player == self.id)
                                    & (TourneyHandPlayerStatistics.id_tourney == tourney.id_tourney)))
            for hand in tourney_hands:
                tourney_chip_ev += float(hand.amt_expected_won)
                self.hand_count += 1

            self.chip_ev += tourney_chip_ev
            self.ev_from_chips += tourney_chip_ev * 0.75 / 500 * float(tourney.amt_buyin) - float(
                tourney.amt_fee) * 0.75

            if float(tourney.amt_won) > 0.88 * float(tourney.amt_prize_pool):
                bounty_collected = True
            elif 0.87 * float(tourney.amt_prize_pool) < float(tourney.amt_won) < 0.88 * float(tourney.amt_prize_pool):
                bounty_collected = False
                self.add_half_bounty(tourney)
            elif 0.84 * float(tourney.amt_prize_pool) < float(tourney.amt_won) < 0.87 * float(tourney.amt_prize_pool):
                bounty_collected = True
            elif 0.76 * float(tourney.amt_prize_pool) < float(tourney.amt_won) < 0.84 * float(tourney.amt_prize_pool):
                bounty_collected = False
                self.add_half_bounty(tourney)
            elif 0.61 * float(tourney.amt_prize_pool) < float(tourney.amt_won) < 0.74 * float(tourney.amt_prize_pool):
                bounty_collected = False
                self.add_half_bounty(tourney)
            elif (tourney.val_finish != 1) & (float(tourney.amt_won) > 0.24 * float(tourney.amt_prize_pool)):
                bounty_collected = True
            elif (tourney.val_finish != 1) & (0.24 * float(tourney.amt_prize_pool)
                                                  > float(tourney.amt_won) > 0.08 * float(tourney.amt_prize_pool)):
                bounty_collected = False
                self.add_half_bounty(tourney)
            else:
                bounty_collected = False

            if bounty_collected:
                self.bounty_count += 1
                self.bounty_ev += float(tourney.amt_buyin) * 0.75 - float(tourney.amt_fee) * 0.25
            else:
                self.bounty_ev -= float(tourney.amt_buyin) * 0.25 + float(tourney.amt_fee) * 0.25

            self.rake_paid += float(tourney.amt_fee)
            self.buyins_paid += float(tourney.amt_buyin + tourney.amt_fee)
            self.ev_line.append(self.bounty_ev+self.ev_from_chips)
            self.real_line.append(self.real_line[-1] + float(tourney.amt_won)
                                  -float(tourney.amt_buyin) - float(tourney.amt_fee))

class HM2Hero(Hero):
    def __init__(self, name):
        super().__init__(name)
        temp = (Players
                .select(Players.player, Players.playername)
                .where((Players.playername ** self.name)
                        & (Players.pokersite == 0))
                .get())
        self.id = temp.player
        self.name = temp.playername

    def read_data(self, start_date, end_date):
        bounty_string = "Bounty Won! {}".format(self.name)
        tourneys = (Tourneydata.select()
                    .where((Tourneydata.player == self.id)
                           & (Tourneydata.firsthandtimestamp > start_date)
                           & (Tourneydata.firsthandtimestamp < end_date)
                           & (Tourneydata.tablesize == 4))
                    .order_by(Tourneydata.firsthandtimestamp)
                    )

        for tourney in tourneys:
            tourney_chip_ev = 0
            bounty_collected = False
            bounty_cleared = False
            self.tourney_count += 1

            tourney_hands = (Handhistories
                             .select()
                             .where(Handhistories.tourneynumber == tourney.tourneynumber))
            for hand in tourney_hands:
                # tourney_chip_ev +=  need to get that from HM2 API
                if bounty_string in hand.handhistory:
                    bounty_collected = True
                elif "Bounty Won!" in hand.handhistory:
                    bounty_cleared = True
                self.hand_count += 1

            if not bounty_collected and not bounty_cleared and tourney.finishposition == 1:
                bounty_collected = True

            hmql = 'select statallinevadjustedchips from stats where tourneynumber="{}"'.format(tourney.tourneynumber)
            api_response = requests.get('http://localhost:8001/Query', params = {'q': hmql})
            tourney_chip_ev = int(api_response.json()["Results"][0]["Chips(EVAdjusted)"]
                                  .replace(',','')
                                  .replace(' ',''))
            self.chip_ev += tourney_chip_ev
            self.ev_from_chips += tourney_chip_ev * 0.75 / 500 * float(tourney.buyinincents) / 100 - float(tourney
                                                                                    .rakeincents) / 100 * 0.75

            if bounty_collected:
                self.bounty_count += 1
                self.bounty_ev += float(tourney.buyinincents) / 100 * 0.75 - float(tourney.rakeincents) / 100 * 0.25
            else:
                self.bounty_ev -= float(tourney.buyinincents) / 100 * 0.25 + float(tourney.rakeincents) / 100 * 0.25

            self.rake_paid += float(tourney.rakeincents) / 100
            self.buyins_paid += float(tourney.buyinincents + tourney.rakeincents)/100
            self.ev_line.append(self.bounty_ev+self.ev_from_chips)
            self.real_line.append(self.real_line[-1] + float(tourney.winningsincents)/100
                                  -float(tourney.buyinincents)/100 - float(tourney.rakeincents)/100)