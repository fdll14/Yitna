from app import app
from app import mysql

class Wisata:
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tempat_wisata JOIN kategori ON kategori.id_kategori = tempat_wisata.kategori")
        return cursor.fetchall()
    def getOne(self, id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tempat_wisata JOIN kategori ON kategori.id_kategori = tempat_wisata.kategori WHERE id_wisata ="+id)
        return cursor.fetchone()
    def store(self, nama, kategori, kecamatan, kelurahan, deskripsi, gambar):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tempat_wisata (nama, kategori, kecamatan, kelurahan, deskripsi, gambar) VALUES (%s, %s, %s, %s, %s, %s)", (nama, kategori, kecamatan, kelurahan, deskripsi, gambar))
        conn.commit()
        cursor.close()
    def destroy(self,id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tempat_wisata WHERE id_wisata = "+id)
        conn.commit()
        cursor.close()
    def update(self, id, nama, kategori, kecamatan, kelurahan, deskripsi, gambar):
        conn = mysql.connect()
        cursor = conn.cursor()
        if gambar == 'sama':
            cursor.execute("UPDATE tempat_wisata SET nama ='"+nama+"', kategori = '"+kategori+"', kecamatan = '"+kecamatan+"', kelurahan = '"+kelurahan+"', deskripsi = '"+deskripsi+"' WHERE id_wisata = "+id)
        else:
            cursor.execute("UPDATE tempat_wisata SET nama ='"+nama+"', kategori = '"+kategori+"', kecamatan = '"+kecamatan+"', kelurahan = '"+kelurahan+"', deskripsi = '"+deskripsi+"', gambar = '"+gambar+"' WHERE id_wisata = "+id)
        conn.commit()
        cursor.close()
    def getCurrentFile(self, id_wisata):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT gambar FROM tempat_wisata WHERE id_wisata ="+id_wisata)
        return cursor.fetchone()
    def kecamatan(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kecamatan")
        return cursor.fetchall()
    def kelurahan(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM kelurahan")
        return cursor.fetchall()
    def getLimit(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT tempat_wisata.id_wisata,tempat_wisata.nama, kategori.kategori, tempat_wisata.gambar, kecamatan.nama, kelurahan.nama FROM `tempat_wisata` JOIN kategori ON tempat_wisata.kategori = kategori.id_kategori JOIN kecamatan ON kecamatan.id_kecamatan = tempat_wisata.kecamatan JOIN kelurahan ON kelurahan.id_kelurahan = tempat_wisata.kelurahan LIMIT 8")
        return cursor.fetchall()
    def getWhereKategori(self, id_kategori):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT tempat_wisata.id_wisata,tempat_wisata.nama, kategori.kategori, tempat_wisata.gambar, kecamatan.nama, kelurahan.nama FROM `tempat_wisata` JOIN kategori ON tempat_wisata.kategori = kategori.id_kategori JOIN kecamatan ON kecamatan.id_kecamatan = tempat_wisata.kecamatan JOIN kelurahan ON kelurahan.id_kelurahan = tempat_wisata.kelurahan WHERE kategori.id_kategori = "+id_kategori)
        return cursor.fetchall()
    def getDetailWisata(self, id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT tempat_wisata.nama, tempat_wisata.gambar,tempat_wisata.deskripsi, kecamatan.nama,kelurahan.nama, persebaran_corona.isoman,persebaran_corona.dirawat,persebaran_corona.sembuh,persebaran_corona.meninggal FROM tempat_wisata JOIN kecamatan ON kecamatan.id_kecamatan = tempat_wisata.kecamatan JOIN kelurahan ON kelurahan.id_kelurahan = tempat_wisata.kelurahan JOIN persebaran_corona ON persebaran_corona.id_kec = kecamatan.id_kecamatan WHERE id_wisata = "+id)
        return cursor.fetchall()
    def getLikeKeyword(self, keyword):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT tempat_wisata.id_wisata,tempat_wisata.nama, kategori.kategori, tempat_wisata.gambar, kecamatan.nama, kelurahan.nama FROM `tempat_wisata` JOIN kategori ON tempat_wisata.kategori = kategori.id_kategori JOIN kecamatan ON kecamatan.id_kecamatan = tempat_wisata.kecamatan JOIN kelurahan ON kelurahan.id_kelurahan = tempat_wisata.kelurahan WHERE tempat_wisata.nama LIKE '%"+keyword+"%'")
        return cursor.fetchall()