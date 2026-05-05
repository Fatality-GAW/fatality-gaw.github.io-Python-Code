"""
    Fatality's & ChatGPT's Scrape GAW Sticky Logs Objects
    -----------------------------------------

    Step 1:  find out the last page of stickies:.
            eg: Last one was here: https://greatawakening.win/logs?page=1012&type=sticky'

    Step 2: put the page # in the last_sticky_page_no variable, and run the script to get all the stickies.
            note:   make sure you check the last page afterwards to see if it's last page.  if it's not
                    then change:
                        first_sticky_page_no to last_sticky_page_no
                        last_sticky_page_no to the new last page number
                    and run it again.

    Step 3: After you have all the stickies, change the variables back to:
                        first_sticky_page_no = 1
                        last_sticky_page_no = 5
            Then you only have to run it once every 125 stickies (you can check more if you want)

    Optional: Delete GAW_sticky_logs_objects file to erase all the data and start scraping a new dataset.

    NOTE: If the format of the posts change, this code needs to be re-done.
"""
import csv
import os
import requests as requests
from datetime import datetime
from bs4 import BeautifulSoup
import threading
import queue

NUM_THREADS = 50
CHECK_RESULTS_INTERVAL = 0.1
first_sticky_page_no = 1
last_sticky_page_no = 100  # <---------------------------SET THIS TO THE HIGHEST PAGE FIRST RUN, BACK TO 5 for next runs
GAW_sticky_logs_objects = './WorkingCSVs/GAW_sticky_logs_objects.csv'
stickies_time = []

# Check if output file exists and populate stickies_time object if it does
if os.path.exists(GAW_sticky_logs_objects):
    with open(GAW_sticky_logs_objects, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            stickies_time.append([row[0], row[1]])
    print(f'File \'{GAW_sticky_logs_objects}\' read.')


# Define a function that will retrieve the logs for a single page
def get_logs(url, stickies_time, page_no, last_page_no):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    log_divs = soup.find_all('div', {'class': 'log'})  # Get all div elements with class="log"

    skipped = 0

    new_records = ""

    for div in log_divs:
        span_tags = div.find_all('span')
        if span_tags:
            time = span_tags[0].get('title').strip()

        i_tags = div.find_all('i')  # Get all the <I> tags in this div
        if i_tags:  # If there are <I> tags
            last_i_tag = i_tags[-1]  # Get the last <I>> tag
            if last_i_tag.find('a').has_attr('href'):
                href = last_i_tag.find('a').get('href').replace('\r\n', '').replace('\n\r', '').replace('\r',
                                                                                                        '').replace(
                    '\n', '').strip()

        row = [time, href]
        if row not in stickies_time:
            stickies_time.append(row)
            new_records += f'\t\t{time} - {href}\n'
        else:
            skipped = skipped + 1
    output = f'{page_no}/{last_sticky_page_no} @ {url}\n'
    if new_records != "":
        output += f'\tAdded Records:\n{new_records}'
    if skipped != 0:
        output += f'\tSkipped Records:\n\t\t{skipped} were already retrieved\n'
    print(output)


# Define a function that will retrieve the logs for multiple pages
def get_logs_for_range(first_sticky_page_no, last_sticky_page_no, stickies_time, results_queue):
    for page_no in range(first_sticky_page_no, last_sticky_page_no + 1):
        url = f'https://greatawakening.win/logs?page={page_no}&type=sticky'
        get_logs(url, stickies_time, page_no, last_sticky_page_no)


# Create a queue for the results
results_queue = queue.Queue()

# Create a list to hold the thread objects
thread_list = []

# Loop through all the page ranges
for i in range(0, (last_sticky_page_no - first_sticky_page_no + NUM_THREADS - 1) // NUM_THREADS):
    # Calculate the page range for this batch of threads
    start_page_no = first_sticky_page_no + NUM_THREADS * i
    end_page_no = min(first_sticky_page_no + NUM_THREADS * (i + 1) - 1, last_sticky_page_no)

    # Create a new thread to retrieve the logs for this range of pages
    t = threading.Thread(target=get_logs_for_range, args=(start_page_no, end_page_no, stickies_time, results_queue))
    thread_list.append(t)
    t.start()

# Wait for all the threads to finish
for t in thread_list:
    t.join()

# Check the results queue until all the threads have finished
while not results_queue.empty():
    print(results_queue.get())

# Sort the dictionary
sorted_stickies_time = sorted(stickies_time, key=lambda x: datetime.strptime(x[0], '%a %b %d %H:%M:%S %Z %Y'))

# Save stickies_time to output file
with open(GAW_sticky_logs_objects, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in sorted_stickies_time:
        writer.writerow([row[0], row[1]])

print(f'File \'{GAW_sticky_logs_objects}\' written.')
