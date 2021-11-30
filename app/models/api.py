from app import app
from app import mysql
from flask import Flask, jsonify, request

class Api:
    def getApiAll(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pelanggaran")
        return cursor.fetchall()

    def getApiOne(self, id):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pelanggaran WHERE id_cam ="+id)
        return cursor.fetchall()
        
        