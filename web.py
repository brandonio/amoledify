import os.path
from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

fileTypes = ["jpg", "png", "jpeg", "ico", "tiff", "gif"]

class PicForm(FlaskForm):
    photo = FileField("Upload Image", validators=[FileRequired(), FileAllowed(fileTypes)])

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB

@app.route('/', methods=["GET", "POST"])
def index():
	form = PicForm()
	if form.validate_on_submit():
		f = form.photo.data
        filename = secure_filename(f.filename)
	else:
		r
	return redirect("/index")
	# return switcher("index")

# @app.route('/picture/<uuid>')
# def withUUID():

@app.errorhandler(413)
def err413(e):
    return render_template('413.html'), 413

@app.errorhandler(404)
def err404(e):
    return render_template('404.html'), 404
