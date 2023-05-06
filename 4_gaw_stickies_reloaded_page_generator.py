"""
    Fatality's & ChatGPT's GAW Stickies Reloaded Page Generator
    -----------------------------------------------

    Step 1:  you must have the output from 3_split_data_into_yyyy.mm.csv_files.py

    Step 2: remove any csv files you don't want to generate a page for (usually the current month)

    Step 3: run the script, it will generate the web pages.

"""
import csv
import datetime
import os
import re
import pytz as pytz

# Define a regular expression pattern to match the filename format
pattern = re.compile(r'^(\d{4}\.\d{2})\.csv$')

# Loop over all files in the current directory
for filename in os.listdir('./CSVs'):

    all_stickies_file = "ALL"  # ALL.CSV's name "ALL" is defined in section 4: of 3_split_data_into_yyyy.mm.csv_files.py
    count = 0
    # Get the current date and time in GMT (because that's what the posts are stamped at)
    now = datetime.datetime.now(pytz.timezone('GMT'))
    # Get the month and year as two separate variables
    month = f'{now.month:02d}'
    year = now.year
    # Format the month and year as a string with a leading zero for single digit months
    time = filename.replace('.csv', '')
    gaw_url = 'https://GreatAwakening.win'
    download_url = 'https://github.com/Fatality-GAW/fatality-gaw.github.io/archive/refs/heads/main.zip'
    changes_url = 'https://github.com/Fatality-GAW/fatality-gaw.github.io/commits/main'
    code_url = 'https://github.com/Fatality-GAW/fatality-gaw.github.io-Python-Code'
    title1 = 'GREATAWAKENING.WIN'
    title2 = 'STICKIES RELOADED'
    title3 = 'STICKIES RELOADING..'
    if filename.startswith(f'{year}.{month}'):
        title = f'{time} {title1} {title3}'
    else:
        title = f'{time} {title1} {title2}'
    fire = '🔥'
    new = '🆕'
    reloading = '🔄'
    boom = '💥'
    all_link = '🌐'
    download_link = '📥'
    changes_link = '📃'
    code_link = '📑'
    fonts = 'Arial, sans-serif, Segoe UI Emoji, Noto Color Emoji, Twemoji'

    # Colors
    black = '#000000'
    white = '#ffffff'
    pale_grey = '#4d4848'
    pale_red = '#dc4848'
    pale_blue = '#346c91'
    title_blue = '#4ca1e0'
    dark_blue = '#305068'
    bright_blue = '#77c5ff'
    h1_color = '#d3d3d3'
    h1_shadow = '#464c8a'
    even_row = '#202020'
    odd_row = '#111111'
    # User Row Colors
    general_chat = '#400f0f'
    unleashed = '#2b2b46'
    sunday_funnies = '#303630'
    wins_of_day = '#3c3727'
    extra_wins = '#3c2c36'
    daily_discussion = '#330133'
    hold_line = '#003333'
    weekly_discussion = '#183718'
    delta_discussion = '#421128'
    daily_prayer = '#68682b'
    anon_theater = '#04002f'
    new_q = '#7d7b7b'

    # Read csv file and extract the columns of interest
    with open(f'./CSVs/{filename}', newline='') as f:
        reader = csv.reader(f)
        data = [[row[1], row[2], row[4], row[6]] for row in reader]

    # Create table rows
    table_rows = []

    row_count = 0
    # Identify if currently reading ALL.CSV:
    if time == all_stickies_file:
        row_count += 1
        # count how many rows have a title
        for index, row in enumerate(data):
            if row[2].strip() != "":
                row_count += 1

    for index, row in enumerate(data):
        row[1] = f'{gaw_url}{row[1]}'
        # skip if there's no title (post is gone)
        if row[2].strip() == "":
            continue

        # switch up the count if this is the "ALL" stickies or not:
        if time == all_stickies_file:
            row_count -= 1
        else:
            row_count += 1

        # Set alternating row colors
        row_color = even_row if row_count % 2 == 0 else odd_row

        # Row_color for bubble_bursts 'General Chat for'
        chat_regex = r'General Chat for'
        if re.search(chat_regex, row[2]):
            if row[3] == 'bubble_bursts':
                row_color = general_chat

        # Row_color for ashlanddog's & team's 'UNLEASHED...' & 'Time For A "Buzz"'
        unleashed_regex = r'UNLEASHED...'
        buzz_regex = r'Time For A "Buzz"'
        if re.search(unleashed_regex, row[2]) or re.search(buzz_regex, row[2]):
            if row[3] == 'ashlanddog' or row[3] == 'Taffy333' or row[3] == 'Nurarihyon_no_MAGA':
                row_color = unleashed

        # Row_color for Uncle_Fester's 'Sunday Funnies'
        sunday_regex = r'Sunday Funnies'
        if re.search(sunday_regex, row[2]):
            if row[3] == 'Uncle_Fester':
                row_color = sunday_funnies

        # Row_color for WinsAnon's 'Wins of the Day:'
        wins_regex = r'Wins of the Day:'
        if re.search(wins_regex, row[2]):
            if row[3] == 'WinsAnon':
                row_color = wins_of_day

        # Row_color for Puncake150's 'Extra Wins of the Day:'
        wins_regex = r'Extra Wins of the Day:'
        if re.search(wins_regex, row[2]):
            if row[3] == 'Puncake150':
                row_color = extra_wins

        # Row_color for meteorknife's & high-valyrian's 'Daily Discussion Thread'
        daily_regex = r'Daily Discussion Thread'
        if re.search(daily_regex, row[2]):
            if row[3] == 'high-valyrian' or row[3] == 'meteorknife':
                row_color = daily_discussion

        # Row_color for penisse's 'HOLD THE LINE.'
        hold_regex = r'HOLD THE LINE.'
        if re.search(hold_regex, row[2]):
            if row[3] == 'penisse':
                row_color = hold_line

        # Row_color for meteorknife's 'Weekly Discussion Thread'
        weekly_discussion_regex = r'Weekly Discussion Thread'
        if re.search(weekly_discussion_regex, row[2]):
            if row[3] == 'meteorknife':
                row_color = weekly_discussion

        # Row_color for ChronicMetamorphosis 'Q in 3D: The Daily Delta Discussion'
        delta_discussion_regex = r'Q in 3D: The Daily Delta Discussion'
        if re.search(delta_discussion_regex, row[2]):
            if row[3] == 'ChronicMetamorphosis':
                row_color = delta_discussion

        # Row_color for Slechta5614 'DAILY PRAYER THREAD'
        daily_prayer_regex = r'DAILY PRAYER THREAD'
        if re.search(daily_prayer_regex, row[2].upper()):
            if row[3] == 'Slechta5614':
                row_color = daily_prayer

        # Row_color for meteorknife's 'Q Drop'
        Qdrops1_regex = f'Q Drop'
        if re.search(Qdrops1_regex, row[2]):
            if row[3] == 'meteorknife':
                row_color = new_q

        # Row_color for general 'Anon Theatre'
        anon_theater_regex = r'Anon Theatre'
        if re.search(anon_theater_regex, row[2]):
            row_color = anon_theater

        # Row_color for general 'New Q'
        Qdrops1_regex = f'New Q'
        if re.search(Qdrops1_regex, row[2]):
            row_color = new_q

        # Create table row
        table_row = f'\t\t\t\t<tr class="table_row" id="{row_count}" style="background-color: {row_color};" '
        table_row += f'onclick="if (event.target.tagName == \'A\') return true; '
        table_row += f'window.open(\'{row[1]}\',\'_blank\',\'noopener noreferrer\');" >'
        table_row += f'<td class="number_col">{row_count}</td>'
        table_row += f'<td class="detail_col"><span>{row[3]}</span> @<br>{row[0]}</td>'
        table_row += f'<td class="title_col"><a href="{row[1]}" target="_blank">{row[2]}</a></td>'
        table_row += '</tr>\n'
        table_rows.append(table_row)

    # Create the HTML page
    # HEADER
    html = ''
    html += '<!DOCTYPE html>\n'
    html += '<html>\n'
    html += '\t<head>\n'
    html += '\t\t<meta charset="UTF-8">\n'
    html += f'\t\t<title>{fire} {title} {fire}</title>\n'
    html += '\t\t<style>\n'
    html += '\t\t\tbody {\n' + \
            f'\t\t\t\tbackground-color:{black};\n' + \
            f'\t\t\t\tfont-family: {fonts};\n' + \
            f'\t\t\t\tmargin: 0;\n' + \
            f'\t\t\t\tpadding: 0;\n' + \
            '\t\t\t}\n'
    html += '\t\t\th1 {\n' + \
            f'\t\t\t\tfont-size: 2.5em;\n' + \
            f'\t\t\t\tfont-weight: normal;\n' + \
            f'\t\t\t\ttext-align: center;\n' +\
            f'\n\t\t\t\ttext-shadow: 0px 0px 4px {h1_shadow}, 0px 0px 4px {h1_shadow}, 0px 0px 5px {h1_shadow};\n' + \
            '\t\t\t}\n'
    html += '\t\t\th1 a {\n' + \
            f'\t\t\t\ttext-decoration: none;\n' + \
            f'\t\t\t\tcolor: {h1_color};\n' + \
            f'\t\t\t\tfont-weight: bold;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* Table Settings */\n' + \
            '\t\t\ttable {\n' + \
            f'\t\t\t\twidth: 75%;\n' + \
            f'\t\t\t\tmargin: 0 auto;\n' + \
            '\t\t\t}\n'
    html += '\t\t\ttable,\n' + \
            '\t\t\ttbody,\n' + \
            '\t\t\ttr,\n' + \
            '\t\t\ttd {\n' + \
            f'\t\t\t\tborder: 1px solid {black};\n' + \
            '\t\t\t\tborder-collapse: collapse;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* Column Defaults */\n' + \
            '\t\t\t.number_col {\n' + \
            '\t\t\t\tbackground-color: black;\n' + \
            '\t\t\t\ttop: 0;\n' + \
            '\t\t\t\ttext-align: right;\n' + \
            '\t\t\t\tvertical-align: top;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t.detail_col {\n' + \
            '\t\t\t\tfont-weight: bold;\n' + \
            '\t\t\t\tfont-size: xx-small;\n' + \
            '\t\t\t\tpadding: 1em;\n' + \
            '\t\t\t\ttext-align: left;\n' + \
            '\t\t\t\tvertical-align: top;\n' + \
            '\t\t\t\twidth: 10%;\n' + \
            '\t\t\t\tmax-width: 10%;\n' + \
            '\t\t\t\twhite-space: nowrap;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t.title_col {\n' + \
            '\t\t\t\tpadding: 1em;\n' + \
            '\t\t\t\tpadding-left: 5%;\n' + \
            '\t\t\t\tpadding-right: 5%;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t.title_col a {\n' + \
            '\t\t\t\ttext-decoration: none;\n' + \
            '\t\t\t\tfont-weight: bold;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* Hovering over a row */\n' + \
            '\t\t\t\t/* Number Column */\n' + \
            '\t\t\t.table_row:hover td:first-child {\n' + \
            f'\t\t\t\tcolor: {white};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n' + \
            '\t\t\t\t/* Detail Column */\n' + \
            '\t\t\t\t\t\t/* Name Color */\n' + \
            '\t\t\t.table_row:hover td:nth-child(2) span {\n' + \
            f'\t\t\t\tcolor: {bright_blue};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n' + \
            '\t\t\t\t\t\t/* Time Color */\n' + \
            '\t\t\t.table_row:hover td:nth-child(2) {\n' + \
            f'\t\t\t\tcolor: {white};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n' + \
            '\t\t\t\t/* Title Column */\n' + \
            '\t\t\t.table_row:hover td:nth-child(3) a {\n' + \
            f'\t\t\t\tcolor: {pale_red};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* Transition Times */\n' + \
            '\t\t\t.table_row td {\n' + \
            '\t\t\t\ttransition: all 1.0s;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t.table_row span,\n' + \
            '\t\t\t.table_row a {\n' + \
            '\t\t\t\ttransition: all 0.1s;\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* Default text settings for number col */\n' + \
            '\t\t\t.table_row td:first-child {\n' + \
            f'\t\t\t\tcolor: {pale_grey};\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* Default text settings for detail col */\n' + \
            '\t\t\t.table_row td:nth-child(2) span {\n' + \
            f'\t\t\t\tcolor: {dark_blue}; /* the author */\n' + \
            '\t\t\t}\n' + \
            '\t\t\t.table_row td:nth-child(2) {\n' + \
            f'\t\t\t\tcolor: {pale_grey}; /* the time */\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* Default text settings for title col */\n' + \
            '\t\t\t.table_row td:nth-child(3) a {\n' + \
            f'\t\t\t\tcolor: {title_blue};\n' + \
            '\t\t\t}\n'
    html += '\t\t\t/* on-screen buttons */\n' + \
            '\t\t\t#menu-div {\n' + \
            '\t\t\t\tposition: fixed;\n' + \
            '\t\t\t\ttop: 125px;\n' + \
            '\t\t\t\tright: 0%;\n' + \
            '\t\t\t\tz-index: 9999;\n' + \
            '\t\t\t}\n' + \
            '\t\t\t#left-div {\n' + \
            '\t\t\t\tposition: fixed;\n' + \
            '\t\t\t\ttop: 50%;\n' + \
            '\t\t\t\tleft: 0%;\n' + \
            '\t\t\t\ttransform: translateY(-50%);\n' + \
            '\t\t\t\tz-index: 9999;\n' + \
            '\t\t\t}\n' + \
            '\t\t\t#right-div {\n' + \
            '\t\t\t\tposition: fixed;\n' + \
            '\t\t\t\ttop: 50%;\n' + \
            '\t\t\t\tright: 0%;\n' + \
            '\t\t\t\ttransform: translateY(-50%);\n' + \
            '\t\t\t\tz-index: 9999;\n' + \
            '\t\t\t}\n' + \
            '\t\t\t#menu-div span,\n' + \
            '\t\t\t#left-div span,\n' + \
            '\t\t\t#right-div span {\n' + \
            '\t\t\t\tfont-size:4em;\n' + \
            '\t\t\t}\n' + \
            '\t\t\t#menu-div span a,\n' + \
            '\t\t\t#left-div span a,\n' + \
            '\t\t\t#right-div span a {\n' + \
            '\t\t\t\ttext-decoration:none;\n' + \
            f'\t\t\t\tcolor:{pale_blue};\n' + \
            '\t\t\t}\n'
    html += '\t\t</style>\n'
    html += '\t</head>\n'

    # BODY
    html += '\t<body>\n'

    # UPPER RIGHT SIDE MENU LINK ☰
    # if the file name isn't 2020.08.csv [0], or today's yyyy.mm.csv [-2] put the upper right side menu link:
    if filename != sorted(os.listdir('./CSVs'))[0] and filename != sorted(os.listdir('./CSVs'))[-2]:
        html += '\t\t<div id="menu-div"><span><a href="index.html" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'

    # LEFT SIDE ARROW ◄ ( or ☰ )
    # if the file name isn't 2020.08.csv [0], or ALL.csv [-1] put the ◄ on the left side of the page
    if filename != sorted(os.listdir('./CSVs'))[0] and filename != sorted(os.listdir('./CSVs'))[-1]:
        previous_index = sorted(os.listdir('./CSVs')).index(filename) - 1
        lname = sorted(os.listdir('./CSVs'))[previous_index].replace('./CSVs', '').replace('.csv', '')
        leftlink = f'{lname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'\t\t<div id="left-div"><span><a href="{leftlink}" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">◄</a></span></div>\n'
    # but if the file name is 2020.08.csv [0], put the ☰ on the left side
    elif filename == sorted(os.listdir('./CSVs'))[0]:
        html += f'\t\t<div id="left-div"><span><a href="index.html" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'

    # RIGHT SIDE ARROW ► ( or ☰ )
    # If the file name isn't today's yyyy.mm.csv [-2], or ALL.csv [-1] put the ► on the right side of the page
    if filename != sorted(os.listdir('./CSVs'))[-2] and filename != sorted(os.listdir('./CSVs'))[-1]:
        next_index = sorted(os.listdir('./CSVs')).index(filename) + 1
        rname = sorted(os.listdir('./CSVs'))[next_index].replace('./CSVs', '').replace('.csv', '')
        rightlink = f'{rname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'\t\t<div id="right-div"><span><a href="{rightlink}" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">►</a></span></div>\n'
    # but if the file name is today's yyyy.mm.csv [-2], put the ☰ on the right side
    elif filename == sorted(os.listdir('./CSVs'))[-2]:
        html += f'\t\t<div id="right-div"><span><a href="index.html" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'

    # TITLE
    html += f'\t\t<h1><a href="{gaw_url}" target="_blank">{fire} {title} {fire}</a></h1>\n'

    # TABLE
    html += '\t\t<table>\n\t\t\t<tbody>\n'
    html += ''.join(table_rows)
    html += '\t\t\t</tbody>\n\t\t</table>\n'

    # FOOTER
    html += '\t</body>\n</html>\n'

    # Write HTML page to file
    title = title.replace(title3, title2).replace(" ", ".")
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
title = f'{fire} {title1} {title2} {fire}'

