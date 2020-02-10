import os.path
from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class PicForm(FlaskForm):
    photo = FileField("Upload Picture", validators=[FileRequired(), FileAllowed(["jpg", "png", "jpeg"])])

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

	return redirect("/index")
	# return switcher("index")

@app.route('/<template>')
def switcher(template):
	try:
		return render_template(f"{template}.html")
	except IOError:
		return render_template("404.html")