"""
    Fatality's GAW Sticky Scraper
    -----------------------------

    This runs the entire scraping process on a timer.
"""
import subprocess
from datetime import datetime, timedelta
import time

RETRY_SECONDS = 3600  # every hour


while True:

    print(f'SCRAPING STICKY LOGS:')
    subprocess.run(['python', '1_scrape_gaw_sticky_logs_objects.py'])
    print(f'SCRAPING STICKY POSTS:')
    subprocess.run(['python', '2_scrape_gaw_sticky_post_objects.py'])
    print(f'GENERATING MONTHLY CSV FILES:')
    subprocess.run(['python', '3_split_data_into_yyyy.mm.csv_files.py'])
    print(f'GENERATING STICKIES RELOADED HTML FILES:')
    subprocess.run(['python', '4_gaw_stickies_reloaded_page_generator.py'])

    retryTime = datetime.now() + timedelta(seconds=RETRY_SECONDS)
    print(f"\nWaiting to run again @ [{retryTime}]\r\n(CTRL+C to quit)")
    try:
        time.sleep(RETRY_SECONDS)
    except:
        print("")
        exit()

