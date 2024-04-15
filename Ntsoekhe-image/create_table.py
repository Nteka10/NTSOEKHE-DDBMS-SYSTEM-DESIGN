import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('''CREATE TABLE patients (
                fname TEXT,
                lname TEXT,
                dob TEXT,
                nationalId TEXT,
                gender TEXT,
                phone TEXT,
                email TEXT,
                address TEXT,
                illness TEXT 
                )''')
print("Created table successfully!")

conn.close()
