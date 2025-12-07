import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from db import get_movies, get_rentals_by_email, add_rental
from objects import Rental

def create_ui():
    root = tk.Tk()
    root.title("Movie Rental System")
    root.geometry("1100x600")
    root.configure(bg="black")

    # Movie Catalog Frame
    catalog_frame = tk.Frame(root, bg="black")
    catalog_frame.place(x=10, y=10, width=530, height=580)

    tk.Label(catalog_frame, text="Movie Catalog", bg="white", font=("Times New Roman", 14, "bold"), bd=1, relief="solid").pack(fill="x")
    search_entry = tk.Entry(catalog_frame, font=("Times New Roman", 12), relief="solid", bd=1)
    search_entry.pack(pady=10, padx=10, fill="x")

    tk.Label(catalog_frame, text="Genre", bg="white", fg="black", relief="solid", bd=1).pack(pady=2, padx=10, anchor="w")
    genre_dropdown = ttk.Combobox(catalog_frame, values=["All", "Action/Adventure", "Sci-Fi", "Animation", "Horror", "Comedy"])
    genre_dropdown.set("All")
    genre_dropdown.pack(pady=2, padx=10, fill="x")

    tk.Label(catalog_frame, text="Rating", bg="white", fg="black", relief="solid", bd=1).pack(pady=2, padx=10, anchor="w")
    rating_dropdown = ttk.Combobox(catalog_frame, values=["All", "G", "PG", "PG-13", "R"])
    rating_dropdown.set("All")
    rating_dropdown.pack(pady=2, padx=10, fill="x")

    movie_tree = ttk.Treeview(catalog_frame, columns=("Title", "Genre", "Rating", "Year"), show="headings")
    for col in movie_tree["columns"]:
        movie_tree.heading(col, text=col)
    movie_tree.pack(expand=True, fill="both", padx=10, pady=10)

    def apply_filters():
        genre = genre_dropdown.get()
        rating = rating_dropdown.get()
        keyword = search_entry.get().lower()
        movie_tree.delete(*movie_tree.get_children())
        for m in get_movies():
            if (genre == "All" or m.genre == genre) and \
               (rating == "All" or m.rating == rating) and \
               (keyword in m.title.lower()):
                movie_tree.insert("", "end", values=(f"{m.title} ({m.year})", m.genre, m.rating, m.year))

    tk.Button(catalog_frame, text="Apply Filters", font=("Times New Roman", 10), command=apply_filters).pack(pady=10)

    # Customer Rentals Frame
    rental_frame = tk.Frame(root, bg="black")
    rental_frame.place(x=560, y=10, width=530, height=580)

    tk.Label(rental_frame, text="Customer Rentals", bg="white", font=("Times New Roman", 14, "bold"), bd=1, relief="solid").pack(fill="x")

    tk.Label(rental_frame, text="Customer Email", bg="white", fg="black", relief="solid", bd=1).pack(pady=5, padx=10, anchor="w")
    email_entry = tk.Entry(rental_frame, font=("Times New Roman", 12), relief="solid", bd=1)
    email_entry.pack(padx=10, fill="x")

    # Add a checkbox (example use: confirm rental)
    confirm_var = tk.BooleanVar()
    confirm_check = tk.Checkbutton(rental_frame, text="Confirm Rental", variable=confirm_var, bg="black", fg="white", selectcolor="black")
    confirm_check.pack(pady=10)

    
    def load_rentals():
        email = email_entry.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter customer email.")
            return
        rental_tree.delete(*rental_tree.get_children())
        for r in get_rentals_by_email(email):
            rental_tree.insert("", "end", values=(r.movie_title, r.rental_date))

    tk.Button(rental_frame, text="Load Rentals", command=load_rentals).pack(pady=5)

    tk.Label(rental_frame, text="Movie", bg="white", fg="black", relief="solid", bd=1).pack(pady=5, padx=10, anchor="w")
    movie_dropdown = ttk.Combobox(rental_frame, values=[m.title for m in get_movies()])
    movie_dropdown.pack(padx=10, fill="x")

    def rent_movie():
        selected_movie = movie_dropdown.get()
        email = email_entry.get().strip()
        if not selected_movie or not email:
            messagebox.showerror("Error", "Please enter email and select a movie.")
            return
        rental_date = datetime.now().strftime("%Y-%m-%d")
        rental = Rental(email, selected_movie, rental_date)
        add_rental(rental)
        rental_tree.insert("", "end", values=(selected_movie, rental_date))

    tk.Button(rental_frame, text="Rent Movie", command=rent_movie).pack(pady=10)
    tk.Button(rental_frame, text="Checkout", bg="white", font=("Times New Roman", 10)).pack(pady=5)

    rental_tree = ttk.Treeview(rental_frame, columns=("Movie", "Rental Date"), show="headings")
    rental_tree.heading("Movie", text="Movie")
    rental_tree.heading("Rental Date", text="Rental Date")
    rental_tree.pack(expand=True, fill="both", padx=10, pady=10)

    root.mainloop()

create_ui()
