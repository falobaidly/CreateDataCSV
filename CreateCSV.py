import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Define the number of records
num_customers = 50000
num_movies = 1000
num_directors = 200
num_stars = 1000
num_genres = 20
num_cinemas = 100
num_halls = 300
num_promotions = 50
num_showings = 500000
num_transactions = 1000000  # At least 1M records in the fact table
num_tickets = num_transactions * np.random.randint(1, 5)  # Each transaction has 1-5 tickets

# Generate Customers
customers = pd.DataFrame({
    "id": range(1, num_customers + 1),
    "name": [f"Customer {i}" for i in range(1, num_customers + 1)],
    "dob": [datetime(1950, 1, 1) + timedelta(days=np.random.randint(0, 25000)) for _ in range(num_customers)],
    "new_column": ["" for _ in range(num_customers)],
    "gender": np.random.choice(["Male", "Female"], num_customers)
})
customers.to_csv("customers.csv", index=False)

# Generate Movies
movies = pd.DataFrame({
    "id": range(1, num_movies + 1),
    "title": [f"Movie {i}" for i in range(1, num_movies + 1)],
    "releasedate": [datetime(2000, 1, 1) + timedelta(days=np.random.randint(0, 7300)) for _ in range(num_movies)],
    "language": np.random.choice(["English", "Spanish", "French", "German"], num_movies),
    "cost": np.random.uniform(50000, 2000000, num_movies).round(2),
    "country": np.random.choice(["USA", "UK", "France", "Germany", "India"], num_movies)
})
movies.to_csv("movies.csv", index=False)

# Generate Directors
directors = pd.DataFrame({
    "id": range(1, num_directors + 1),
    "name": [f"Director {i}" for i in range(1, num_directors + 1)],
    "dob": [datetime(1950, 1, 1) + timedelta(days=np.random.randint(0, 25000)) for _ in range(num_directors)],
    "gender": np.random.choice(["Male", "Female"], num_directors)
})
directors.to_csv("directors.csv", index=False)

# Generate Stars
stars = pd.DataFrame({
    "id": range(1, num_stars + 1),
    "name": [f"Star {i}" for i in range(1, num_stars + 1)],
    "dob": [datetime(1960, 1, 1) + timedelta(days=np.random.randint(0, 25000)) for _ in range(num_stars)],
    "gender": np.random.choice(["Male", "Female"], num_stars)
})
stars.to_csv("stars.csv", index=False)

# Generate Genres
genres = pd.DataFrame({
    "id": range(1, num_genres + 1),
    "genre_name": [f"Genre {i}" for i in range(1, num_genres + 1)]
})
genres.to_csv("genres.csv", index=False)

# Generate Cinemas
cinemas = pd.DataFrame({
    "id": range(1, num_cinemas + 1),
    "address": [f"Address {i}" for i in range(1, num_cinemas + 1)],
    "state": np.random.choice(["Doha", "Alwakra", "Alrayyan", "Alkhore", "Lusail"], num_cinemas)
})
cinemas.to_csv("cinemas.csv", index=False)

# Generate Halls
halls = pd.DataFrame({
    "id": range(1, num_halls + 1),
    "size": np.random.randint(50, 300, num_halls),
    "cinema_id": np.random.randint(1, num_cinemas + 1, num_halls)
})
halls.to_csv("halls.csv", index=False)

# Generate Promotions
promotions = pd.DataFrame({
    "id": range(1, num_promotions + 1),
    "description": [f"Promo {i}" for i in range(1, num_promotions + 1)],
    "discount": np.random.uniform(5, 50, num_promotions).round(2),
    "startdate": [datetime(2014, 1, 1) + timedelta(days=np.random.randint(0, 3650)) for _ in range(num_promotions)],
    "enddate": [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 3650)) for _ in range(num_promotions)]
})
promotions.to_csv("promotions.csv", index=False)

# Generate Showings
showings = pd.DataFrame({
    "id": range(1, num_showings + 1),
    "date": [datetime(2014, 1, 1) + timedelta(days=np.random.randint(0, 3650)) for _ in range(num_showings)],
    "time": [f"{np.random.randint(0, 23)}:{np.random.randint(0, 59)}:{np.random.randint(0, 59)}" for _ in range(num_showings)],
    "movie_id": np.random.randint(1, num_movies + 1, num_showings),
    "hall_id": np.random.randint(1, num_halls + 1, num_showings)
})
showings.to_csv("showings.csv", index=False)

# Generate Transactions
transactions = pd.DataFrame({
    "id": range(1, num_transactions + 1),
    "date": [datetime(2014, 1, 1) + timedelta(days=np.random.randint(0, 3650)) for _ in range(num_transactions)],
    "time": [datetime.now() for _ in range(num_transactions)],
    "paymethod": np.random.choice(["Credit Card", "Cash", "Online Payment"], num_transactions),
    "totalprice": np.random.uniform(5, 50, num_transactions).round(2),
    "customer_id": np.random.randint(1, num_customers + 1, num_transactions),
    "transaction_type": np.random.choice(["Online", "Offline"], num_transactions)
})
transactions.to_csv("transactions.csv", index=False)

# Generate Tickets
tickets = pd.DataFrame({
    "id": range(1, num_tickets + 1),
    "row": np.random.randint(1, 20, num_tickets),
    "seat": np.random.randint(1, 100, num_tickets),
    "price": np.random.uniform(5, 20, num_tickets).round(2),
    "transaction_id": np.random.randint(1, num_transactions + 1, num_tickets),
    "showing_id": np.random.randint(1, num_showings + 1, num_tickets)
})
tickets.to_csv("tickets.csv", index=False)

print("Synthetic data CSV files generated successfully!")
