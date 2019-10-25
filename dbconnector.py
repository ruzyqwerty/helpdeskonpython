import sqlite3

DB_NAME = "helpdeskdb.db"


def get_data(text):
    connector = sqlite3.connect(DB_NAME)
    cursor = connector.cursor()
    return cursor.execute(text).fetchall()


def set_data(text):
    connector = sqlite3.connect(DB_NAME)
    cursor = connector.cursor()
    cursor.execute(text)
    connector.close()
