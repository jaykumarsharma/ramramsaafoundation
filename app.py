from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:@localhost/ramramsaafoundation'
db = SQLAlchemy(app)

class donators(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(80), nullable=False)
    billname = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    pin = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    pan = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(6), nullable=True)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(6), nullable=True)
    email = db.Column(db.String(20), nullable=False)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact" , methods=['GET','POST'])
def contact():
  if(request.method=='POST'):
     '''Add entry to the database'''
     name = request.form.get('name')
     email = request.form.get('email')
     phone = request.form.get('phone')
     message = request.form.get('message')
     entry = Contacts(name=name, phone = phone, msg = message, date= datetime.now(),email = email )
     db.session.add(entry)
     db.session.commit()
  return render_template('contact.html')

@app.route("/services")
def services():
    return render_template('services.html')
    


@app.route("/donate" , methods=['GET','POST'])
def donate():
    if(request.method=='POST'):
     '''Add entry to the database'''
     amount  = request.form.get('amount')
     billname = request.form.get('billname')
     address = request.form.get('address')
     email = request.form.get('email')
     state = request.form.get('state')
     pin = request.form.get('pin')
     phone = request.form.get('phone')
     pan = request.form.get('pan')
     entry1 = donators(amount= amount, billname=billname, address=address, state=state , pin = pin, phone = phone,email = email , pan = pan , date= datetime.now())
     db.session.add(entry1)
     db.session.commit()
    return render_template('donate.html')

if __name__ == '__main__':
        app.run(debug=True)
