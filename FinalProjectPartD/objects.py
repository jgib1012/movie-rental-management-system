# objects.py

class Movie:
    def __init__(self, title, genre, rating, year):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

class Rental:
    def __init__(self, email, movie_title, rental_date):
        self.email = email
        self.movie_title = movie_title
        self.rental_date = rental_date
