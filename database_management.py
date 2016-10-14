from peewee import *
from playhouse.postgres_ext import *

database = PostgresqlDatabase(input("Enter DB name: "), **{'password': input("Enter DB password: "), 'user': 'postgres'})

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