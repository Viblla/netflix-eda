import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Netflix Color Scheme
netflix_red = '#e50914'
netflix_dark = '#221f1f'
netflix_light = '#f5f5f1'
netflix_gold = '#FFB000'

print("=" * 60)
print("NETFLIX DATASET EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# Load dataset
df = pd.read_csv('netflix_titles.csv')

print(f"\nDataset Shape: {df.shape}\n")
print("Column Names:")
print(df.columns.tolist())
print("\nData Info:")
print(df.info())
print("\nFirst Few Rows:")
print(df.head())

# ============================================================
# VISUALIZATION 1: Movies vs TV Shows
# ============================================================
plt.figure(figsize=(12, 7), dpi=300, facecolor=netflix_light)
ax = plt.gca()
ax.set_facecolor(netflix_light)

content_counts = df['type'].value_counts()
bars = ax.bar(content_counts.index, content_counts.values, 
              color=[netflix_red, netflix_gold], width=0.6, edgecolor=netflix_dark, linewidth=2)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=18, fontweight='bold', color=netflix_dark)

ax.set_title('Count of Movies vs TV Shows', fontsize=20, fontweight='bold', 
             pad=20, color=netflix_dark, fontfamily='sans-serif')
ax.set_ylabel('Count', fontsize=16, fontweight='bold', color=netflix_dark)
ax.set_xlabel('Type', fontsize=16, fontweight='bold', color=netflix_dark)
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax.set_axisbelow(True)

# Style improvements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(netflix_dark)
ax.spines['bottom'].set_color(netflix_dark)
ax.tick_params(labelsize=14, colors=netflix_dark, length=6, width=2)

