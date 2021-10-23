from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float(10), nullable=False)


# db.create_all()
all_books = []


@app.route("/")
def home():
    all_books = Books.query.all()
    return render_template("index.html", books=all_books)


@app.route('/add', methods=['POST', 'GET'])
def add_books():
    if request.method == "POST":
        title = request.form['book_name']
        author = request.form['book_author']
        rating = request.form['book_rating']
        new_entry = Books(title=title, author=author, rating=rating)
        db.session.add(new_entry)
        db.session.commit()
        return redirect('/')
    return render_template("add.html")


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    books_id = request.args.get("id")
    book_to_delete = Books.query.get(books_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect('/')


@app.route("/edit", methods=["POST", "GET"])
def edit():
    books_id = request.args.get("id")
    get_book = Books.query.filter_by(id=books_id).first()
    if request.method == "POST":
        book_to_update = Books.query.get(request.form['id'])
        book_to_update.rating = request.form['books_rating']
        db.session.commit()
        return redirect('/')

    return render_template("edit.html", book=get_book)


if __name__ == "__main__":
    app.run(debug=True)


'''
IF WER WERE USING SQLITE3

# Initialize connection
db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) "
#                "NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(2, 'Not Mint', ' Rowling', '5')")
db.commit()

'''