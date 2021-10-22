from db import db, Books, app, request, render_template

# db.create_all()
all_books = []

new_entry = Books(title="f Potter", author="J.K Rowlling", rating="9.5")
db.session.add(new_entry)
db.session.commit()


@app.route("/")
def home():
    return render_template("index.html", books=all_books)


@app.route('/add', methods=['POST', 'GET'])
def add_books():
    if request.method == "POST":
        all_books.append({
            "title": request.form['book_name'],
            "author": request.form['book_author'],
            "rating": request.form['book_rating']
        })

    return render_template("add.html")


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