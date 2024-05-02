import sqlite3

from Model.AddUser import UserModel


class AddFlightModel:
    DATABASE = 'Connection'

    @staticmethod
    def add_flight(company, departure, destination, year,month,day,hour,minute):
        """Add a new user to the database."""
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO main.Flight (CompanyName, Departure, Destination, Year, Month, Day, Hour, Minute)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (company, departure, destination, year, month, day, hour, minute))

        conn.commit()
        conn.close()