import sqlite3
from Model.AddUser import UserModel
class DeleteFlightModel:
    DATABASE= 'Connection'

    @staticmethod
    def delete_flight(flight_id):
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor= conn.cursor()
        cursor.execute('''UPDATE main.Flight SET is_removed=1 WHERE flight_id=?''', (flight_id,))
        conn.commit()
        conn.close()