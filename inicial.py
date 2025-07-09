import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DROP TABLE IF EXISTS {TABLE_NAME}'
)
connection.commit()

cursor.execute(f"CREATE TABLE IF NOT EXISTS {TABLE_NAME}"
               "("
               "id INTEGER PRIMARY KEY AUTOINCREMENT, "
               "name TEXT,"
               "weight REAL"
               ")"
               )

connection.commit()

#perfeito pra sql injection. Delicinha.
cursor.execute(
    f'INSERT INTO {TABLE_NAME} '
    '(id, name, weight) '
    'VALUES '
    '(NULL, "Helena", 4), '
    '(NULL, "Eduardo", 10)'
)
connection.commit()

sql = (
    f"INSERT INTO {TABLE_NAME}"
    "(name, weight)"
    "VALUES"
    "(?, ?)"
)
cursor.execute(sql, ["Joana", 4])
connection.commit()

cursor.close()
connection.close()