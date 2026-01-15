import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample Netflix dataset
n_records = 5000

# Sample data
types = ['Movie', 'TV Show']
countries_list = ['United States', 'India', 'United Kingdom', 'Canada', 'Japan', 'Mexico', 'South Korea', 'Australia', 'France', 'Germany', 'Spain', 'Brazil', 'Italy', 'Netherlands', 'Turkey']
genres_list = ['Drama', 'Comedy', 'Action', 'Thriller', 'Romance', 'Horror', 'Documentary', 'Animation', 'Adventure', 'Crime', 'Fantasy', 'Sci-Fi']
ratings_list = ['G', 'PG', 'PG-13', 'R', 'NC-17', 'TV-Y', 'TV-Y7', 'TV-G', 'TV-PG', 'TV-14', 'TV-MA']

# Create DataFrame
df = pd.DataFrame({
    'show_id': [f's{i}' for i in range(n_records)],
    'type': np.random.choice(types, n_records, p=[0.65, 0.35]),
    'title': [f'Title {i}' for i in range(n_records)],
    'director': [f'Director {np.random.randint(0, 200)}' for _ in range(n_records)],
    'cast': [f'Actor {np.random.randint(0, 500)}' for _ in range(n_records)],
    'country': [', '.join(np.random.choice(countries_list, np.random.randint(1, 4), replace=False)) for _ in range(n_records)],
    'date_added': [(datetime.now() - timedelta(days=np.random.randint(0, 3000))).strftime('%B %d, %Y') for _ in range(n_records)],
    'release_year': np.random.randint(1990, 2024, n_records),
    'rating': np.random.choice(ratings_list, n_records),
    'duration': [f'{np.random.randint(40, 180)} min' if np.random.choice(types) == 'Movie' else f'{np.random.randint(1, 15)} Seasons' for _ in range(n_records)],
    'listed_in': [', '.join(np.random.choice(genres_list, np.random.randint(1, 4), replace=False)) for _ in range(n_records)],
    'description': [f'Description for title {i}' for i in range(n_records)]
})

# Save to CSV
df.to_csv('netflix_titles.csv', index=False)
print(f"✓ Generated {n_records} sample records in netflix_titles.csv")
print(f"✓ Shape: {df.shape}")
print(f"✓ Columns: {list(df.columns)}")
