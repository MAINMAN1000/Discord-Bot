import sqlite3

def create_database():
    conn = sqlite3.connect('kushy.db')  # This creates a new database file
    cursor = conn.cursor()

    # Create a table for strains
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS strains (
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        type TEXT,
        thc_level REAL,
        cbd_level REAL,
        flavor TEXT,
        effects TEXT,
        medical_uses TEXT
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Database and table created successfully.")