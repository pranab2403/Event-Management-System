import sqlite3

# Create database file
conn = sqlite3.connect("database.db")

cursor = conn.cursor()

# Users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT
)
""")

# Events table
cursor.execute("""
CREATE TABLE IF NOT EXISTS events(
    id INTEGER PRIMARY KEY,
    title TEXT,
    date TEXT,
    location TEXT
)
""")

# Registrations table
cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations(
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    event_id INTEGER
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")