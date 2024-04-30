import sqlite3


class UserModel:
    DATABASE = 'Connection'

    @staticmethod
    def check_user(email, password):
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM User WHERE email = ?", (email,))
        row = cursor.fetchone()
        if row is not None: # checks if user exist
            conn.commit()
            conn.close()
            if row[4] == password: # checking the password
                if row[5] == True: # checking the is_admin
                    return email, True # user is admin
                else:
                    return email, False #user is not admin
            else:
                return "pw" # password is wrong
        else:
            return "ue" # user does not exist
