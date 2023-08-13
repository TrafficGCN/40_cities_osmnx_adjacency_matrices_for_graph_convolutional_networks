# Remove sensors that aren't in both the matrix and data. An example with Los Angeles.

import os
import pandas as pd

OS_PATH = os.path.dirname(os.path.realpath('__file__'))


# Load the sensor names in each dataframe, excluding the first one
speed_csv_file = OS_PATH + '/data/losangeles/utd19_u_losangeles_flow.csv'
adjacency_csv_file = OS_PATH + '/adj_matrix/losangeles/los_angeles_adjacency_matrix_transposed_normalized.csv'

# Load the dataframes
speed_df = pd.read_csv(speed_csv_file)
adjacency_df = pd.read_csv(adjacency_csv_file)

# Get sensor names from the column headers
speed_sensors = speed_df.columns.tolist()[1:]  # Exclude the first column
adjacency_sensors = adjacency_df.columns.tolist()[1:]  # Exclude the first column

# Find sensors in speed_df that aren't in adjacency_df
extra_sensors_in_speed = [sensor for sensor in speed_sensors if sensor not in adjacency_sensors]

print("Sensors in speed_df that aren't in adjacency_df:", extra_sensors_in_speed)

# Drop the extra sensors from speed_df
speed_df = speed_df.drop(columns=extra_sensors_in_speed)

# Save the new speed_df to a CSV file
new_speed_csv_file = OS_PATH + '/data/losangeles/new_utd19_u_losangeles_flow.csv'
speed_df.to_csv(new_speed_csv_file, index=False)



import os
import pandas as pd

OS_PATH = os.path.dirname(os.path.realpath('__file__'))

# Load the sensor names in each dataframe, excluding the first one
speed_csv_file = OS_PATH + '/data/losangeles/utd19_u_losangeles_flow.csv'
adjacency_csv_file = OS_PATH + '/adj_matrix/losangeles/los_angeles_adjacency_matrix_transposed_normalized.csv'

# Load the dataframes without making the first column as index
speed_df = pd.read_csv(speed_csv_file, index_col=None)
adjacency_df = pd.read_csv(adjacency_csv_file, index_col=0)

# Get sensor names from the column headers
speed_sensors = speed_df.columns.tolist()[1:]  # Exclude the first column
adjacency_sensors = adjacency_df.columns.tolist()

# Find sensors in adjacency_df that aren't in speed_df
extra_sensors_in_adjacency = [str(sensor) for sensor in adjacency_sensors if str(sensor) not in speed_sensors]

print("Sensors in adjacency_df that aren't in speed_df:", extra_sensors_in_adjacency)

# Drop the extra sensors from adjacency_df (both rows and columns) if they exist
adjacency_df = adjacency_df.drop(columns=extra_sensors_in_adjacency, errors='ignore')
adjacency_df = adjacency_df[adjacency_df.index.astype(str).isin(extra_sensors_in_adjacency) == False]

# Save the new adjacency_df to a CSV file
new_adjacency_csv_file = OS_PATH + '/adj_matrix/losangeles/new_los_angeles_adjacency_matrix_transposed_normalized.csv'

adjacency_df.to_csv(new_adjacency_csv_file)
