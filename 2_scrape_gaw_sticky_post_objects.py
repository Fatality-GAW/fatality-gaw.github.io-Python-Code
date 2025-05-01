"""
    Fatality's & ChatGPT's Scrape GAW Sticky Posts Objects
    ------------------------------------------------------

    Step 1:  you must have the output from 1_scrape_gaw_sticky_logs_objects.py

    Step 2: run the script, it will fetch all urls of the stickies and put them in the GAW_sticky_post_objects.csv.

    Step 3: run this a few times to make sure that you have all the data, when you do, it will output only this:
        File './WorkingCSVs/GAW_sticky_logs_objects.csv' read.
        File './WorkingCSVs/GAW_sticky_posts_objects.csv' read.
        File './WorkingCSVs/GAW_sticky_posts_objects.csv' written.

    Optional: Delete GAW_sticky_post_objects file to erase all the data and start scraping a new dataset.

    NOTE: If the format of the posts change, this code needs to be re-done.
"""

import csv
import os
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

GAW_sticky_logs_objects = './WorkingCSVs/GAW_sticky_logs_objects.csv'

GAW_sticky_posts_objects = './WorkingCSVs/GAW_sticky_posts_objects.csv'

count = 0
to_get = 0  # 0 to get them all
max_workers = 5
all_posts = 0


def scrape(url):
    global count

    request_url = f'https://greatawakening.win{url}'

    count = count + 1

    print(f'reading {count}/{all_posts}: {request_url}')

    response = requests.get(request_url)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the <div> element with class "container"
    container_div = soup.find('div', class_='container')

    if container_div:
        # Find the <main> element with class "main"
        main_element = container_div.find('main', {'class': 'main'})

        if main_element:
            # Find the <article> element with class "main-content"
            article_element = main_element.find('article', {'class': 'main-content'})

            if article_element:
                # get post id (first) and author (last)
                post_data = article_element.find('div', {'class': 'post'})
                if post_data:
                    author = post_data.get('data-author').replace('\r\n', '').replace('\n\r', ''). \
                        replace('\r', '').replace('\n', '').strip()
                    post_id = post_data.get('data-id').replace('\r\n', '').replace('\n\r', ''). \
                        replace('\r', '').replace('\n', '').strip()

                # GMT Date
                time_element = article_element.find('time', {'class': 'timeago'})
                if time_element:
                    time = time_element.get('title').replace('\r\n', '').replace('\n\r', '').replace('\r', ''). \
                        replace('\n', '').strip()

                # vote #
                vote_data = article_element.find('div', {'class': 'vote'})
                if vote_data:
                    vote = vote_data.text.replace('\r\n', '').replace('\n\r', '').replace('\r', ''). \
                        replace('\n', '').strip()

                # title
                title_data = article_element.find('a', {'class': 'title'})
                if title_data:
                    title = title_data.text.replace('\r\n', ' ').replace('\n\r', ' ').replace('\r', ' '). \
                        replace('\n', ' ').strip()
                    title = title.replace(';', ':')  # Some titles have ';' which breaks the output
                    title_words = title.split()
                    trimmed_title = " ".join(title_words).strip()

                # [title](url)
                gaw_link = f'[{trimmed_title}]({request_url})'

                return [post_id, time, url, vote, trimmed_title, gaw_link, author]
            else:
                print(f'Missing one or more of the required elements @ {request_url}')
        else:
            print(f'Missing <main> element @ {request_url}')
    else:
        print(f'Missing <div> element with class "container" @ {request_url}')


# Get the distinct urls from the GAW_sticky_logs_objects file
distinct_url = []

if os.path.exists(GAW_sticky_logs_objects):
    with open(GAW_sticky_logs_objects, 'r') as csv1:
        reader = csv.reader(csv1)
        for row in reader:
            if row[1] not in distinct_url:
                distinct_url.append(row[1])
    print(f'File \'{GAW_sticky_logs_objects}\' read.')
else:
    print(f'File \'{GAW_sticky_logs_objects}\' not found.')
    exit()

if len(distinct_url) == 0:
    print(f'File \'{GAW_sticky_logs_objects}\' had no distinct urls.')
    exit()

# Check if output file exists and populate gaw_sticky_posts object if it does
gaw_sticky_posts = []
if os.path.exists(GAW_sticky_posts_objects):
    with open(GAW_sticky_posts_objects, 'r') as csv2:
        reader = csv.reader(csv2)
        for row in reader:
            gaw_sticky_posts.append(row)
    print(f'File \'{GAW_sticky_posts_objects}\' read.')

# Remove non-retrieved urls:
for post in gaw_sticky_posts:
    text = post[2]
    if text in distinct_url:  # 2 is url: ([post_id, time, url, vote, title, gaw_link, author])
        distinct_url.remove(text)

if to_get != 0:
    distinct_urls = distinct_url[:to_get]
    all_posts = len(distinct_urls)
else:
    distinct_urls = distinct_url
    all_posts = len(distinct_url)
# Scrape all the pages
with ThreadPoolExecutor(max_workers=max_workers) as executor:
    results = executor.map(scrape, distinct_urls)
    for result in results:
        gaw_sticky_posts.append(result)

# sort the output
# Filter out None values from gaw_sticky_posts and sort the remaining values
sorted_gaw_sticky_posts = sorted([post for post in gaw_sticky_posts if post is not None])

# Save stickies_time to output file
with open(GAW_sticky_posts_objects, 'w', newline='') as f:
    writer = csv.writer(f)
    for row in sorted_gaw_sticky_posts:
        writer.writerow(row)

print(f'File \'{GAW_sticky_posts_objects}\' written.')