plt.tight_layout()
plt.savefig('movies_vs_tv_shows.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: movies_vs_tv_shows.png")

# ============================================================
# VISUALIZATION 2: Release Year Distribution
# ============================================================
plt.figure(figsize=(14, 7), dpi=300, facecolor=netflix_light)
ax = plt.gca()
ax.set_facecolor(netflix_light)

release_years = df['release_year'].value_counts().sort_index()
bars = ax.bar(release_years.index, release_years.values, 
              color=netflix_red, width=0.8, edgecolor=netflix_dark, linewidth=1, alpha=0.9)

# Highlight the highest bar
max_idx = release_years.values.argmax()
bars[max_idx].set_color(netflix_gold)
bars[max_idx].set_edgecolor(netflix_dark)
bars[max_idx].set_linewidth(2)

ax.set_title('Distribution of Movie Release Years', fontsize=20, fontweight='bold', 
             pad=20, color=netflix_dark, fontfamily='sans-serif')
ax.set_ylabel('Count', fontsize=16, fontweight='bold', color=netflix_dark)
ax.set_xlabel('Release Year', fontsize=16, fontweight='bold', color=netflix_dark)
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax.set_axisbelow(True)

# Style improvements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(netflix_dark)
ax.spines['bottom'].set_color(netflix_dark)
ax.tick_params(labelsize=12, colors=netflix_dark, length=6, width=2)

plt.tight_layout()
plt.savefig('movie_release_years.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: movie_release_years.png")

# ============================================================
# VISUALIZATION 3: Top 12 Genres
# ============================================================
plt.figure(figsize=(14, 8), dpi=300, facecolor=netflix_light)
ax = plt.gca()
ax.set_facecolor(netflix_light)

# Extract and count genres
genres = df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(12)
colors = [netflix_gold if i == 0 else netflix_red for i in range(len(genres))]

bars = ax.barh(range(len(genres)), genres.values, color=colors, edgecolor=netflix_dark, linewidth=1.5)

# Add value labels
for i, (bar, value) in enumerate(zip(bars, genres.values)):
    ax.text(value, i, f'  {int(value):,}', va='center', fontsize=13, fontweight='bold', color=netflix_dark)

ax.set_yticks(range(len(genres)))
ax.set_yticklabels(genres.index, fontsize=13, fontweight='bold', color=netflix_dark)
ax.set_title('Top 12 Genres on Netflix', fontsize=20, fontweight='bold', 
             pad=20, color=netflix_dark, fontfamily='sans-serif')
ax.set_xlabel('Count', fontsize=16, fontweight='bold', color=netflix_dark)
ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax.set_axisbelow(True)

# Style improvements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(netflix_dark)
ax.spines['bottom'].set_color(netflix_dark)
ax.tick_params(labelsize=12, colors=netflix_dark, length=6, width=2)

plt.tight_layout()
plt.savefig('top_genres.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: top_genres.png")

# ============================================================
# VISUALIZATION 4: Top 12 Countries
# ============================================================
plt.figure(figsize=(14, 8), dpi=300, facecolor=netflix_light)
ax = plt.gca()
ax.set_facecolor(netflix_light)

# Extract and count countries
countries = df['country'].str.split(', ', expand=True).stack().value_counts().head(12)
colors = [netflix_gold if i == 0 else netflix_red for i in range(len(countries))]

bars = ax.barh(range(len(countries)), countries.values, color=colors, edgecolor=netflix_dark, linewidth=1.5)

# Add value labels
for i, (bar, value) in enumerate(zip(bars, countries.values)):
    ax.text(value, i, f'  {int(value):,}', va='center', fontsize=13, fontweight='bold', color=netflix_dark)

ax.set_yticks(range(len(countries)))
ax.set_yticklabels(countries.index, fontsize=13, fontweight='bold', color=netflix_dark)
ax.set_title('Top 12 Countries Producing Content', fontsize=20, fontweight='bold', 
             pad=20, color=netflix_dark, fontfamily='sans-serif')
ax.set_xlabel('Count', fontsize=16, fontweight='bold', color=netflix_dark)
ax.grid(axis='x', alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax.set_axisbelow(True)

# Style improvements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(netflix_dark)
ax.spines['bottom'].set_color(netflix_dark)
ax.tick_params(labelsize=12, colors=netflix_dark, length=6, width=2)

plt.tight_layout()
plt.savefig('top_countries.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: top_countries.png")

# ============================================================
# VISUALIZATION 5: Content Ratings Distribution
# ============================================================
plt.figure(figsize=(14, 7), dpi=300, facecolor=netflix_light)
ax = plt.gca()
ax.set_facecolor(netflix_light)

ratings = df['rating'].value_counts().head(10)
colors = [netflix_gold if i % 2 == 0 else netflix_red for i in range(len(ratings))]

bars = ax.bar(range(len(ratings)), ratings.values, color=colors, edgecolor=netflix_dark, linewidth=1.5)

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}',
            ha='center', va='bottom', fontsize=13, fontweight='bold', color=netflix_dark)

ax.set_xticks(range(len(ratings)))
ax.set_xticklabels(ratings.index, fontsize=13, fontweight='bold', color=netflix_dark, rotation=45, ha='right')
ax.set_title('Top 10 Content Ratings', fontsize=20, fontweight='bold', 
             pad=20, color=netflix_dark, fontfamily='sans-serif')
ax.set_ylabel('Count', fontsize=16, fontweight='bold', color=netflix_dark)
ax.set_xlabel('Rating', fontsize=16, fontweight='bold', color=netflix_dark)
ax.grid(axis='y', alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax.set_axisbelow(True)

# Style improvements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(netflix_dark)
ax.spines['bottom'].set_color(netflix_dark)
ax.tick_params(labelsize=12, colors=netflix_dark, length=6, width=2)

plt.tight_layout()
plt.savefig('content_ratings.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: content_ratings.png")

# ============================================================
# VISUALIZATION 6: Content Duration Analysis
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), dpi=300, facecolor=netflix_light)
fig.patch.set_facecolor(netflix_light)

# Movies duration
movies = df[df['type'] == 'Movie']['duration']
movies_duration = movies.str.extract(r'(\d+)', expand=False).astype(float)

ax1.hist(movies_duration, bins=40, color=netflix_red, edgecolor=netflix_dark, 
         linewidth=1.2, alpha=0.9, facecolor=netflix_light)
ax1.set_facecolor(netflix_light)
ax1.set_title('Movie Duration (Minutes)', fontsize=16, fontweight='bold', 
              color=netflix_dark, pad=15, fontfamily='sans-serif')
ax1.set_xlabel('Duration (mins)', fontsize=13, fontweight='bold', color=netflix_dark)
ax1.set_ylabel('Count', fontsize=13, fontweight='bold', color=netflix_dark)
ax1.grid(axis='y', alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.tick_params(labelsize=11, colors=netflix_dark, length=6, width=1.5)

# TV Shows duration
tv_shows = df[df['type'] == 'TV Show']['duration']
tv_duration = tv_shows.str.extract(r'(\d+)', expand=False).astype(float)

ax2.hist(tv_duration, bins=20, color=netflix_gold, edgecolor=netflix_dark, 
         linewidth=1.2, alpha=0.9, facecolor=netflix_light)
ax2.set_facecolor(netflix_light)
ax2.set_title('TV Show Duration (Seasons)', fontsize=16, fontweight='bold', 
              color=netflix_dark, pad=15, fontfamily='sans-serif')
ax2.set_xlabel('Duration (seasons)', fontsize=13, fontweight='bold', color=netflix_dark)
ax2.set_ylabel('Count', fontsize=13, fontweight='bold', color=netflix_dark)
ax2.grid(axis='y', alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.tick_params(labelsize=11, colors=netflix_dark, length=6, width=1.5)

fig.suptitle('Content Duration Comparison', fontsize=18, fontweight='bold', 
             color=netflix_dark, y=1.02, fontfamily='sans-serif')
plt.tight_layout()
plt.savefig('content_duration.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: content_duration.png")

# ============================================================
# VISUALIZATION 7: Content Added Over Time
# ============================================================
plt.figure(figsize=(14, 7), dpi=300, facecolor=netflix_light)
ax = plt.gca()
ax.set_facecolor(netflix_light)

# Parse date and create timeline
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
timeline = df.dropna(subset=['date_added']).resample('M', on='date_added').size()

ax.plot(timeline.index, timeline.values, color=netflix_red, linewidth=3, label='Monthly Added')
ax.fill_between(timeline.index, timeline.values, alpha=0.3, color=netflix_red)

ax.set_title('Content Added Over Time', fontsize=20, fontweight='bold', 
             pad=20, color=netflix_dark, fontfamily='sans-serif')
ax.set_ylabel('Number of Titles', fontsize=16, fontweight='bold', color=netflix_dark)
ax.set_xlabel('Date', fontsize=16, fontweight='bold', color=netflix_dark)
ax.grid(True, alpha=0.3, linestyle='--', linewidth=1, color=netflix_dark)
ax.set_axisbelow(True)

# Style improvements
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(netflix_dark)
ax.spines['bottom'].set_color(netflix_dark)
ax.tick_params(labelsize=12, colors=netflix_dark, length=6, width=2)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('content_added_timeline.png', dpi=300, bbox_inches='tight', facecolor=netflix_light)
plt.close()
print("✓ Saved: content_added_timeline.png")

print("\n" + "=" * 60)
print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
print("=" * 60)
