import sqlite3
import csv

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

c.execute('SELECT * FROM tasks')
rows = c.fetchall()

# Optional: Get column names for the CSV header
column_names = [description[0] for description in c.description]

# Specify CSV output file path
csv_file_path = 'tasks_export.csv'

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    # Write header
    csv_writer.writerow(column_names)
    # Write data rows
    csv_writer.writerows(rows)

print(f"Exported {len(rows)} rows to {csv_file_path}")

conn.close()

