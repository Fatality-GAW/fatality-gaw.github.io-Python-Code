"""
    Fatality's GAW Sticky Scraper
    -----------------------------

    This runs the entire scraping process on a timer.
"""
import os
import subprocess
from datetime import datetime, timedelta
import time
import pytz

RETRY_SECONDS = 3600  # every hour
GAW_sticky_logs_objects = './WorkingCSVs/GAW_sticky_logs_objects.csv'
GAW_sticky_posts_objects = './WorkingCSVs/GAW_sticky_posts_objects.csv'

# Get the file sizes:

sticky_logs_size = 0
if os.path.exists(GAW_sticky_logs_objects):
    sticky_logs_size = os.path.getsize(GAW_sticky_logs_objects)

sticky_posts_size = 0
if os.path.exists(GAW_sticky_posts_objects):
    sticky_posts_size = os.path.getsize(GAW_sticky_posts_objects)


# Scraper loop
while True:
    print(f'SCRAPING STICKY LOGS:')
    subprocess.run(['python3', '1_scrape_gaw_sticky_logs_objects.py'])

    if os.path.exists(GAW_sticky_logs_objects) and sticky_logs_size != os.path.getsize(GAW_sticky_logs_objects):
        print(f'SCRAPING STICKY POSTS:')
        subprocess.run(['python3', '2_scrape_gaw_sticky_post_objects.py'])

    else:
        print('NO NEW STICKIES TO SCRAPE!')

    if os.path.exists(GAW_sticky_posts_objects) and sticky_posts_size != os.path.getsize(GAW_sticky_posts_objects):
        print(f'GENERATING CSV FILES:')
        subprocess.run(['python3', '3_split_data_into_yyyy.mm.csv_files.py'])
        print(f'GENERATING HTML FILES:')
        subprocess.run(['python3', '4_gaw_stickies_reloaded_page_generator.py'])

    retryTime = datetime.now() + timedelta(seconds=RETRY_SECONDS)
    retryTimeGMT = datetime.now(pytz.timezone('GMT')) + timedelta(seconds=RETRY_SECONDS)
    print(f"\nWaiting to run again @\r\n\t[{retryTime}](LOCAL)\r\n\t[{retryTimeGMT}](GMT)\r\n(CTRL+C to quit)")
    try:
        time.sleep(RETRY_SECONDS)
    except:
        print(f"\nTerminated by user")
        exit()

