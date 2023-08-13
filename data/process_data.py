import os
import pandas as pd

# Get the directory where the current script is located
OS_PATH = os.path.dirname(os.path.realpath(__file__))

print(f"Current directory: {OS_PATH}")

# Form the path for utd19_u.csv
csv_path = os.path.join(OS_PATH, 'utd19_u.csv')

# Read the CSV
print("Loading Data...")
data = pd.read_csv(csv_path, low_memory=False)

# Convert the 'day' column to datetime format
data['day'] = pd.to_datetime(data['day'])

# Convert the 'interval' column (which seems to be in seconds) to timedelta format
data['interval'] = pd.to_timedelta(data['interval'], unit='s')

# Combine the 'day' and 'interval' columns to create a new 'DATETIMESTEP' column
data['DATETIMESTEP'] = data['day'] + data['interval']

print(data)

# Group by city
print("Grouping Data...")
grouped = data.groupby('city')

# Save each city's data as a separate CSV in its respective folder within the 'data' directory
for city, group in grouped:
    print(f"Processing {city}...")
    city_dir = os.path.join(OS_PATH, city)
    
    # Ensure directory exists
    if not os.path.exists(city_dir):
        os.makedirs(city_dir)
    
    # Modified filename format
    output_path = os.path.join(city_dir, f'utd19_u_{city}.csv')
    group.to_csv(output_path, index=False)

print("CSV files saved by city in respective folders within the 'data' directory!")
