import os
import pandas as pd

OS_PATH = os.path.dirname(os.path.realpath('__file__'))

print(OS_PATH)

print("Processing speed...")

# Load your data into a DataFrame
df = pd.read_csv(OS_PATH + '/data/groningen/utd19_u_groningen.csv')

# Convert 'DATETIMESTEP' to datetime format if it's not already
df['DATETIMESTEP'] = pd.to_datetime(df['DATETIMESTEP'])

# We first group the dataframe by 'DATETIMESTEP' and 'detid' and get the speed value
grouped_df = df.groupby(['DATETIMESTEP', 'detid']).apply(lambda x: pd.Series({
    'day': x['day'].values[0],
    'speed': x['speed'].values[0]
})).reset_index()

# We now pivot the DataFrame using 'DATETIMESTEP' as index, 'detid' as columns and 'speed' as values
pivot_df = grouped_df.pivot(index='DATETIMESTEP', columns='detid', values='speed')

# Since 'pivot' removes the 'day' from the DataFrame, we need to include it back
days_df = grouped_df[['DATETIMESTEP', 'day']].drop_duplicates().set_index('DATETIMESTEP')
pivot_df = pd.concat([pivot_df, days_df], axis=1)

# Reordering the columns to have 'day' as the first column
cols = pivot_df.columns.tolist()
cols = cols[-1:] + cols[:-1]
pivot_df = pivot_df[cols]

# Forward and backward fill NaN values
pivot_df.fillna(method='ffill', inplace=True)
pivot_df.fillna(method='bfill', inplace=True)

# Resetting the index of the pivot_df DataFrame
pivot_df.reset_index(inplace=True)

# Sort DataFrame by 'DATETIMESTEP' in ascending order
pivot_df.sort_values(by='DATETIMESTEP', inplace=True)

# Saving the DataFrame to a new CSV file
pivot_df.to_csv(OS_PATH + '/data/groningen/utd19_u_groningen_speed.csv', index=False)


print("Processing flow...")

# Load your data into a DataFrame
df = pd.read_csv(OS_PATH + '/data/groningen/utd19_u_groningen.csv')

# Convert 'DATETIMESTEP' to datetime format if it's not already
df['DATETIMESTEP'] = pd.to_datetime(df['DATETIMESTEP'])

# We first group the dataframe by 'DATETIMESTEP' and 'detid' and get the flow value
grouped_df = df.groupby(['DATETIMESTEP', 'detid']).apply(lambda x: pd.Series({
    'day': x['day'].values[0],
    'flow': x['flow'].values[0]
})).reset_index()

# We now pivot the DataFrame using 'DATETIMESTEP' as index, 'detid' as columns and 'flow' as values
pivot_df = grouped_df.pivot(index='DATETIMESTEP', columns='detid', values='flow')

# Since 'pivot' removes the 'day' from the DataFrame, we need to include it back
days_df = grouped_df[['DATETIMESTEP', 'day']].drop_duplicates().set_index('DATETIMESTEP')
pivot_df = pd.concat([pivot_df, days_df], axis=1)

# Reordering the columns to have 'day' as the first column
cols = pivot_df.columns.tolist()
cols = cols[-1:] + cols[:-1]
pivot_df = pivot_df[cols]

# Forward and backward fill NaN values
pivot_df.fillna(method='ffill', inplace=True)
pivot_df.fillna(method='bfill', inplace=True)

# Resetting the index of the pivot_df DataFrame
pivot_df.reset_index(inplace=True)

# Sort DataFrame by 'DATETIMESTEP' in ascending order
pivot_df.sort_values(by='DATETIMESTEP', inplace=True)

# Saving the DataFrame to a new CSV file
pivot_df.to_csv(OS_PATH + '/data/groningen/utd19_u_groningen_flow.csv', index=False)


print("Processing occ...")

# Load your data into a DataFrame
df = pd.read_csv(OS_PATH + '/data/groningen/utd19_u_groningen.csv')

# Convert 'DATETIMESTEP' to datetime format if it's not already
df['DATETIMESTEP'] = pd.to_datetime(df['DATETIMESTEP'])

# We first group the dataframe by 'DATETIMESTEP' and 'detid' and get the occ value
grouped_df = df.groupby(['DATETIMESTEP', 'detid']).apply(lambda x: pd.Series({
    'day': x['day'].values[0],
    'occ': x['occ'].values[0]
})).reset_index()

# We now pivot the DataFrame using 'DATETIMESTEP' as index, 'detid' as columns and 'occ' as values
pivot_df = grouped_df.pivot(index='DATETIMESTEP', columns='detid', values='occ')

# Since 'pivot' removes the 'day' from the DataFrame, we need to include it back
days_df = grouped_df[['DATETIMESTEP', 'day']].drop_duplicates().set_index('DATETIMESTEP')
pivot_df = pd.concat([pivot_df, days_df], axis=1)

# Reordering the columns to have 'day' as the first column
cols = pivot_df.columns.tolist()
cols = cols[-1:] + cols[:-1]
pivot_df = pivot_df[cols]

# Forward and backward fill NaN values
pivot_df.fillna(method='ffill', inplace=True)
pivot_df.fillna(method='bfill', inplace=True)

# Resetting the index of the pivot_df DataFrame
pivot_df.reset_index(inplace=True)

# Sort DataFrame by 'DATETIMESTEP' in ascending order
pivot_df.sort_values(by='DATETIMESTEP', inplace=True)

# Saving the DataFrame to a new CSV file
pivot_df.to_csv(OS_PATH + '/data/groningen/utd19_u_groningen_occ.csv', index=False)