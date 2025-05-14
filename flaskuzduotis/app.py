import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect
from forms import MessageForm

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# pilnas kelias iki šio failo.
# app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
# nustatėme, kad mūsų duomenų bazė bus šalia šio failo esants data.sqlite failas
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# neseksime kiekvienos modifikacijos
db = SQLAlchemy(app)
# sukuriame duomenų bazės objektą
# sukurkime modelį užklausos formai, kuris sukurs duomenų bazėje lentelę

SECRET_KEY = "my_secret_key"
app.config['SECRET_KEY'] = SECRET_KEY

class Message(db.Model):
    # DB lentelei priskiria pavadinimą, jei nenurodysite, priskirs automatiškai pagal klasės pavadinimą.
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)  # stulpelis, kurio reikšmės integer. Taip pat jis bus primary_key.
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, surname, message):
        self.name = name
        self.surname = surname
        self.message = message
 

    def __repr__(self):
        return f'{self.name} - {self.created_at}'
    
@app.route("/", methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        message = form.message.data
        new_message = Message(name, surname, message)
        db.session.add(new_message)
        db.session.commit()
        
        return redirect(url_for("index"))
    messages = Message.query.all()
    return render_template("index.html", form=form)


@app.route("/about")
def about():
    return render_template("index.html")
    


with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 