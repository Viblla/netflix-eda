# Netflix EDA - Exploratory Data Analysis

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.0+-green.svg)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-orange.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A comprehensive Exploratory Data Analysis (EDA) of Netflix titles dataset. This project analyzes Netflix's content library to uncover insights about movie and TV show distributions, release years, and content trends.

## Overview

This EDA project examines Netflix's dataset to answer key questions about:
- Distribution of movies vs TV shows
- Trends in content release years
- Content patterns and statistics
- Visualization of key metrics

## Features

- **Data Processing**: Using Pandas for data manipulation and analysis
- **Statistical Analysis**: Comprehensive data exploration and summary statistics
- **Visualizations**: High-quality plots using Matplotlib and Seaborn
- **Insights**: Actionable findings from Netflix content data
- **Reproducible**: Well-documented code for easy reproduction

## Dataset

The analysis uses the Netflix titles dataset containing information about:
- Movie and TV show titles
- Release years
- Type (Movie/TV Show)
- Genres and descriptions
- Content metadata

## Tech Stack

- **Python**: 3.7+
- **Data Processing**: Pandas
- **Visualization**: Matplotlib, Seaborn
- **Analysis**: NumPy, Scipy

## Installation

### Prerequisites
- Python 3.7+
- pip or conda

### Setup

1. Clone the repository:
```bash
git clone https://github.com/Viblla/netflix-eda.git
cd netflix-eda
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Obtain the Netflix dataset:
   - Download `netflix_titles.csv` from Kaggle or another source
   - Place it in the project root directory

## Usage

Run the analysis script:
```bash
python eda.py
```

This will:
- Load and explore the Netflix dataset
- Generate statistical summaries
- Create visualization plots
- Save visualizations as PNG files

## Visualizations

### Movies vs TV Shows
Analysis of the distribution between movies and TV shows in Netflix's catalog.

![Movies vs TV Shows](movies_vs_tv_shows.png)

### Movie Release Years
Distribution of movie release years showing content trends over time.

![Movie Release Years](movie_release_years.png)

## Key Findings

- Netflix catalog includes both movies and TV shows
- Content spans multiple decades with trends in recent releases
- Significant growth in content availability
- Diverse distribution of content types

## Project Structure

```
netflix-eda/
├── eda.py                      # Main EDA script
├── movies_vs_tv_shows.png      # Visualization: Movies vs TV shows
├── movie_release_years.png     # Visualization: Release year distribution
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── LICENSE                     # MIT License
```

## Requirements

See `requirements.txt` for complete dependencies list. Key packages:
- pandas
- matplotlib
- seaborn
- numpy

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](.github/CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Questions?

Feel free to open an issue or discussion for questions about the analysis.

---

For more Netflix data analysis, checkout similar EDA projects on Kaggle.
