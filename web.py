from flask import Flask, request, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from PIL import Image
from amoledify import amoledify
import uuid
import os

FILE_TYPES = ["jpg", "png", "jpeg", "ico", "tiff", "gif"]
FILE_TYPES_STRING = ", ".join(FILE_TYPES)
MAX_MB = 16

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = MAX_MB * 1024 * 1024
app.config["SECRET_KEY"] = "idkletstrythisfornow"

class PicForm(FlaskForm):
	photo = FileField("Upload Image", validators=[FileRequired(), FileAllowed(FILE_TYPES)])

@app.route("/", methods=["GET", "POST"])
def index():
	form = PicForm()
	if form.validate_on_submit():
		f = amoledify(pic=form.photo.data, fg=(255, 255, 255))
		filename = secure_filename(form.photo.data.filename)
		_, extension = os.path.splitext(filename)
		name = str(uuid.uuid4())[:4] + extension
		path = os.path.join("static/images", name)
		f.save(path)
		return redirect(url_for("result", name=name))
	return render_template("index.html", form=form, fileTypes=FILE_TYPES_STRING, maxMB = MAX_MB)

@app.route("/result/<name>")
def result(name):
	src = url_for("static", filename="images/" + name)
	return render_template("result.html", src=src)


@app.errorhandler(404)
@app.errorhandler(413)
def err(e):
	return render_template("404.html"), 404

if __name__ == "__main__":
	app.run()
