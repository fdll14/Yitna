import os
from flask import (Flask, render_template, url_for, request, abort, redirect, make_response, session, flash, abort, jsonify)
from app import app
from uuid import uuid4
from werkzeug.utils import secure_filename
from app.models.satgas import Satgas
from app.models.wisata import Wisata
from app.models.user import User

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def make_unique(string):
    ident = uuid4().__str__()[:8]
    return f"{ident}-{string}"

# ADMIN
@app.route('/admin', methods = ['GET'])
def admin():
    if not session.get('id'):
        return redirect(url_for('login'))
    else:
        user = User()
        data = user.getOneId(str(session.get('id')))
        if data[0] == 'satgas':
            return redirect(url_for('satgas'))
        else:
            return render_template('admin/index.html')
@app.route('/admin/satgas/<idx>', methods = ['GET', 'POST'])
def admin_satgas(idx='all'):
    if request.method == "POST":
        satgas = Satgas()
        inputan = request.form
        username = make_unique(inputan['nama'])
        satgas.store(username, inputan['nama'], inputan['email'], inputan['tgl_lahir'], inputan['no_hp'], inputan['alamat'], inputan['jk'])
        flash('Berhasil tambah data')
        return redirect(url_for('admin_satgas', idx='all'))
    elif request.method == "GET" :
        if idx == 'all':
            satgas = Satgas()
            data = satgas.get()
            return render_template('admin/satgas.html', data=data)
        else:
            satgas = Satgas()
            data = satgas.getOne(idx)
            return jsonify(result=data)
            
@app.route('/admin/satgas/delete/<idx>', methods = ['GET'])
def admin_satgas_delete(idx=None):
    satgas = Satgas()
    data = satgas.destroy(idx)
    flash('Berhasil hapus data')
    return redirect(url_for('admin_satgas', idx='all'))
@app.route('/admin/satgas/update', methods = ['POST'])
def admin_satgas_update():
    satgas = Satgas()
    inputan = request.form
    satgas.update(inputan['id'], inputan['nama'], inputan['email'], inputan['tgl_lahir'], inputan['no_hp'], inputan['alamat'], inputan['jk'])
    flash('Berhasil update data')
    return redirect(url_for('admin_satgas', idx='all'))

# WISATA
@app.route('/admin/wisata/<idx>', methods = ['GET', 'POST'])
def admin_wisata(idx='all'):
    if request.method == "POST":
        file = request.files['foto']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = make_unique(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        wisata = Wisata()
        inputan = request.form
        wisata.store(inputan['nama'], inputan['kecamatan'], inputan['kelurahan'], inputan['deskripsi'], filename)
        flash('Berhasil tambah data')
        return redirect(url_for('admin_wisata', idx='all'))
    elif request.method == "GET" :
        if idx == 'all':
            wisata = Wisata()
            data = {
                'wisata':wisata.get(),
                'kecamatan':wisata.kecamatan(),
                'kelurahan':wisata.kelurahan()
            }
            return render_template('admin/wisata.html', data=data)
        else:
            wisata = Wisata()
            data = wisata.getOne(idx)
            return jsonify(result=data)
            
@app.route('/admin/wisata/delete/<idx>', methods = ['GET'])
def admin_wisata_delete(idx=None):
    wisata = Wisata()
    data = wisata.destroy(idx)
    flash('Berhasil hapus data')
    return redirect(url_for('admin_wisata', idx='all'))
@app.route('/admin/wisata/update', methods = ['POST'])
def admin_wisata_update():
    
    if not request.files['foto'] :
        filename = 'sama'
    else :
        file = request.files['foto']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename = make_unique(filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else :
            return redirect(url_for('admin_wisata', idx='all'))

    wisata = Wisata()
    inputan = request.form
    wisata.update(inputan['id'], inputan['nama'], inputan['kecamatan'], inputan['kelurahan'], inputan['deskripsi'], filename)
    flash('Berhasil update data')
    return redirect(url_for('admin_wisata', idx='all'))