# Create the index.html HTML page

# HEADER
html = ''
html += '<!DOCTYPE html>\n'
html += '<html>\n'
html += '\t<head>\n'
html += '\t\t<meta charset="UTF-8">\n'
html += f'\t\t<title>{title}</title>\n'
html += '\t\t<style>\n'
html += '\t\t\tbody {\n' + \
        f'\t\t\t\tbackground-color: {black};\n' + \
        f'\t\t\t\tcolor: {pale_grey};\n' + \
        f'\t\t\t\tfont-family: {fonts};\n' + \
        '\t\t\t\tmargin: 0;\n' + \
        '\t\t\t\tpadding: 0;\n' + \
        '\t\t\t}\n'
html += '\t\t\th1 {\n' + \
        '\t\t\t\tfont-size: 2.5em;\n' + \
        '\t\t\t\tfont-weight: normal;\n' + \
        '\t\t\t\ttext-align: center;\n' + \
        f'\t\t\t\ttext-shadow: 0px 0px 4px {h1_shadow}, 0px 0px 4px {h1_shadow}, 0px 0px 5px {h1_shadow};\n' + \
        '\t\t\t}\n'
html += '\t\t\th1 a {\n' + \
        '\t\t\t\ttext-decoration: none;\n' + \
        '\t\t\t\tfont-weight: bold;\n' + \
        f'\t\t\t\tcolor: {white};\n' + \
        '\t\t\t}\n'
