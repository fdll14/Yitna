from app import app
from app import mysql

class Riwayat: 
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pelanggaran JOIN cameras USING(id_cam)")
        return cursor.fetchall()
    def getWithFilter(self, kamera, tgl_awal, tgl_akhir):
        conn = mysql.connect()
        cursor = conn.cursor()
        
        if tgl_awal == '':
            cursor.execute("SELECT * FROM pelanggaran JOIN cameras USING(id_cam) WHERE cameras.id_cam ='"+kamera+"'")
        else:
            if not kamera:
                cursor.execute("SELECT * FROM pelanggaran JOIN cameras USING(id_cam) WHERE pelanggaran.created_at BETWEEN '"+tgl_awal+"' AND '"+tgl_akhir+"'")
            else:
                cursor.execute("SELECT * FROM pelanggaran JOIN cameras USING(id_cam) WHERE cameras.id_cam ='"+kamera+"' AND pelanggaran.created_at BETWEEN '"+tgl_awal+"' AND '"+tgl_akhir+"'")
        return cursor.fetchall()