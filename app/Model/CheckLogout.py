import sqlite3

from Model.AddUser import UserModel

class CheckUserModel:
    DATABASE = 'Connection'

    @staticmethod
    def check_admin(email):
        print(email)
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE Email = ?", (email,))
        row = cursor.fetchone()
        if row:
            if row[5] == 1:
                return True
            else:
                return False

    @staticmethod
    def check_user(email):
        print(email)
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE Email = ?", (email,))
        row = cursor.fetchone()
        if row:
            if row[5] == 0:
                return True
            else:
                return False