html += '\t\t\ttable {\n' + \
        '\t\t\t\twidth: 75%;\n' + \
        '\t\t\t\tmargin: 0 auto;\n' + \
        '\t\t\t}\n'
html += '\t\t\t#all {\n' + \
        '\t\t\t\ttop: 25px;\n' + \
        '\t\t\t\tleft: 2%;\n' + \
        '\t\t\t}\n'
html += '\t\t\t#download {\n' + \
        '\t\t\t\ttop: 25px;\n' + \
        '\t\t\t\tright: 2%;\n' + \
        '\t\t\t}\n'
html += '\t\t\t#changes {\n' + \
        '\t\t\t\ttop: 125px;\n' + \
        '\t\t\t\tright: 2%;\n' + \
        '\t\t\t}\n'
html += '\t\t\t#code {\n' + \
        '\t\t\t\ttop: 225px;\n' + \
        '\t\t\t\tright: 2%;\n' + \
        '\t\t\t}\n'
html += '\t\t\t#all,\n' + \
        '\t\t\t\t#download,\n' + \
        '\t\t\t\t#changes,\n' + \
        '\t\t\t\t#code {\n' + \
        '\t\t\t\tposition: fixed;\n' + \
        '\t\t\t\tz-index: 9999;\n' + \
        '\t\t\t}\n'
