from app import app
from app import mysql
from app import bcrypt

class Satgas:
    def get(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE role = 'satgas'")
        return cursor.fetchall()
    def getOne(self, id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user WHERE id_user ="+id)
        return cursor.fetchone()
    def store(self, username, nama, email, tgl_lahir, no_hp, alamat, jk):
        key = bcrypt.generate_password_hash(username)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (username, password, nama, email, tgl_lahir, no_hp, alamat, jk, role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (username, key, nama, email, tgl_lahir, no_hp, alamat, jk, "satgas"))
        conn.commit()
        cursor.close()
    def destroy(self,id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM user WHERE id_user = "+id)
        conn.commit()
        cursor.close()
    def update(self, id, nama, email, tgl_lahir, no_hp, alamat, jk):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE user SET nama ='"+nama+"', email = '"+email+"', tgl_lahir = '"+tgl_lahir+"', no_hp = '"+no_hp+"', alamat = '"+alamat+"', jk = '"+jk+"' WHERE id_user = "+id)
        conn.commit()
        cursor.close()