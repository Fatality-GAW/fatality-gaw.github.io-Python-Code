"""
    Fatality's & ChatGPT's Split Data Into YYYY.MM.csv Files
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

# Define the output folder to work with
output_directory = "./CSVs"

# Check and create or use the output_directory:
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    print("Created ", output_directory, " directory")
else:
    print("Using ", output_directory, " directory")

# 1: Open the GAW_sticky_logs_objects CSV file for reading
with open(GAW_sticky_logs_objects, 'r') as GAW_sticky_logs_objects_file:
    reader = csv.reader(GAW_sticky_logs_objects_file)

    # Initialize variables for keeping track of the current month and year
    current_month = None
    current_year = None

    # Set up an array to hold data for the upcoming loop
    urls = []

    # Loop over the rows in the GAW_sticky_logs_objects CSV file
    for row in reader:
        # Get date (row[0]) & url (row[1]) from the row:
        row_date = datetime.strptime(row[0], '%a %b %d %H:%M:%S GMT %Y')
        row_url = row[1]

        # Get the month and year from the date:
        this_month = f'{row_date.month:02d}'  # prefixes a 0 to single digit month
        this_year = row_date.year

        # If the month or year has changed, deal with it:
        if this_month != current_month or this_year != current_year:
            # If current month/year is not None, process it:
            if current_month is not None and current_year is not None:
                unique_urls_for_this_month = []
                for url in urls:
                    if url not in unique_urls_for_this_month:
                        unique_urls_for_this_month.append(url)

                # Add the current_month's data to the dictionary:
                month_dictionary[f'{current_year}.{current_month}'] = unique_urls_for_this_month

                # Reset the array:
                urls = []

            # Update the current month, year:
            current_month = this_month
            current_year = this_year

        # Add the current row_url to the urls array:
        urls.append(row_url)

    # Get the last array:
    unique_urls_for_this_month = []
    for url in urls:
        if url not in unique_urls_for_this_month:
            unique_urls_for_this_month.append(url)

    # Add the last array to the dictionary:
    month_dictionary[f'{current_year}.{current_month}'] = unique_urls_for_this_month


# 2: Get all the sticky posts from the GAW_sticky_posts_objects
gaw_sticky_posts = []

if os.path.exists(GAW_sticky_posts_objects):
    with open(GAW_sticky_posts_objects, 'r') as GAW_sticky_posts_objects_file:
        reader = csv.reader(GAW_sticky_posts_objects_file)
        for row in reader:
            gaw_sticky_posts.append(row)
    print(f'File \'{GAW_sticky_posts_objects}\' read.')


# 3: Dump each monthly file
for month in month_dictionary:
    if month == 'None.None':
        continue

    # Get the file name to output to:
    file = f'{output_directory}/{month}.csv'

    # Create a set of urls of with this month:
    month_urls = month_dictionary[month]

    with open(file, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for url in month_urls:
            for row in gaw_sticky_posts:
                if row[2] == url:
                    writer.writerow(row)
                    break
        print(f'wrote \'{file}\'')

# 4: Dump a reversed mega csv (everything in 1 csv):
all_unique_gaw_sticky_posts = []

# Iterate through all the months again:
for month in month_dictionary:
    if month == 'None.None':
        continue

    # Create a set of urls of with this month:
    month_urls = month_dictionary[month]

    # Add the row to all_unique_gaw_sticky_posts
    for url in month_urls:
        for row in gaw_sticky_posts:
            if row[2] == url:
                if row not in all_unique_gaw_sticky_posts:
                    all_unique_gaw_sticky_posts.append(row)
                    break

all_unique_gaw_sticky_posts = reversed(all_unique_gaw_sticky_posts)


file = f'{output_directory}/ALL.csv'

with open(file, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    for row in all_unique_gaw_sticky_posts:
        writer.writerow(row)
    print(f'wrote \'{file}\'')
