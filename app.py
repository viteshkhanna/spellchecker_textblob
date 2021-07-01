from logging import debug
from flask import Flask , render_template , request
from textblob import TextBlob
from textblob import Word


app = Flask(__name__)

@app.route('/home')
def Welcome():
    return render_template('base.html')

@app.route('/correction', methods = ['GET','POST'])
def predict():
    a = request.form.get('word')
    blob = TextBlob(a)
    correction = blob.correct()
    x = blob.words[0].spellcheck()
    return render_template('base.html' ,correction_text = f" {correction} , {x}")

app.run(host = "0.0.0.0",debug=True)