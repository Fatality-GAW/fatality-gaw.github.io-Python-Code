"""
    Fatality's Scrape GAW Sticky Logs Objects
    -----------------------------------------

    Step 1:  find out the last page of stickies:.
            eg: Last one was here: https://greatawakening.win/logs?page=1011&type=sticky'

    Step 2: put the page # in the last_sticky_page_no variable, and run the script to get all the stickies.
            note:   make sure you check the last page afterwards to see if it's last page.  if it's not
                    then change:
                        first_sticky_page_no to last_sticky_page_no
                        last_sticky_page_no to the new last page number

    Step 3: After you have all the stickies, change the variables back to:
                        first_sticky_page_no = 1
                        last_sticky_page_no = 5
            Then you only have to run it once every 125 stickies (you can check more if you want)

    Optional: Delete GAW_sticky_logs_objects file to erase all the data and start scraping a new dataset.
"""
import csv
import os
import requests as requests
from datetime import datetime
from bs4 import BeautifulSoup

first_sticky_Page_no = 1
last_sticky_page_no = 5   # <---------------------------SET THIS TO THE HIGHEST PAGE FIRST RUN, BACK TO 5 for next runs
GAW_sticky_logs_objects = './WorkingCSVs/GAW_sticky_logs_objects.csv'
stickies_time = []

# Check if output file exists and populate stickies_time object if it does
if os.path.exists(GAW_sticky_logs_objects):
    with open(GAW_sticky_logs_objects, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            stickies_time.append([row[0], row[1]]);
    print(f'File \'{GAW_sticky_logs_objects}\' read.')

# Loop through all the pages:
count = first_sticky_Page_no
while count <= last_sticky_page_no:
    print(f'GAW sticky logs page {count}/{last_sticky_page_no}:')
    url = f'https://greatawakening.win/logs?page={count}&type=sticky'

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    log_divs = soup.find_all('div', {'class': 'log'})  # Get all div elements with class="log"

    skipped = 0

    for div in log_divs:

        span_tags = div.find_all('span')
        if span_tags:
            time = span_tags[0].get('title').strip()

        i_tags = div.find_all('i')          # Get all the i tags in this div
        if i_tags:                          # If there are i tags
            last_i_tag = i_tags[-1]         # Get the last i tag
            if last_i_tag.find('a').has_attr('href'):
                href = last_i_tag.find('a').get('href').replace('\r\n', '').replace('\n\r', '').replace('\r', '').replace('\n', '').strip()

        row = [time, href]
        if row not in stickies_time:
            stickies_time.append(row)
            print(f'\tNew Record Added: {time} - {href}')
        else:
            skipped = skipped + 1

    print(f'\t{skipped} skipped.')
    count = count + 1

# Sort the dictionary
sorted_stickies_time = sorted(stickies_time, key=lambda x: datetime.strptime(x[0], '%a %b %d %H:%M:%S %Z %Y'))

# Save stickies_time to output file
with open(GAW_sticky_logs_objects, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in sorted_stickies_time:
        writer.writerow([row[0], row[1]])

print(f'File \'{GAW_sticky_logs_objects}\' written.')
