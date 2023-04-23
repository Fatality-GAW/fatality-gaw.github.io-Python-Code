"""
    Fatality's & ChatGPT's GAW Stickies Reloaded Page Generator
    -----------------------------------------------

    Step 1:  you must have the output from 3_split_data_into_yyyy.mm.csv_files.py

    Step 2: remove any csv files you don't want to generate a page for (usually the current month)

    Step 3: run the script, it will generate the web pages.

"""
import csv
import datetime
import glob
import os
import re

# Define a regular expression pattern to match the filename format
pattern = re.compile(r'^(\d{4}\.\d{2})\.csv$')

# TODO Set up a var for mega-rows for the mega TODO name
all_rows = []



# Loop over all files in the current directory
for filename in os.listdir('./CSVs'):


    count = 0
    last_title = ""
    # Get the current date and time
    now = datetime.datetime.now()
    # Get the month and year as two separate variables
    month = f'{now.month:02d}'
    year = now.year
    # Format the month and year as a string with a leading zero for single digit months
    time = filename.replace('.csv', '')
    page = f'https://GreatAwakening.win'
    title1 = f'GREATAWAKENING.WIN'
    title2 = f'STICKIES RELOADED'
    title3 = f'STICKIES RELOADING..'
    title = f'{time} {title1} {title2}'
    fire = '🔥'
    new = '🆕'
    boom = '💥'
    download = '📥'
    changes = '📃'
    code = '📑'
    reloading = '🔄'
    # Read csv file and extract the columns of interest
    with open(f'./CSVs/{filename}', newline='') as f:
        reader = csv.reader(f)
        data = [[row[1], row[2], row[4], row[6]] for row in reader]


    # Create table rows
    table_rows = []
    row_count = 0
    for index, row in enumerate(data):
        row[1] = f'{page}{row[1]}'
        #skip if there is no title:
        if row[2].strip() == "":
            continue


        row_count = row_count + 1

        # Set alternating row colors
        row_color = "#202020" if row_count % 2 == 0 else "#111111"

        # Check if data value matches regular expression for bubble_bursts' general chat
        chat_regex = r'General Chat for (Mon|Tue|Wed|Thu|Fri|Sat|Sun), (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) \d{1,2}'
        if re.search(chat_regex, row[2]):
            if row[3] == 'bubble_bursts':
                row_color = "#3a252f"

        # Check if data value matches regular expression for ashlanddog's team for unleashed / buzz
        unleashed_regex = r'UNLEASHED...'
        buzz_regex = r'Time For A "Buzz"'
        if re.search(unleashed_regex, row[2]) or re.search(buzz_regex, row[2]):
            if row[3] == 'ashlanddog' or row[3] == 'Taffy333' or row[3] == 'Nurarihyon_no_MAGA':
                row_color = "rgb(43, 43, 70)"

        # Check if data value matches regular expression for Uncle_Fester's sunday funnies
        sunday_regex = r'Sunday Funnies'
        if re.search(sunday_regex, row[2]):
            if row[3] == 'Uncle_Fester':
                row_color = "#303630"

        # Check if data value matches regular expression for WinsAnon's WINS OF THE DAY
        wins_regex = r'Wins of the Day:'
        if re.search(wins_regex, row[2]):
            if row[3] == 'WinsAnon':
                row_color = "rgb(60, 55, 39)"  # Change row color if condition is met

        # Check if data value matches regular expression for Puncake150's EXTRA WINS OF THE DAY
        wins_regex = r'Extra Wins of the Day:'
        if re.search(wins_regex, row[2]):
            if row[3] == 'Puncake150':
                row_color = "rgb(60, 44, 54)"  # Change row color if condition is met

        # Check if data value matches regular expression for high-valyrian's Daily Discussion
        daily_regex = r'Daily Discussion Thread'
        if re.search(daily_regex, row[2]):
            if row[3] == 'high-valyrian':
                row_color = "#4d004d"

        # Check if data value matches regular expression for penisse's hold the line
        hold_regex = f'HOLD THE LINE.'
        if re.search(hold_regex, row[2]):
            if row[3] == 'penisse':
                row_color = "#003333"

        # Check if data value matches regular expression for penisse's 'Q Drops - '
        Qdrops1_regex = f'Q Drop'
        Qdrops2_regex = f'Q Drop'
        if re.search(Qdrops1_regex, row[2]) or re.search(Qdrops2_regex, row[2]):
            if row[3] == 'meteorknife':
                row_color = "rgb(230, 230, 230)"

        # Check if data value matches regular expression for 'New Q'
        Qdrops1_regex = f'New Q'
        if re.search(Qdrops1_regex, row[2]):
            row_color = "rgb(230, 230, 230)"

        # Create table row
        table_row = f'<tr id="{row_count}" style="background-color: {row_color}; border-bottom: 1px solid darkred;" '
        table_row += f'onmouseover="this.style.backgroundColor=\'#253147\'; '
        table_row += f'this.childNodes[0].style.color=\'lightgrey\'; this.childNodes[0].style.textShadow=\'0px 0px 10px black\'; '
        table_row += f'this.childNodes[1].style.color=\'white\'; this.childNodes[1].style.textShadow=\'0px 0px 10px black\'; '
        table_row += f'this.childNodes[2].childNodes[0].style.color=\'#dc4848\'; this.childNodes[2].style.textShadow=\'0px 0px 10px black\'; '
        table_row += f'this.childNodes[1].childNodes[0].style.color=\'#4ca1e0\';" '
        table_row += f'onmouseout="this.style.backgroundColor=\'{row_color}\'; '
        table_row += f'this.childNodes[0].style.color=\'#4d4848\'; this.childNodes[0].style.textShadow=\'none\'; '
        table_row += f'this.childNodes[1].style.color=\'#4d4848\'; this.childNodes[1].style.textShadow=\'none\'; '
        table_row += f'this.childNodes[2].childNodes[0].style.color=\'#4ca1e0\'; this.childNodes[2].style.textShadow=\'none\'; '
        table_row += f'this.childNodes[1].childNodes[0].style.color=\'#346c91\';" '
        table_row += f'onclick="if (event.target.tagName == \'A\') return true; '
        table_row += f'window.open(\'{row[1]}\',\'_blank\',\'noopener noreferrer\');" >'
        table_row += f'<td style="background-color:black;top:0;text-align:right;vertical-align:top;">{row_count}</td>'
        table_row += f'<td style="font-weight:bold;font-size:xx-small;color:#4d4848;padding:1em;text-align:left;vertical-align:top;'
        table_row += f'width:10%;max-width:10%;white-space:nowrap;"><span style="color:#346c91">{row[3]}</span> @<br>{row[0]}</td>'
        table_row += f'<td style="padding:1em;color:#464c8a;padding-left:5%;padding-right:5%;'
        table_row += f'font-family: Arial, sans-serif, Segoe UI Emoji, Noto Color Emoji, Twemoji;">'
        table_row += f'<a href="{row[1]}" target="_blank" style="text-decoration:none;font-weight:bold;color:#4ca1e0;">'
        table_row += f'{row[2]}</a></td>'
        table_row += '</tr>'
        table_rows.append(table_row)
        all_rows.append(table_row)

    # Create the HTML page
    html = f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n'
    html += f'<title>{fire} {title} {fire}</title>\n'
    html += '<style>\nbody {\nbackground-color:black;\ncolor:#4d4848;\nfont-family: Arial, sans-serif, Segoe UI Emoji, '
    html += 'Noto Color Emoji, Twemoji;\nmargin: 0; padding: 0;}\nh1 {\nfont-size: 2.5em; font-weight: normal; color: #464c8a;'
    html += f'\ntext-align: center;text-shadow: 0px 0px 4px #464c8a, 0px 0px 4px #464c8a, 0px 0px 5px #464c8a;\n</style>\n</head>\n<body>\n'
    if filename != sorted(os.listdir('./CSVs'))[0] and filename != sorted(os.listdir('./CSVs'))[-1]:
        html += '<div id="menu-div" style="position: fixed; top: 125px; right: 0%; z-index: 9999;">'
        html += f'<span style="font-size:3em;"><a href="index.html" style="text-decoration:none;color:#346c91;" onmouseover="this.style.color=\'#dc4848\'" onmouseout="this.style.color=\'#346c91\'">☰</a></span></div>\n'
    html += '<div id="left-div" style="position: fixed; top: 50%; left: 0; transform: translateY(-50%); z-index: 9999;">'
    if filename != sorted(os.listdir('./CSVs'))[0]:
        previous_index = sorted(os.listdir('./CSVs')).index(filename) - 1
        lname = sorted(os.listdir('./CSVs'))[previous_index].replace('./CSVs', '').replace('.csv', '')
        leftlink = f'{lname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'<span style="font-size:4em;"><a href="{leftlink}" style="text-decoration:none;color:#346c91;" onmouseover="this.style.color=\'#dc4848\'" onmouseout="this.style.color=\'#346c91\'">◄</a></span></div>\n'
    else:
        html += f'<span style="font-size:4em;"><a href="index.html" style="text-decoration:none;color:#346c91;" onmouseover="this.style.color=\'#dc4848\'" onmouseout="this.style.color=\'#346c91\'">☰</a></span></div>\n'
    html += '<div id="right-div" style="position: fixed; top: 50%; right: 0; transform: translateY(-50%); z-index: 9999;">'
    if filename != sorted(os.listdir('./CSVs'))[-1]:
        next_index = sorted(os.listdir('./CSVs')).index(filename) + 1
        rname = sorted(os.listdir('./CSVs'))[next_index].replace('./CSVs', '').replace('.csv', '')
        rightlink = f'{rname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'<span style="font-size:4em;"><a href="{rightlink}" style="text-decoration:none;color:#346c91;" onmouseover="this.style.color=\'#dc4848\'" onmouseout="this.style.color=\'#346c91\'">►</a></span></div>\n'
    else:
        html += f'<span style="font-size:4em;"><a href="index.html" style="text-decoration:none;color:#346c91;" onmouseover="this.style.color=\'#dc4848\'" onmouseout="this.style.color=\'#346c91\'">☰</a></span></div>\n'
    html += f'<h1><a href="{page}" target="_blank" style="text-decoration:none;color:lightgray;font-weight:bold">{fire} {title} {fire}</a></h1>\n'
    html += '<table style="width: 75%; margin: 0 auto;">\n<tbody>\n'
    html += ''.join(table_rows)
    html += '</tbody>\n</table>\n</body>\n</html>'

    # Write HTML page to file
    title = title.replace(" ", ".")
    path = f'./Pages/{title}.html'
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(html)
        print(f'wrote \'{path}\'')

