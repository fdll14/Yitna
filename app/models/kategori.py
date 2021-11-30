from app import app
from app import mysql

class Kategori:
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kategori")
        return cursor.fetchall()