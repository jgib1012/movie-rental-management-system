# db.py

import sqlite3
from objects import Movie, Rental

def connect():
    return sqlite3.connect("movies.db")

def create_tables():
    with connect() as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS Movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                genre TEXT,
                rating TEXT,
                year TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS Rentals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT,
                movie_id INTEGER,
                rental_date TEXT,
                FOREIGN KEY(movie_id) REFERENCES Movies(id)
            )
        ''')

def add_movie(movie):
    with connect() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Movies (title, genre, rating, year) VALUES (?, ?, ?, ?)",
                  (movie.title, movie.genre, movie.rating, movie.year))

def get_movies():
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT title, genre, rating, year FROM Movies")
        return [Movie(*row) for row in c.fetchall()]

def add_rental(rental):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT id FROM Movies WHERE title = ?", (rental.movie_title,))
        result = c.fetchone()
        if result:
            movie_id = result[0]
            c.execute("INSERT INTO Rentals (email, movie_id, rental_date) VALUES (?, ?, ?)",
                      (rental.email, movie_id, rental.rental_date))

def get_rentals_by_email(email):
    with connect() as conn:
        c = conn.cursor()
        c.execute('''SELECT m.title, r.rental_date
                     FROM Rentals r
                     JOIN Movies m ON r.movie_id = m.id
                     WHERE r.email = ?''', (email,))
        return [Rental(email, title, date) for title, date in c.fetchall()]
