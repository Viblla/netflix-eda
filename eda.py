import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Netflix colors
netflix_red = '#e50914'
netflix_dark = '#221f1f'
netflix_light = '#f5f5f1'

# Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')

print("=" * 60)
print("NETFLIX DATASET EXPLORATORY DATA ANALYSIS")
print("=" * 60)
print(f"\nDataset Shape: {df.shape}")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nData Info:\n{df.info()}")
print(f"\nFirst Few Rows:\n{df.head()}")

# ============================================
# 1. MOVIES vs TV SHOWS - IMPROVED
# ============================================
plt.figure(figsize=(12, 7))
type_counts = df['type'].value_counts()
colors = [netflix_red, '#FFB000']
plt.bar(type_counts.index, type_counts.values, color=colors, edgecolor='black', linewidth=2, width=0.6)
plt.title('Distribution of Movies vs TV Shows', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Content Type', fontsize=14, fontweight='bold')
plt.ylabel('Count', fontsize=14, fontweight='bold')
plt.ylim(0, max(type_counts.values) * 1.1)

# Add value labels on bars
for i, v in enumerate(type_counts.values):
    plt.text(i, v + 50, str(v), ha='center', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('movies_vs_tv_shows.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("\n✓ Saved: movies_vs_tv_shows.png")

# ============================================
# 2. RELEASE YEAR DISTRIBUTION - IMPROVED
# ============================================
plt.figure(figsize=(14, 7))
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
release_counts = df['release_year'].dropna().astype(int).value_counts().sort_index()
plt.bar(release_counts.index, release_counts.values, color=netflix_red, alpha=0.85, edgecolor='black', linewidth=1)
plt.title('Movie Release Years Distribution', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Release Year', fontsize=14, fontweight='bold')
plt.ylabel('Count', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('movie_release_years.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: movie_release_years.png")

# ============================================
# 3. TOP GENRES
# ============================================
plt.figure(figsize=(14, 8))
# Split genres and flatten
genres_list = df['listed_in'].dropna().str.split(', ').explode().value_counts().head(12)
colors_gradient = plt.cm.RdYlGn_r(np.linspace(0.3, 0.7, len(genres_list)))
bars = plt.barh(range(len(genres_list)), genres_list.values, color=netflix_red, alpha=0.85, edgecolor='black', linewidth=1)
plt.yticks(range(len(genres_list)), genres_list.index, fontsize=11)
plt.title('Top 12 Genres on Netflix', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Count', fontsize=14, fontweight='bold')

# Add value labels
for i, v in enumerate(genres_list.values):
    plt.text(v + 10, i, str(v), va='center', fontsize=10, fontweight='bold')

plt.grid(axis='x', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('top_genres.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: top_genres.png")

# ============================================
# 4. CONTENT BY COUNTRY
# ============================================
plt.figure(figsize=(14, 8))
# Get country counts (first country listed)
countries_list = df['country'].dropna().str.split(', ').str[0].value_counts().head(12)
bars = plt.barh(range(len(countries_list)), countries_list.values, color='#FFB000', alpha=0.85, edgecolor='black', linewidth=1)
plt.yticks(range(len(countries_list)), countries_list.index, fontsize=11)
plt.title('Top 12 Countries Producing Netflix Content', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Count', fontsize=14, fontweight='bold')

# Add value labels
for i, v in enumerate(countries_list.values):
    plt.text(v + 5, i, str(v), va='center', fontsize=10, fontweight='bold')

plt.grid(axis='x', alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig('top_countries.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: top_countries.png")

# ============================================
# 5. RATINGS DISTRIBUTION
# ============================================
plt.figure(figsize=(14, 7))
if 'rating' in df.columns:
    ratings_count = df['rating'].value_counts().sort_values(ascending=False).head(10)
    colors_ratings = [netflix_red if i % 2 == 0 else '#FFB000' for i in range(len(ratings_count))]
    plt.bar(ratings_count.index, ratings_count.values, color=colors_ratings, edgecolor='black', linewidth=1.5)
    plt.title('Top 10 Content Ratings on Netflix', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Rating', fontsize=14, fontweight='bold')
    plt.ylabel('Count', fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, fontsize=11)
    
    # Add value labels
    for i, v in enumerate(ratings_count.values):
        plt.text(i, v + 20, str(v), ha='center', fontsize=10, fontweight='bold')
    
    plt.grid(axis='y', alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('content_ratings.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
    plt.close()
    print("✓ Saved: content_ratings.png")

# ============================================
# 6. CONTENT DURATION ANALYSIS
# ============================================
if 'duration' in df.columns:
    plt.figure(figsize=(14, 7))
    
    # Separate movies and TV shows
    movies = df[df['type'] == 'Movie']['duration'].dropna()
    tv_shows = df[df['type'] == 'TV Show']['duration'].dropna()
    
    # Extract numeric values
    movies_duration = movies.str.extract('(\d+)')[0].astype(int)
    tv_duration = tv_shows.str.extract('(\d+)')[0].astype(int)
    
    plt.subplot(1, 2, 1)
    plt.hist(movies_duration, bins=30, color=netflix_red, alpha=0.85, edgecolor='black')
    plt.title('Movie Duration Distribution', fontsize=14, fontweight='bold')
    plt.xlabel('Duration (minutes)', fontsize=12, fontweight='bold')
    plt.ylabel('Count', fontsize=12, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    plt.subplot(1, 2, 2)
    plt.hist(tv_duration, bins=30, color='#FFB000', alpha=0.85, edgecolor='black')
    plt.title('TV Show Duration Distribution', fontsize=14, fontweight='bold')
    plt.xlabel('Duration (seasons)', fontsize=12, fontweight='bold')
    plt.ylabel('Count', fontsize=12, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    plt.suptitle('Content Duration Analysis', fontsize=16, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('content_duration.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
    plt.close()
    print("✓ Saved: content_duration.png")

# ============================================
# 7. CONTENT ADDED OVER TIME
# ============================================
if 'date_added' in df.columns:
    plt.figure(figsize=(14, 7))
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    
    content_by_year = df['year_added'].value_counts().sort_index()
    plt.plot(content_by_year.index, content_by_year.values, color=netflix_red, linewidth=3, marker='o', markersize=8)
    plt.fill_between(content_by_year.index, content_by_year.values, alpha=0.3, color=netflix_red)
    
    plt.title('Netflix Content Added Over Years', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Year Added', fontsize=14, fontweight='bold')
    plt.ylabel('Number of Titles Added', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.tight_layout()
    plt.savefig('content_added_timeline.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
    plt.close()
    print("✓ Saved: content_added_timeline.png")

print("\n" + "=" * 60)
print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
print("=" * 60)
