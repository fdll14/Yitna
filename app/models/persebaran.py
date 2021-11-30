from app import app
from app import mysql

class Persebaran:
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(isoman) as isoman, SUM(dirawat) as dirawat, SUM(sembuh) as sembuh, SUM(meninggal) as meninggal FROM `persebaran_corona`")
        return cursor.fetchall()