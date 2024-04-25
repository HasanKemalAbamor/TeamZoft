import sqlite3


class UserModel:
    DATABASE = 'Connection'

    @staticmethod
    def check_user(email, password):
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row is not None:
            conn.commit()
            conn.close()
            if row[4] == password:
                return email
            else:
                return "pw"
        else:
            return "ue"
