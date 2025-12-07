

from db import create_tables, add_movie
from objects import Movie

# Movie list copied directly here (safer than importing from main.py)
movies = [
    {"title": "Avengers: Endgame", "genre": "Action/Adventure", "rating": "PG-13", "year": "2019"},
    {"title": "Spider-Man: No Way Home", "genre": "Action/Adventure", "rating": "PG-13", "year": "2021"},
    {"title": "The Dark Knight", "genre": "Action/Adventure", "rating": "PG-13", "year": "2008"},
    {"title": "Captain America: Civil War", "genre": "Action/Adventure", "rating": "PG-13", "year": "2016"},
    {"title": "Black Panther", "genre": "Action/Adventure", "rating": "PG-13", "year": "2018"},
    {"title": "The Matrix", "genre": "Action/Adventure", "rating": "R", "year": "1999"},
    {"title": "John Wick", "genre": "Action/Adventure", "rating": "R", "year": "2014"},
    {"title": "Kill Bill Vol. 1", "genre": "Action/Adventure", "rating": "R", "year": "2003"},
    {"title": "Gladiator", "genre": "Action/Adventure", "rating": "R", "year": "2000"},
    {"title": "Mad Max: Fury Road", "genre": "Action/Adventure", "rating": "R", "year": "2015"},
    {"title": "Toy Story 3", "genre": "Animation", "rating": "PG", "year": "2010"},
    {"title": "The Lion King", "genre": "Animation", "rating": "PG", "year": "1994"},
    {"title": "The Prince of Egypt", "genre": "Animation", "rating": "PG", "year": "1998"},
    {"title": "Frozen", "genre": "Animation", "rating": "PG", "year": "2013"},
    {"title": "Shrek", "genre": "Animation", "rating": "PG", "year": "2001"},
    {"title": "Insidious", "genre": "Horror", "rating": "PG-13", "year": "2010"},
    {"title": "A Quiet Place", "genre": "Horror", "rating": "PG-13", "year": "2018"},
    {"title": "The Ring", "genre": "Horror", "rating": "PG-13", "year": "2002"},
    {"title": "The Others", "genre": "Horror", "rating": "PG-13", "year": "2001"},
    {"title": "Scary Stories to Tell in the Dark", "genre": "Horror", "rating": "PG-13", "year": "2019"},
    {"title": "The Conjuring", "genre": "Horror", "rating": "R", "year": "2013"},
    {"title": "Hereditary", "genre": "Horror", "rating": "R", "year": "2018"},
    {"title": "Get Out", "genre": "Horror", "rating": "R", "year": "2017"},
    {"title": "The Exorcist", "genre": "Horror", "rating": "R", "year": "1973"},
    {"title": "It", "genre": "Horror", "rating": "R", "year": "2017"},
    {"title": "Pitch Perfect", "genre": "Comedy", "rating": "PG-13", "year": "2012"},
    {"title": "Mean Girls", "genre": "Comedy", "rating": "PG-13", "year": "2004"},
    {"title": "School of Rock", "genre": "Comedy", "rating": "PG-13", "year": "2003"},
    {"title": "Yes Man", "genre": "Comedy", "rating": "PG-13", "year": "2008"},
    {"title": "The Proposal", "genre": "Comedy", "rating": "PG-13", "year": "2009"},
    {"title": "Ted", "genre": "Comedy", "rating": "R", "year": "2012"},
    {"title": "The Hangover", "genre": "Comedy", "rating": "R", "year": "2009"},
    {"title": "Superbad", "genre": "Comedy", "rating": "R", "year": "2007"},
    {"title": "Step Brothers", "genre": "Comedy", "rating": "R", "year": "2008"},
    {"title": "Pineapple Express", "genre": "Comedy", "rating": "R", "year": "2008"},
    {"title": "Star Wars Revenge of the Sith", "genre": "Sci-Fi", "rating": "PG-13", "year": "2005"},
    {"title": "Inception", "genre": "Sci-Fi", "rating": "PG-13", "year": "2010"},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": "PG-13", "year": "2014"},
    {"title": "Avatar", "genre": "Sci-Fi", "rating": "PG-13", "year": "2009"},
    {"title": "Dune", "genre": "Sci-Fi", "rating": "PG-13", "year": "2021"}
]

# Create tables and insert movies
create_tables()

for m in movies:
    add_movie(Movie(m["title"], m["genre"], m["rating"], m["year"]))

print("✅ Database created and movies inserted.")
