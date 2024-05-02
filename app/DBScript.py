# Re-establishing the database connection to modify the existing table and create a new one
# Re-establishing the database connection to modify the existing table and create a new one
import sqlite3

conn = sqlite3.connect('Connection')
cursor = conn.cursor()

# Adjust the 'Countrys' table to ensure 'CountryName' is suitable for a foreign key reference
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Countrys_New (
        CountryName TEXT PRIMARY KEY
    )
''')

# Migrate data from old Countrys table to new one
cursor.execute('INSERT INTO Countrys_New (CountryName) SELECT CountryName FROM Countrys')
cursor.execute('DROP TABLE Countrys')
cursor.execute('ALTER TABLE Countrys_New RENAME TO Countrys')

# SQL query to create the 'Flights' table with appropriate foreign key constraints
create_flights_table_sql = '''
CREATE TABLE IF NOT EXISTS Flights (
    FlightID INTEGER PRIMARY KEY AUTOINCREMENT,
    DepartureCountry TEXT,
    DestinationCountry TEXT,
    TotalTime TEXT,
    RemainingTime TEXT,
    StatusOfFlight TEXT,
    Price REAL,
    FOREIGN KEY (DepartureCountry) REFERENCES Countrys(CountryName),
    FOREIGN KEY (DestinationCountry) REFERENCES Countrys(CountryName)
)
'''

# Execute the SQL command to create the Flights table
cursor.execute(create_flights_table_sql)

# Commit changes and close the connection after done
conn.commit()
conn.close()

# Uncomment the following line in the final version to confirm table creation.
# print("Flights table created successfully with references to the updated Countrys table.")

