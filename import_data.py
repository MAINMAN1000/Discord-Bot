import csv
import sqlite3

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = sqlite3.connect('kushy.db')  
    return conn

def import_data_from_csv(csv_file):
    """Import strain data from a CSV file into the database."""
    conn = create_connection()
    cursor = conn.cursor()

    # Adjust this according to the columns in your dataset
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            cursor.execute(
                "INSERT OR IGNORE INTO strains (name, type, thc_level, cbd_level, flavor, effects, medical_uses) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (row['name'], row['type'], row['thc_level'], row['cbd_level'], row['flavor'], row['effects'], row['medical_uses'])
            )

    conn.commit()
    conn.close()

if __name__ == '__main__':
    import_data_from_csv('strain.csv')  # Change this to the correct path
    print("Data imported successfully.")