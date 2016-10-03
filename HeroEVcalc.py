from pt4models import close_data_connection
from hero import Hero
from datetime import datetime, timedelta
import tkinter # needed for pyinstaller
import tkinter.filedialog # needed for pyinstaller

hero_names = None
hero_list = []

while not hero_list:
    hero_names = input("Please enter player name(s): ")
    for name in hero_names.split():
        try:
            hero_list.append(Hero(name))
        except:
            print("Something went wrong. Can't find a player named {}".format(name))

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

for current_hero in hero_list:
    current_hero.read_data(start_date,end_date)

close_data_connection()

for current_hero in hero_list:
    current_hero.display_summary()
    current_hero.display_graph()



