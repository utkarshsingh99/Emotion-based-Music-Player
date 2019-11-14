from flask import Flask, render_template, request, redirect, url_for
import paralleldots
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/'
paralleldots.set_api_key("Kyy830QxC01AsSg9Y4eYFtQo5JYAK6l7zc9jIJ1oNJ8")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/")
def home():
	# path = "/home/utkarsh/Pictures/parallel.jpg"
	# resp = paralleldots.facial_emotion( path )
	# print(resp)
	return render_template("home.html")

@app.route("/song", methods = ['GET', 'POST'])
def song():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

if __name__ == "__main__":
    app.run(debug=True)