import os
import urllib.request

# Download the Netflix dataset
url = 'https://raw.githubusercontent.com/amankharwal/Netflix-Dataset-Analysis/main/netflix_titles.csv'
filename = 'netflix_titles.csv'

if not os.path.exists(filename):
    print("Downloading Netflix dataset...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"✓ Downloaded {filename}")
    except Exception as e:
        print(f"✗ Failed to download: {e}")
else:
    print(f"✓ {filename} already exists")
