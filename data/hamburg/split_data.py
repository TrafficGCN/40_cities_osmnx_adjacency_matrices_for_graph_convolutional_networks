import os
import csv

def split_csv(input_filename, output_filename1, output_filename2):
    """
    Split a CSV file into two roughly equal parts by rows.

    Parameters:
        - input_filename: the name of the input CSV file.
        - output_filename1: the name of the first output CSV file.
        - output_filename2: the name of the second output CSV file.
    """
    
    # First, count the number of rows in the input file
    with open(input_filename, 'r') as source:
        reader = csv.reader(source)
        rows = list(reader)
        total_rows = len(rows)
    
    # Now, write the rows to the two output files
    with open(output_filename1, 'w', newline='') as dest1, open(output_filename2, 'w', newline='') as dest2:
        writer1 = csv.writer(dest1)
        writer2 = csv.writer(dest2)
        
        for i, row in enumerate(rows):
            if i < total_rows / 2:
                writer1.writerow(row)
            else:
                writer2.writerow(row)

OS_PATH = os.path.dirname(os.path.realpath('__file__'))

split_csv(OS_PATH + '/data/hamburg/utd19_u_hamburg_speed.csv', OS_PATH +  '/data/hamburg/utd19_u_hamburg_speed_part1.csv', OS_PATH +  '/data/hamburg/utd19_u_hamburg_speed_part2.csv')
split_csv(OS_PATH + '/data/hamburg/utd19_u_hamburg_flow.csv', OS_PATH +  '/data/hamburg/utd19_u_hamburg_flow_part1.csv', OS_PATH +  '/data/hamburg/utd19_u_hamburg_flow_part2.csv')
split_csv(OS_PATH + '/data/hamburg/utd19_u_hamburg_occ.csv', OS_PATH +  '/data/hamburg/utd19_u_hamburg_occ_part1.csv', OS_PATH +  '/data/hamburg/utd19_u_hamburg_occ_part2.csv')