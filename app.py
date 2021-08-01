from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
  return render_template('contact.html')

@app.route("/services")
def services():
    return render_template('services.html')
    
@app.route("/donate")
def donate():
    return render_template('donate.html')

@app.route("/career")
def career():
    return render_template('career.html')

if __name__ == '__main__':
     app.run(debug=True)
