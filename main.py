# -*- coding: utf-8 -*-
from flask import *
import paralleldots
from werkzeug.utils import secure_filename
import os
import mysql.connector
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'madmajksgdckua'
UPLOAD_FOLDER = '/static'
paralleldots.set_api_key("Kyy830QxC01AsSg9Y4eYFtQo5JYAK6l7zc9jIJ1oNJ8")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

cnx = mysql.connector.connect(user = 'wanderer', password = 'admin', host = '127.0.0.1', database ='moodplayer')
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
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file == '':
			flash('No selected file')
			return redirect(request.url)
		if file:
			filename = secure_filename(file.filename)
			print(os.path.abspath(os.path.join(app.config['UPLOAD_FOLDER'], filename)))
			file.save(filename)
			path=filename
			results = paralleldots.facial_emotion( path )
			print(results['facial_emotion'][0])
			genre = results['facial_emotion'][0]['tag']
			# cur = mysql.connection.cursor()
			cursor.execute("select * from songs where mood = %s;", ('neutral',))
			a=[]
			for song in cursor:
				a.append(song[0])
			result=random.choice(a)
			print(result)

			# cursor.close()
			# mysql.connection.commit()
			# cur.close()
			return Response(result)
	else:
		return Response(500)

if __name__ == "__main__":
    app.run(debug=True)
