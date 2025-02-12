import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')

# Basic data info
print(df.info())

# Example: Distribution of movie release years
plt.figure(figsize=(10, 6))
sns.histplot(df['release_year'], bins=30, kde=True)
plt.title('Distribution of Movie Release Years')

# Save the plot as a .png image
plt.savefig('movie_release_years.png')
plt.show()

# Example: Count of Movies and TV Shows
plt.figure(figsize=(8, 6))
sns.countplot(x='type', data=df)
plt.title('Count of Movies vs TV Shows')

# Save the plot as a .png image
plt.savefig('movies_vs_tv_shows.png')
plt.show()
