import sqlite3

from Model.AddUser import UserModel


class FlightModel:
    DATABASE = 'Connection'

    @staticmethod
    def check_flight(email):
        print(email)
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Flight WHERE author = ?", (email,))
        row = cursor.fetchall()
        data = []
        print(row)
        for x in row:
            data.append(x)

        conn.commit()
        conn.close()
        return data

    def check_userflight(departure, destination, yearL, monthL, dayL):
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Flight WHERE is_removed = ? AND departure = ? AND destination = ?",(False,departure, destination))
        row = cursor.fetchall()
        data = []
        for x in row:
            if int(x[3]) == int(yearL) and int(x[4]) == int(monthL) and int(x[5]) == int(dayL):
                data.append(x)
        conn.commit()
        conn.close()
        return data