import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM events WHERE date="2088.10.15"')

rows = cursor.fetchall()
print(rows)

# new_rows = [('Cats', 'Cat City', '2088.10.15'), ('Hens', 'Hen City', '2088.15.10')]
# cursor.executemany('INSERT INTO events VALUES (?, ?, ?)', new_rows)
# connection.commit()

