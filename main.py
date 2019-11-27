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

			return render_template("song.html", songname=songname, mood = mood, song_id = song_id, name = name)
	else:
		return Response(500)

if __name__ == "__main__":
    app.run(debug=True)
