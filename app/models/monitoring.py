from app import app
from app import mysql

class Monitoring:
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cameras")
        return cursor.fetchall()
    def getOne(self, id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cameras WHERE id_cam ="+id)
        return cursor.fetchone()
    def store(self, nama, ip_address, lokasi):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO cameras (nama, ip_address, location) VALUES (%s, %s, %s)", (nama, ip_address, lokasi))
        conn.commit()
        cursor.close()
    def destroy(self,id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cameras WHERE id_cam = "+id)
        conn.commit()
        cursor.close()
    def update(self, id, nama, ip_address, lokasi):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE cameras SET nama ='"+nama+"', ip_address = '"+ip_address+"', location = '"+lokasi+"' WHERE id_cam = "+id)
        conn.commit()
        cursor.close()