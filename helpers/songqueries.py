import paralleldots
import mysql.connector
import random

from keys import *

paralleldots.set_api_key(paralleldots_api_key)
cnx = mysql.connector.connect(user = user, password = password, host = '127.0.0.1', database ='moodplayer')
cursor = cnx.cursor()

def find_mood (path):
	# Using ParallelDots API to find the Facial Emotion in the Image
	results = paralleldots.facial_emotion( path )
	user_mood=""
	if 'facial_emotion' in results:
		user_mood = results['facial_emotion'][0]['tag']
	else:
		user_mood = 'Neutral'
	print('Found user_mood', user_mood)
	return user_mood

	# # Finding the mood_id for the predicted mood
	# cursor.execute("select mood_id from moods where moodname = %s", (user_mood,))
	# mood_id=cursor.fetchall()[0][0]
	# print('Found mood_id', mood_id)
	# return mood_id

def find_mood_id ( mood ):
	# Finding the mood_id from mood
	cursor.execute("select mood_id from moods where moodname=%s", (mood, ))
	mood_id = cursor.fetchall()[0][0]
	print("Found mood_id", mood_id)
	return mood_id

def find_user_id (username):
	# Finding the user_id by username
	cursor.execute("select user_id, name from users where username=%s", (username, ))
	(user_id, name)=cursor.fetchall()[0]
	print('Found user_id and name', user_id, name)
	return (user_id, name)

def find_song ( song_id ):
	# Finding the song through the randomly obtained song_id
	cursor.execute("select songname from songs where song_id=%s", (song_id, ))
	songname=cursor.fetchall()[0][0]
	print('Found song: ', songname)
	return songname

def find_song_id (mood_id, user_id):
	# Finding all song_id's that match the user_id and mood_id, and then choosing one from it
	cursor.execute("select song_id from songs where song_id not in (select song_id from mapmoods where user_id=%s AND mood_id = %s) order by rand()", (user_id, mood_id, ))
	song_id=cursor.fetchall()
	if cursor.rowcount == 0 or len(song_id)==0:
		cursor.execute("select song_id from mapmoods where user_id=%s AND mood_id = %s order by rand()", (user_id, mood_id, ))
		total_length = cursor.fetchall()[0][0]
		return random.randint(1, total_length)	
	print(song_id)
	song_id = song_id[0][0]
	cursor.execute("insert into mapmoods (user_id, song_id, mood_id) values (%s, %s, %s)", (user_id, song_id, mood_id,))
	cnx.commit()
	print('Found song_id', song_id)
	return song_id

def did_not_like (user_id, mood, song_id):
	# user_id = find_user_id ( username )
	mood_id = find_mood_id ( mood )
	cursor.execute("delete from mapmoods where mood_id =%s AND user_id = %s order by rand() limit 1", (mood_id, user_id, ))
	cnx.commit()
	# Finding new song to play
	new_song_id = find_song_id ( mood_id, user_id )
	print(new_song_id)
	return new_song_id