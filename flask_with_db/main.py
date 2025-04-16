import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# Migrate(app, db)

'''
Klasėje Book mus domina publisher_id kintamasis. Jis susieja klasę Book su klase Publisher per ForeignKey, 
kuriame parametruose nurodytas kitos lentelės pavadinimas ir prie kurio lauko rišame, t.y. prie id, 
kuris publishers lentelėje yra primary_key. 
'''
class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(150))
    title = db.Column(db.String(300))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))

    def __init__(self, author, title, publisher_id):
        self.author = author
        self.title = title
        self.publisher_id = publisher_id

    def __repr__(self):
        return self.title

'''
Klasėje Publisher, atgalinį ryšį su Books klase sukuria books kintamąjam priskirta eilutė. 
Parametruose nurodyta klasė, su kuria siejame ir backref - kol kas žiūrėkite, kaip į papildomą 
saitą tarp python klasių. 
'''
class Publisher(db.Model):

    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    books = db.relationship('Book', backref='publisher')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


@app.route('/publisher', methods=['POST'])
def index():
    data = request.get_json()
    name = data['name']
    publisher = Publisher(name)
    db.session.add(publisher)
    db.session.commit()
    return {"message": "Publisher added successfully"}, 201


@app.route('/publishers')
def get_publishers():
    publishers = Publisher.query.all()
    return [{"id": publisher.id, "name": publisher.name} for publisher in publishers], 200

@app.route('/publisher/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_publisher(id):
    publisher = Publisher.query.get(id)
    if request.method == 'GET':
        return {"id": publisher.id, "name": publisher.name}, 200
    elif request.method == 'PUT':
        data = request.get_json()
        publisher.name = data['name']
        db.session.commit()
        return {"message": "Publisher updated successfully"}, 200
    elif request.method == 'DELETE':
        db.session.delete(publisher)
        db.session.commit()
        return {"message": "Publisher deleted successfully"}, 200
    
@app.route('/book', methods=['POST'])
def add_book():
    data = request.get_json()
    author = data['author']
    title = data['title']
    publisher_id = data['publisher_id']
    book = Book(author, title, publisher_id)
    db.session.add(book)
    db.session.commit()
    return {"message": "Book added successfully"}, 201


@app.route('/books')
def get_books():
    books = Book.query.all()
    return [{"id": book.id, "author": book.author, "title": book.title, "publisher_id": book.publisher_id} for book in books], 200


@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_book(id):
    book = Book.query.get(id)
    if request.method == 'GET':
        return {"id": book.id, "author": book.author, "title": book.title, "publisher_id": book.publisher_id}, 200
    elif request.method == 'PUT':
        data = request.get_json()
        book.author = data['author']
        book.title = data['title'] 
        book.publisher_id = data['publisher_id']
        db.session.commit()
        return {"message": "Publisher updated successfully"}, 200
    elif request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return {"message": "Publisher deleted successfully"}, 200


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(port=5001, debug=True)