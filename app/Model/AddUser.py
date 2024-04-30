import sqlite3


class UserModel:
    DATABASE = 'Connection'

    @staticmethod
    def add_user(name, surname, email, phone, password):
        """Add a new user to the database."""
        conn = sqlite3.connect(UserModel.DATABASE)
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO main.User (Name, Surname, Email, PhoneNumber, Password,is_admin)
            VALUES (?, ?, ?, ?, ?,False)
        ''', (name, surname, email, phone, password))

        conn.commit()
        conn.close()
