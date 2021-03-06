from database_management import close_data_connection, args
from hero import PT4Hero, HM2Hero
from datetime import datetime, timedelta
import tkinter # needed for pyinstaller
import tkinter.filedialog # needed for pyinstaller

hero_names = ' '.join(args.heronames or [])
hero_list = []

db_type = args.dbtype or None
while not db_type:
    db_type = input("Please enter 'H' for HM2, 'P' for PT4: ")
    if db_type.lower() not in ['h', 'p']:
        db_type = None

while True:
    for name in hero_names.split():
        try:
            if db_type.lower() == 'h':
                hero_list.append(HM2Hero(name))
            elif db_type.lower() == 'p':
                hero_list.append(PT4Hero(name))
        except Exception:
            print("Something went wrong. Can't find a player named {}.".format(name))
    if hero_list:
        break
    else:
        hero_names = input("Please enter player name(s): ")

start_date = None

while not start_date:
    try:
        temp = input("Please enter start date (dd/mm/yy), empty for no start: ")
        if temp == "":
            start_date = datetime.min
        else:
            start_date = datetime.strptime(temp, "%d/%m/%y")
    except:
        print("Something went wrong. Wrong date format.")
        start_date = None

end_date = None

while not end_date:
    try:
        temp = input("Please enter end date (dd/mm/yy), empty for no end: ")
        if temp == "":
            end_date = datetime.max
        else:
            end_date = datetime.strptime(temp, "%d/%m/%y")+timedelta(days=1)
    except:
        print("Something went wrong. Wrong date format.")
        end_date = None

min_stake = None

while min_stake is None:
    try:
        temp = input("Please enter minimum stake to be included, empty for no minimum: ")
        if temp == "":
            min_stake = 0
        else:
            min_stake = int(temp)
    except:
        print("Something went wrong. Wrong stake format.")
        min_stake = None

max_stake = None

while max_stake is None:
    try:
        temp = input("Please enter maximum stake to be included, empty for no maximum: ")
        if temp == "":
            max_stake = float('Inf')
        else:
            max_stake = float(temp)
    except:
        print("Something went wrong. Wrong stake format.")
        max_stake = None

for current_hero in hero_list:
    current_hero.read_data(start_date,end_date,min_stake,max_stake)

close_data_connection()

for current_hero in hero_list:
    current_hero.display_summary()
    current_hero.display_graph()



