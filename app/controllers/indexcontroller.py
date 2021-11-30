import os
from flask import render_template, request, redirect, url_for, jsonify
from app import app
import requests
from datetime import date
from uuid import uuid4
import json
from app.models.persebaran import Persebaran
from app.models.kategori import Kategori
from app.models.wisata import Wisata

def make_unique(string):
    ident = uuid4().__str__()[:8]
    return f"{ident}-{string}"

@app.route('/', methods = ['GET'])
def index():
	persebaran = Persebaran()
	kategori = Kategori()
	wisata = Wisata()
	
	data = {
		'persebaran': persebaran.get(),
		'kategori': kategori.get(),
		'wisata': wisata.getLimit()
	}
	return render_template('index.html', data=data)
@app.route('/cari/<keyword>', methods = ['GET'])
def index_cari(keyword):
	persebaran = Persebaran()
	kategori = Kategori()
	wisata = Wisata()
	
	data = {
		'persebaran': persebaran.get(),
		'kategori': kategori.get(),
		'wisata': wisata.getLikeKeyword(keyword),
		'scroll': True
	}
	return render_template('index.html', data=data)
@app.route('/kategori/<id>', methods = ['GET'])
def index_kategori(id):
	persebaran = Persebaran()
	kategori = Kategori()
	wisata = Wisata()
	
	data = {
		'persebaran': persebaran.get(),
		'kategori': kategori.get(),
		'wisata': wisata.getWhereKategori(id),
		'scroll': True
	}
	return render_template('index.html', data=data)
@app.route('/detail/<id>', methods = ['GET'])
def index_detail(id):
	persebaran = Persebaran()
	kategori = Kategori()
	wisata = Wisata()
	
	data = {
		'persebaran': persebaran.get(),
		'kategori': kategori.get(),
		'wisata': wisata.getLimit(),
		'detail': wisata.getDetailWisata(id),
		'scroll': True,
		'display': True
	}
	return render_template('index.html', data=data)
@app.route('/api_guide', methods = ['GET'])
def api_guide():
	return render_template('api.html')


	
	
