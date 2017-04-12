from peewee import *
from playhouse.postgres_ext import *
import argparse

parser = argparse.ArgumentParser(description='Calculate EV for PartyPoker Hero')
parser.add_argument('--dbname')
parser.add_argument('--dbpass')
parser.add_argument('--dbtype', choices=['H', 'P'])
parser.add_argument('--heronames', nargs='*')
args = parser.parse_args()

database = PostgresqlDatabase(
    args.dbname or input("Enter DB name: "),
    **{
        'password': args.dbpass or input("Enter DB password: "),
        'user': 'postgres'
    }
)

def connect_to_data():
    global database
    try:
        database.connect()
    except OperationalError:
        print("\nIncorrect DB details, try again")
        database = PostgresqlDatabase(input("Enter DB name: "),
                                      **{'password': input("Enter DB password: "), 'user': 'postgres'})
        connect_to_data()

connect_to_data()

def close_data_connection():
    database.close()