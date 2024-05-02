import sqlite3

from Model.AddUser import UserModel


class FlightModel:
    DATABASE = 'Connection'

    @staticmethod
    def check_flight(departure,destination,yearL,monthL,dayL,yearU,monthU,dayU):
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Flight WHERE departure = ? AND destination = ?", (departure,destination))
        row = cursor.fetchall()
        data=[]
        lowerBound = t2n(yearL, monthL, dayL)
        upperBound= t2n(yearU,monthU,dayU)
        for x in row:
            date=t2n(x[3],x[4],x[5])
            if date>=lowerBound and date<=upperBound:
                data.append(x)
        conn.commit()
        conn.close()
        return data

def t2n(year, month, day):
    return int(year) * 10000 + int(month) * 100 + int(day)