html += '\t\t\t#all span,\n' + \
        '\t\t\t#download span,\n' + \
        '\t\t\t#changes span,\n' + \
        '\t\t\t#code span {\n' + \
        '\t\t\t\tfont-size:3em;\n' + \
        '\t\t\t}\n'
html += '\t\t\t#all span a,\n' + \
        '\t\t\t#download span a,\n' + \
        '\t\t\t#changes span a,\n' + \
        '\t\t\t#code span a {\n' + \
        '\t\t\t\ttext-decoration: none;\n' + \
        '\t\t\t}\n'
html += '\t\t</style>\n'
html += '\t</head>\n'
html += '\t<body>\n'
html += f'\t\t<h1><a href="{gaw_url}">{title}</a></h1>\n'
html += f'\t\t<div id="all"><span><a href="{all_stickies_file}.GREATAWAKENING.WIN.STICKIES.RELOADED.html" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' +\
        f'onmouseout="this.style.textShadow=\'none\'">{all_link}</a></span></div>\n'
html += f'\t\t<div id="download"><span><a href="{download_url}" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' +\
        f'onmouseout="this.style.textShadow=\'none\'">{download_link}</a></span></div>\n'
html += f'\t\t<div id="changes"><span><a href="{changes_url}" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' +\
        f'onmouseout="this.style.textShadow=\'none\'">{changes_link}</a></span></div>\n'
