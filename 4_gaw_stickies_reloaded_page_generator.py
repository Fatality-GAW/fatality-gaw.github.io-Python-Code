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

import pytz as pytz

# Define a regular expression pattern to match the filename format
pattern = re.compile(r'^(\d{4}\.\d{2})\.csv$')

# Loop over all files in the current directory
for filename in os.listdir('./CSVs'):

    name_of_all_stickies_file = "ALL"  # ALL.CSV's name "ALL" is defined in section 4: of 3_split_data_into_yyyy.mm.csv_files.py
    count = 0
    last_title = ""
    # Get the current date and time in GMT (because that's what the posts are stamped at)
    now = datetime.datetime.now(pytz.timezone('GMT'))
    # Get the month and year as two separate variables
    month = f'{now.month:02d}'
    year = now.year
    # Format the month and year as a string with a leading zero for single digit months
    time = filename.replace('.csv', '')
    page = f'https://GreatAwakening.win'
    title1 = f'GREATAWAKENING.WIN'
    title2 = f'STICKIES RELOADED'
    title3 = f'STICKIES RELOADING..'
    if filename.startswith(f'{year}.{month}'):
        title = f'{time} {title1} {title3}'
    else:
        title = f'{time} {title1} {title2}'
    everything = '🌐'
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
    # Identify if currently reading ALL.CSV:
    if time == name_of_all_stickies_file:
        row_count += 1
        # count how many rows have a title
        for index, row in enumerate(data):
            if row[2].strip() != "":
                row_count += 1

    for index, row in enumerate(data):
        row[1] = f'{page}{row[1]}'
        # skip if there's no title (post is gone)
        if row[2].strip() == "":
            continue

        # switch up the count if this is the "ALL" stickies or not:
        if time == name_of_all_stickies_file:
            row_count -= 1
        else:
            row_count += 1

        # Set alternating row colors
        row_color = "#202020" if row_count % 2 == 0 else "#111111"

        # Check if data value matches regular expression for bubble_bursts' general chat
        chat_regex = r'General Chat for'
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
        # meteorknife's "Weekly Discussion Thread"

        # Check if data value matches regular expression for 'New Q'
        Qdrops1_regex = f'New Q'
        if re.search(Qdrops1_regex, row[2]):
            row_color = "rgb(230, 230, 230)"

        # Create table row
        table_row = f'<tr class="table_row" id="{row_count}" style="background-color: {row_color};" '
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
    html += '<head>\n'
    html += '<meta charset="UTF-8">\n'
    html += f'<title>{fire} {title} {fire}</title>\n'

    # CSS
    # Colors
    fonts = 'Arial, sans-serif, Segoe UI Emoji, Noto Color Emoji, Twemoji'
    black = '#000000'
    white = '#ffffff'
    pale_grey = '#4d4848'
    pale_red = '#dc4848'
    pale_blue = '#346c91'
    title_blue = '#4ca1e0'
    dark_blue = '#305068'
    bright_blue = '#77c5ff'
    h1_color = 'lightgray'
    h1_shadow = '#464c8a'

    html += '<style>\n'
    html += 'body {\n' + f'background-color:{black};\nfont-family: {fonts}' +\
            ';\nmargin: 0;\npadding: 0;\n}\n'
    html += 'h1 {\nfont-size: 2.5em;\nfont-weight: normal;\ntext-align: center;' +\
            f'\ntext-shadow: 0px 0px 4px {h1_shadow}, 0px 0px 4px {h1_shadow}, 0px 0px 5px {h1_shadow};' + '\n}\n'
    html += 'h1 a {\ntext-decoration:none;\n' + f'color:{h1_color};\n' + 'font-weight:bold\n}\n'

    html += '/* Table Settings */\n'
    html += 'table {\nwidth: 75%;\nmargin: 0 auto;\n}\n'
    html += 'table, tbody, tr, td {\n' + f'border: 1px solid {black};\n' + 'border-collapse: collapse\n}\n'

    html += '/* Column Defaults */\n'
    html += '.number_col {\nbackground-color: black;\ntop: 0;\ntext-align: right;\nvertical-align: top;\n}\n'
    html += '.detail_col {\nfont-weight:bold;\nfont-size:xx-small;\npadding:1em;\ntext-align:left;\n' + \
            'vertical-align:top;\nwidth:10%;\nmax-width:10%;\nwhite-space:nowrap;\n}\n'
    html += '.title_col {\npadding:1em;\npadding-left:5%;\npadding-right:5%;\n}\n'
    html += '.title_col a {\ntext-decoration:none;\nfont-weight:bold;\n}\n'

    html += '/* Hovering over a row */\n'
    html += '        /* Number Column */\n'
    html += '.table_row:hover td:first-child {\n' + f'color: {white};\n' + \
            f'text-shadow: 0px 0px 10px {black};\n' + '}\n'
    html += '        /* Detail Column */\n'
    html += '                          /* Name Color */\n'
    html += '.table_row:hover td:nth-child(2) span {\n' + f'color: {bright_blue};\n' + \
            f'text-shadow: 0px 0px 10px {black};\n' + '}\n'
    html += '                          /* Time Color */\n'
    html += '.table_row:hover td:nth-child(2) {\n' + f'color: {white};\n' + \
            f'text-shadow: 0px 0px 10px {black};\n' + '}\n'
    html += '        /* Title Column */\n'
    html += '.table_row:hover td:nth-child(3) a {\n' + f'color: {pale_red};\n' + \
            f'text-shadow: 0px 0px 10px {black};\n' + '}\n'

    html += '/* Transition Times */\n'
    html += '.table_row td {\ntransition: all 1.5s;\n}\n'
    html += '.table_row span, .table_row a {\ntransition: all 0.1s;\n}\n'

    html += '/* Default text settings for number col */\n'
    html += '.table_row td:first-child {\n' + f'color: {pale_grey};\n' + '}\n'

    html += '/* Default text settings for detail col */\n'
    html += '.table_row td:nth-child(2) span {\n' + f'color: {dark_blue}; /* the author */\n' + '}\n'
    html += '.table_row td:nth-child(2) {\n' + f'color: {pale_grey}; /* the time */\n' + '}\n'

    html += '/* Default text settings for title col */\n'
    html += '.table_row td:nth-child(3) a {\n' + f'color: {title_blue};\n' + '}\n'

    html += '/* on-screen buttons */\n'
    html += '#menu-div {\nposition: fixed;\ntop: 125px;\nright: 0%;\nz-index: 9999;\n}\n'
    html += '#left-div {\nposition: fixed;\ntop: 50%;\nleft: 0%;\ntransform: translateY(-50%);\nz-index: 9999;\n}\n'
    html += '#right-div {\nposition: fixed;\ntop: 50%;\nright: 0%;\ntransform: translateY(-50%);\nz-index: 9999;\n}\n'
    html += '#menu-div span,\n#left-div span,\n#right-div span {\nfont-size:4em;\n}\n'
    html += '#menu-div span a,\n#left-div span a,\n#right-div span a {\ntext-decoration:none;\n' + \
            f'color:{pale_blue}' + ';\n}\n'
    html += '</style>\n'
    html += '</head>\n'

    # BODY
    html += '<body>\n'

    # UPPER RIGHT SIDE MENU LINK ☰
    # if the file name isn't 2020.08.csv [0], or today's yyyy.mm.csv [-2] put the upper right side menu link:
    if filename != sorted(os.listdir('./CSVs'))[0] and filename != sorted(os.listdir('./CSVs'))[-2]:
        html += '<div id="menu-div"><span><a href="index.html"' + \
                f'onmouseover="this.style.color=\'{pale_red}\'"' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'

    # LEFT SIDE ARROW ◄ ( or ☰ )
    # if the file name isn't 2020.08.csv [0], or ALL.csv [-1] put the ◄ on the left side of the page
    if filename != sorted(os.listdir('./CSVs'))[0] and filename != sorted(os.listdir('./CSVs'))[-1]:
        previous_index = sorted(os.listdir('./CSVs')).index(filename) - 1
        lname = sorted(os.listdir('./CSVs'))[previous_index].replace('./CSVs', '').replace('.csv', '')
        leftlink = f'{lname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'<div id="left-div"><span><a href="{leftlink}"' + \
                f'onmouseover="this.style.color=\'{pale_red}\'"' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">◄</a></span></div>\n'
    # but if the file name is 2020.08.csv [0], put the ☰ on the left side
    elif filename == sorted(os.listdir('./CSVs'))[0]:
        html += f'<div id="left-div"><span><a href="index.html"' + \
                f'onmouseover="this.style.color=\'{pale_red}\'"' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'

    # RIGHT SIDE ARROW ► ( or ☰ )
    # If the file name isn't today's yyyy.mm.csv [-2], or ALL.csv [-1] put the ► on the right side of the page
    if filename != sorted(os.listdir('./CSVs'))[-2] and filename != sorted(os.listdir('./CSVs'))[-1]:
        next_index = sorted(os.listdir('./CSVs')).index(filename) + 1
        rname = sorted(os.listdir('./CSVs'))[next_index].replace('./CSVs', '').replace('.csv', '')
        rightlink = f'{rname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'<div id="right-div"><span><a href="{rightlink}"' + \
                f'onmouseover="this.style.color=\'{pale_red}\'"' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">►</a></span></div>\n'
    # but if the file name is today's yyyy.mm.csv [-2], put the ☰ on the right side
    elif filename == sorted(os.listdir('./CSVs'))[-2]:
        html += f'<div id="right-div"><span><a href="index.html"' + \
                f'onmouseover="this.style.color=\'{pale_red}\'"' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'

    # TITLE
    html += f'<h1><a href="{page}" target="_blank">{fire} {title} {fire}</a></h1>\n'

    # TABLE
    html += '<table>\n<tbody>\n'
    html += ''.join(table_rows)
    html += '</tbody>\n</table>\n'

    # FOOTER
    html += '</body>\n</html>'

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
with open(path, mode='w', encoding='utf-8') as f:
    title = f'{fire} {title1} {title2} {fire}'
    html = f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n'
    html += f'<title>{title}</title>\n'
    html += '<style>\nbody {\nbackground-color:black;\ncolor:#4d4848;\nfont-family: Arial, sans-serif, Segoe UI Emoji, '
    html += 'Noto Color Emoji, Twemoji;\nmargin: 0; padding: 0;}\nh1 {\nfont-size: 2.5em; font-weight: normal; color: #464c8a;'
    html += '\ntext-align: center;text-shadow: 0px 0px 4px #464c8a, 0px 0px 4px #464c8a, 0px 0px 5px #464c8a;\n}</style>\n</head>\n<body>\n'
    html += f'<h1><a href="{page}" style="text-decoration:none;color:lightgray;font-weight:bold">{title}</a></h1>\n'
    html += '<div id="left-div" style="position: fixed; top: 25px; left: 2%; z-index: 9999;">'
    html += f'<span style="font-size:3em;"><a href="ALL.GREATAWAKENING.WIN.STICKIES.RELOADED.html" style="text-decoration:none;" onmouseover="this.style.textShadow=\'0px 0px 10px white\';" onmouseout="this.style.textShadow=\'none\'">{everything}</a></span></div>\n'
    html += '<div id="right-div" style="position: fixed; top: 25px; right: 2%; z-index: 9999;">'
    html += f'<span style="font-size:3em;"><a href="https://github.com/Fatality-GAW/fatality-gaw.github.io/archive/refs/heads/main.zip" style="text-decoration:none;" onmouseover="this.style.textShadow=\'0px 0px 10px white\';" onmouseout="this.style.textShadow=\'none\'">{download}</a></span></div>\n'
    html += '<div id="right-div" style="position: fixed; top: 125px; right: 2%; z-index: 9999;">'
    html += f'<span style="font-size:3em;"><a href="https://github.com/Fatality-GAW/fatality-gaw.github.io/commits/main" style="text-decoration:none;" onmouseover="this.style.textShadow=\'0px 0px 10px white\';" onmouseout="this.style.textShadow=\'none\'">{changes}</a></span></div>\n'
    html += '<div id="right-div" style="position: fixed; top: 225px; right: 2%; z-index: 9999;">'
    html += f'<span style="font-size:3em;"><a href="https://github.com/Fatality-GAW/fatality-gaw.github.io-Python-Code" style="text-decoration:none;" onmouseover="this.style.textShadow=\'0px 0px 10px white\';" onmouseout="this.style.textShadow=\'none\'">{code}</a></span></div>\n'
    html += '<table style="width: 75%; margin: 0 auto;">\n<tbody>\n'
    for index, file in enumerate(files):
        fileTitle = file.replace('html', '').replace('.', ' ').replace(' ', '.', 1).replace('GREATAWAKENING WIN',
                                                                                            title1).strip()
        # Set alternating row colors
        row_color = "#202020" if index % 2 == 0 else "#111111"
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
    f.write(html)
    print(f'wrote \'{path}\'')
