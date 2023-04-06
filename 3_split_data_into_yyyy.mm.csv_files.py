"""
    Fatality's Split Data Into YYYY.MM.csv Files
    --------------------------------------------

    Step 1:  you must have the output from 1_scrape_gaw_sticky_logs_objects.py and 2_scrape_gaw_sticky_post_objects.py

    Step 2: run the script, it will generate csv files for the page generation.
"""
import csv
import os
from datetime import datetime


month_dictionary = {}

GAW_sticky_logs_objects = './WorkingCSVs/GAW_sticky_logs_objects.csv'

GAW_sticky_posts_objects = './WorkingCSVs/GAW_sticky_posts_objects.csv'

# Open the input CSV file for reading
with open(GAW_sticky_logs_objects, 'r') as f:
    reader = csv.reader(f)

    # Initialize variables for keeping track of the current month and year
    current_month = None
    current_year = None

    urls =[]

    # Loop over the rows in the input CSV file
    for row in reader:
        # Parse the date from the first column of the row
        url = row[1]
        date_string = row[0]
        date = datetime.strptime(date_string, '%a %b %d %H:%M:%S GMT %Y')

        # Get the month and year from the date
        month = f'{date.month:02d}'
        year = date.year

        # If this is a new month or year, create a new output file for it
        if month != current_month or year != current_year:
            unique_urls = []
            for url in urls:
               if url not in unique_urls:
                   unique_urls.append(url)

            month_dictionary[f'{current_year}.{current_month}'] = unique_urls

            urls = []
            # Update the current month, year, and output file
            current_month = month
            current_year = year

        # Write the current row to the current output file
        urls.append(url)

    # add the last dictionar:
    unique_urls = []
    for url in urls:
        if url not in unique_urls:
            unique_urls.append(url)

    month_dictionary[f'{current_year}.{current_month}'] = unique_urls

gaw_sticky_posts = []
if os.path.exists(GAW_sticky_posts_objects):
    with open(GAW_sticky_posts_objects, 'r') as csv2:
        reader = csv.reader(csv2)
        for row in reader:
            gaw_sticky_posts.append(row)
    print(f'File \'{GAW_sticky_posts_objects}\' read.')

for month in month_dictionary:
    if month == 'None.None':
        continue
    file = f'./CSVs/{month}.csv'
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        print(f'writing {file}')
        for url in month_dictionary[month]:
            for row in gaw_sticky_posts:
                if url == row[2]:
                    writer.writerow(row)