# get the list of HTML pages
pattern = re.compile(r'^(\d{4}\.\d{2})\.GREATAWAKENING\.WIN\.STICKIES\.RELOADED\.html$')
files = []
for file in os.listdir('./Pages'):
    if pattern.match(file):
        files.append(file)

files = sorted(files, reverse=True)

first_post = True
# update the new index.html
path = './Pages/index.html'
with open(path, mode='w', encoding='utf-8') as f:
    title = f'{fire} {title1} {title2} {fire}'
    html = f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n'
    html += f'<title>{title}</title>\n'
    html += '<style>\nbody {\nbackground-color:black;\ncolor:#4d4848;\nfont-family: Arial, sans-serif, Segoe UI Emoji, '
    html += 'Noto Color Emoji, Twemoji;\nmargin: 0; padding: 0;}\nh1 {\nfont-size: 2.5em; font-weight: normal; color: #464c8a;'
    html += '\ntext-align: center;text-shadow: 0px 0px 4px #464c8a, 0px 0px 4px #464c8a, 0px 0px 5px #464c8a;\n}</style>\n</head>\n<body>\n'
    html += f'<h1><a href="{page}" style="text-decoration:none;color:lightgray;font-weight:bold">{title}</a></h1>\n'
    html += '<div id="right-div" style="position: fixed; top: 25px; right: 2%; z-index: 9999;">'
    html += f'<span style="font-size:3em;"><a href="https://github.com/Fatality-GAW/fatality-gaw.github.io/archive/refs/heads/main.zip" style="text-decoration:none;" onmouseover="this.style.textShadow=\'0px 0px 10px white\';" onmouseout="this.style.textShadow=\'none\'">{download}</a></span></div>\n'
    html += '<div id="right-div" style="position: fixed; top: 125px; right: 2%; z-index: 9999;">'
    html += f'<span style="font-size:3em;"><a href="https://github.com/Fatality-GAW/fatality-gaw.github.io/commits/main" style="text-decoration:none;" onmouseover="this.style.textShadow=\'0px 0px 10px white\';" onmouseout="this.style.textShadow=\'none\'">{changes}</a></span></div>\n'
    html += '<div id="right-div" style="position: fixed; top: 225px; right: 2%; z-index: 9999;">'
    html += f'<span style="font-size:3em;"><a href="https://github.com/Fatality-GAW/fatality-gaw.github.io-Python-Code" style="text-decoration:none;" onmouseover="this.style.textShadow=\'0px 0px 10px white\';" onmouseout="this.style.textShadow=\'none\'">{code}</a></span></div>\n'
    html += '<table style="width: 75%; margin: 0 auto;">\n<tbody>\n'
    for index, file in enumerate(files):
        fileTitle = file.replace('html', '').replace('.', ' ').replace(' ', '.', 1).replace('GREATAWAKENING WIN', title1).strip()
        # Set alternating row colors
        row_color = "#202020" if index % 2 == 0 else "#111111"
        table_row = f'<tr style="background-color: {row_color}; border-bottom: 1px solid darkred; text-align:center;" '
        table_row += f'onmouseover="this.style.backgroundColor=\'#253147\'; this.childNodes[0].childNodes[0].style.color=\'#dc4848\'; this.childNodes[0].childNodes[0].style.textShadow=\'0px 0px 5px black\';" '
        table_row += f'onmouseout="this.style.backgroundColor=\'{row_color}\'; this.childNodes[0].childNodes[0].style.color=\'#4ca1e0\'; this.childNodes[0].childNodes[0].style.textShadow=\'none\';" '
        table_row += f'onclick="window.location.href=\'./{file}\'"; >'
        if first_post:
            if file.startswith(f'{year}.{month}'):
                reloadingTitle = file.replace('html', '').replace('.', ' ').replace(' ', '.', 1).replace('GREATAWAKENING WIN', title1).replace(title2, title3).strip()
                table_row += f'<td style="padding:1em;color:#4ca1e0;font-weight:bold;"><a href="./{file}" target="_self" style="color:inherit;text-decoration:inherit;">{reloading} {fire} {reloadingTitle} {fire} {reloading}</a></td>'
            else:
                table_row += f'<td style="padding:1em;color:#4ca1e0;font-weight:bold;"><a href="./{file}" target="_self" style="color:inherit;text-decoration:inherit;">{boom} {new} {fire} {fileTitle} {fire} {new} {boom}</a></td>'
                first_post = False
        else:
            table_row += f'<td style="padding:1em;color:#4ca1e0;font-weight:bold;"><a href="./{file}" target="_self" style="color:inherit;text-decoration:inherit;">{fire} {fileTitle} {fire}</a></td>'
        table_row += '</tr>'
        html += table_row
    html += '</tbody>\n</table>\n</body>\n</html>'
    f.write(html)
    print(f'wrote \'{path}\'')
