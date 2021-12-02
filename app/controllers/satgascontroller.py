import os
from flask import (Flask, render_template, url_for, request, abort, redirect, make_response, session, flash, abort, jsonify)
from app import app
from uuid import uuid4
from app import mysql
from app.models.monitoring import Monitoring
from app.models.riwayat import Riwayat
from app.models.yolo import Yolo
from app.models.persebaran import Persebaran

def make_unique(string):
    ident = uuid4().__str__()[:8]
    return f"{ident}-{string}"

@app.route('/satgas', methods = ['GET', 'POST'])
def satgas():
    if request.method == "POST":
        riwayat = Riwayat()
        inputan = request.form
        kamera = inputan['kamera']
        from_date = inputan['tgl_awal']
        to_date = inputan['tgl_akhir']

        chart = riwayat.getWithFilter(kamera, from_date, to_date)
        violations = list()
        time = list()

        for f in chart:
            violations.append(f[2])
            time.append(f[4])

        persebaran = Persebaran()
        monitoring = Monitoring()
            
        data = {
            'persebaran': persebaran.get(),
            'kamera': monitoring.get(),
            'violations': violations,
            'time': time
        }
        
        return render_template('satgas/index.html', data=data)
    else:
        if not session.get('id'):
            return redirect(url_for('login'))
        else:
            persebaran = Persebaran()
            monitoring = Monitoring()
            

            data = {
                'persebaran': persebaran.get(),
                'kamera': monitoring.get()
            }
            return render_template('satgas/index.html', data=data)

# MY BAZOKA
@app.route('/satgas/camera/<id>', methods = ['GET'])
def satgasoncam(id=None):
    monitoring = Monitoring()
    data = monitoring.getOne(id)
    id_cam = data[0]
    ip = data[2]
    yolo = Yolo()
    yolo.start_cam(mysql, ip, id_cam)
    return redirect(url_for('satgas_monitoring', idx='all'))
    
# KAMERA
@app.route('/satgas/monitoring/<idx>', methods = ['GET', 'POST'])
def satgas_monitoring(idx='all'):
    if request.method == "POST":
        monitoring = Monitoring()
        inputan = request.form
        monitoring.store(inputan['nama'], inputan['ip_address'], inputan['lokasi'])
        flash('Berhasil tambah data')
        return redirect(url_for('satgas_monitoring', idx='all'))
    elif request.method == "GET" :
        if idx == 'all':
            monitoring = Monitoring()
            data = monitoring.get()
            return render_template('satgas/monitoring.html', data=data)
        else:
            monitoring = Monitoring()
            data = monitoring.getOne(idx)
            return jsonify(result=data)
@app.route('/satgas/monitoring/delete/<idx>', methods = ['GET'])
def satgas_monitoring_delete(idx=None):
    monitoring = Monitoring()
    monitoring.destroy(idx)
    flash('Berhasil hapus data')
    return redirect(url_for('satgas_monitoring', idx='all'))
@app.route('/satgas/monitoring/update', methods = ['POST'])
def satgas_monitoring_update():
    monitoring = Monitoring()
    inputan = request.form
    monitoring.update(inputan['id'], inputan['nama'], inputan['ip_address'], inputan['lokasi'])
    flash('Berhasil update data')
    return redirect(url_for('satgas_monitoring', idx='all'))

# RIWAYAT
@app.route('/satgas/riwayat/<idx>', methods = ['GET', 'POST'])
def satgas_riwayat(idx='all'):
    if request.method == "POST":
        monitoring = Monitoring()
        riwayat = Riwayat()
        inputan = request.form
        
        data = {
            'riwayat':riwayat.getWithFilter(inputan['kamera'], inputan['tgl_awal'], inputan['tgl_akhir']),
            'kamera':monitoring.get()
        }
        
        return render_template('satgas/riwayat.html', data=data)
    elif request.method == "GET" :
        if idx == 'all':
            riwayat = Riwayat()
            monitoring = Monitoring()
            data = {
                'riwayat':riwayat.get(),
                'kamera':monitoring.get()
            }
            return render_template('satgas/riwayat.html', data=data)