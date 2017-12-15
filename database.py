import sqlite3
import sys

SCORE_TABLE_NAME = "score"

class Database:
    def __init__(self, target):
        conn = sqlite3.connect("test1.db")
        cur = conn.cursor()
        cur.execute("DROP table  if exists employee;")
        conn.commit()
