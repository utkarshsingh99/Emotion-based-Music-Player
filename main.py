# -*- coding: utf-8 -*-
from flask import *
import paralleldots
from werkzeug.utils import secure_filename
import os
import mysql.connector
from werkzeug.datastructures import ImmutableMultiDict

from keys import *
from helpers.songqueries import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'madmajksgdckua'
UPLOAD_FOLDER = '/static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

cnx = mysql.connector.connect(user = user, password = password, host = '127.0.0.1', database ='moodplayer')
cursor = cnx.cursor()

@app.route("/")
def home():
	# path = "/home/utkarsh/Pictures/parallel.jpg"
	# resp = paralleldots.facial_emotion( path )
	# print(resp)
	return render_template("home.html")

@app.route("/song", methods = ['GET', 'POST'])
def song():
	if request.method == 'POST':
		# Extracting the data to retrieve username
		data = dict(request.form)
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		
		# Extracting username and file from the POST request
		username = data['username']
		file = request.files['file']

		if file == '':
			flash('No selected file')
			return redirect(request.url)
		if file:
			print('Username Received is: ',username)
			filename = secure_filename(file.filename)
			print(os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
			file.save(filename)
			path=filename

			mood = find_mood( path )

			mood_id = find_mood_id ( mood )			

			(user_id, name) = find_user_id (username )
			
			song_id = find_song_id ( mood_id, user_id )

			songname = find_song ( song_id )

			return render_template("song.html", songname=songname, mood = mood, song_id = song_id, user_id = user_id, name = name)
	else:
		return Response(500)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':	
		return render_template("index.html")
	else:
		data = dict(request.form)
		print('This data? ',data)
		if all(key in data for key in ('username', 'name', 'email', 'password')):
			cursor.execute("INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s)", (data['name'], data['username'], data['email'], data['password'], ))
			cnx.commit()
			return Response(200)
		else:
			return Response(403)

@app.route('/unlike', methods=['GET', 'POST'])
def unlike():
	if request.method == 'POST':
		data = dict(request.form)
		print('The user did not like the following: ', data)
		new_song_id = did_not_like(data['user_id'], data['mood'], data['song_id'])
		songname = find_song ( new_song_id )
		return Response( songname )

@app.route('/liked', methods=['GET', 'POST'])
def like():
	if request.method == 'POST':
		data = dict(request.form)
		print('The user liked the following: ', data)
		mood_id = find_mood_id( data['mood'])
		new_song_id = find_song_id( mood_id, data['user_id'])
		songname = find_song( new_song_id )
		return Response ( songname )

if __name__ == "__main__":
    app.run(debug=True)