html += f'\t\t<div id="code"><span><a href="{code_url}" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' +\
        f'onmouseout="this.style.textShadow=\'none\'">{code_link}</a></span></div>\n'
html += '<table>\n<tbody>\n'
for index, file in enumerate(files):
    fileTitle = file.replace('html', '').replace('.', ' ').replace(' ', '.', 1).\
        replace('GREATAWAKENING WIN', title1).strip()
    # Set alternating row colors
    row_color = even_row if index % 2 == 0 else odd_row
    table_row = f'<tr style="background-color: {row_color}; border-bottom: 1px solid darkred; text-align:center;" '
    table_row += f'onmouseover="this.style.backgroundColor=\'#253147\'; this.childNodes[0].childNodes[0].style.color=\'#dc4848\'; this.childNodes[0].childNodes[0].style.textShadow=\'0px 0px 5px black\';" '
    table_row += f'onmouseout="this.style.backgroundColor=\'{row_color}\'; this.childNodes[0].childNodes[0].style.color=\'#4ca1e0\'; this.childNodes[0].childNodes[0].style.textShadow=\'none\';" '
    table_row += f'onclick="window.location.href=\'./{file}\'"; >'
    if first_post:
        if file.startswith(f'{year}.{month}'):
            reloadingTitle = file.replace('html', '').replace('.', ' ').replace(' ', '.', 1).replace(
                'GREATAWAKENING WIN', title1).replace(title2, title3).strip()
            table_row += f'<td style="padding:1em;color:#4ca1e0;font-weight:bold;"><a href="./{file}" target="_self" style="color:inherit;text-decoration:inherit;">{reloading} {fire} {reloadingTitle} {fire} {reloading}</a></td>'
        else:
            table_row += f'<td style="padding:1em;color:#4ca1e0;font-weight:bold;"><a href="./{file}" target="_self" style="color:inherit;text-decoration:inherit;">{boom} {new} {fire} {fileTitle} {fire} {new} {boom}</a></td>'
            first_post = False
    else:
        table_row += f'<td style="padding:1em;color:#4ca1e0;font-weight:bold;"><a href="./{file}" target="_self" style="color:inherit;text-decoration:inherit;">{fire} {fileTitle} {fire}</a></td>'
    table_row += '</tr>'
    html += table_row
html += '</tbody>\n</table>\n</body>\n</html>'


# Write the index.html:
with open(path, mode='w', encoding='utf-8') as file:
    file.write(html)
    print(f'wrote \'{path}\'')
