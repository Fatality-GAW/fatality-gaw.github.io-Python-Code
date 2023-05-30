"""
    Fatality's & ChatGPT's GAW Stickies Reloaded Page Generator
    -----------------------------------------------

    Step 1:  you must have the output from 3_split_data_into_yyyy.mm.csv_files.py

    Step 2: remove any csv files you don't want to generate a page for.

    Step 3: run the script, it will generate the web pages.

"""
import csv
import datetime
import os
import re
import pytz as pytz

# Define ALL.CSV's name (MUST MATCH what is defined in section 4: of 3_split_data_into_yyyy.mm.csv_files.py)
all_stickies_file = "ALL"

# Get the current date and time in GMT (because that's what the posts are stamped at)
now = datetime.datetime.now(pytz.timezone('GMT'))

# Get the month and year as two separate variables
month = f'{now.month:02d}'
year = now.year

# Define some urls:
gaw_url = 'https://GreatAwakening.win'
download_url = 'https://github.com/Fatality-GAW/fatality-gaw.github.io/archive/refs/heads/main.zip'
changes_url = 'https://github.com/Fatality-GAW/fatality-gaw.github.io/commits/main'
code_url = 'https://github.com/Fatality-GAW/fatality-gaw.github.io-Python-Code'

# Define variables used in html:
title1 = 'GREATAWAKENING.WIN'
title2 = 'STICKIES RELOADED'
title3 = 'STICKIES RELOADING..'
gaw = 'GREATAWAKENING WIN'
gaw_stickies_reloaded_appendix = '.GREATAWAKENING.WIN.STICKIES.RELOADED.html'
fire = '🔥'
new = '🆕'
reloading = '🔄'
boom = '💥'
all_link = '🌐'
download_link = '📥'
changes_link = '📃'
code_link = '📑'

# CSS variables:
fonts = 'Arial, sans-serif, Segoe UI Emoji, Noto Color Emoji, Twemoji'
none = 'none'
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
row_highlight = '#253147'

# Regular sticky pattern row colors:
general_chat = '#4a2422'
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

# Loop over all files in the current directory
for csv_file in os.listdir('./CSVs'):
    # Take the base csv_file name as the time.
    time = csv_file.replace('.csv', '')

    # Determine the title based the file name and if it matches this yyyy.MM it's reloading:
    if csv_file.startswith(f'{year}.{month}'):
        title = f'{time} {title1} {title3}'
    # Otherwise it's a regular title:
    else:
        title = f'{time} {title1} {title2}'

    # Read csv_file and extract the columns of interest
    with open(f'./CSVs/{csv_file}', newline='') as this_csv_file:
        reader = csv.reader(this_csv_file)
        csv_data = [[row[1], row[2], row[4], row[6]] for row in reader]

    # Create table rows
    table_rows = []

    row_count = 0
    # Identify if currently reading ALL.CSV:
    if time == all_stickies_file:
        # If so add an initial number, so it can start at 1 (instead of 0)
        row_count += 1
        # Then count how many rows have a title:
        for index, row in enumerate(csv_data):
            if row[2].strip() != "":
                row_count += 1

    # Iterate through all the csv_data to create html <TR />'s for each row of data:
    for index, row in enumerate(csv_data):
        row[1] = f'{gaw_url}{row[1]}'
        # Skip this row if there's no title (post is gone)
        if row[2].strip() == "":
            continue

        # Decrement count if the file is the "ALL" stickies:
        if time == all_stickies_file:
            row_count -= 1
        # Otherwise increment the count if it's not:
        else:
            row_count += 1

        # Set alternating row colors
        row_color = even_row if row_count % 2 == 0 else odd_row

        ''' \\/ \\/ START SECTION: handle row coloring for user/post patterns \\/ \\/ '''

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
        wins_regex = r'Wins of the Day'
        if re.search(wins_regex, row[2]):
            if row[3] == 'WinsAnon':
                row_color = wins_of_day

        # Row_color for Puncake150's 'Wins of the Day'
        wins_regex = r'Wins of the Day'
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

        ''' /\\ /\\ END SECTION: handle row coloring for user/post patterns /\\ /\\ '''

        # Create the table row
        table_row = ''
        table_row += f'\t\t\t\t<tr class="table_row" id="{row_count}" style="background-color: {row_color};" '
        table_row += 'onclick="if (event.target.tagName == \'A\') return true; '
        table_row += f'window.open(\'{row[1]}\',\'_blank\',\'noopener noreferrer\');" >'
        table_row += f'<td class="number_col">{row_count}</td>'
        table_row += f'<td class="detail_col"><span>{row[3]}</span> @<br>{row[0]}</td>'
        table_row += f'<td class="title_col"><a href="{row[1]}" target="_blank">{row[2]}</a></td>'
        table_row += '</tr>\n'

        # Add this row to the table_rows array:
        table_rows.append(table_row)

    # Create the HTML page for this csv_file:
    # HEADER
    html = ''
    html += '<!DOCTYPE html>\n'
    html += '<html>\n'
    html += '\t<head>\n'
    html += '\t\t<meta charset="UTF-8">\n'
    html += f'\t\t<title>{fire} {title} {fire}</title>\n'
    html += '\t\t<style>\n'
    html += '\t\t/* GENERAL SETTINGS */\n' + \
            '\t\t\tbody {\n' + \
            f'\t\t\t\tbackground-color: {black};\n' + \
            f'\t\t\t\tfont-family: {fonts};\n' + \
            '\t\t\t\tmargin: 0;\n' + \
            '\t\t\t\tpadding: 0;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\th1 {\n' + \
            '\t\t\t\tfont-size: 2.5em;\n' + \
            '\t\t\t\tfont-weight: normal;\n' + \
            '\t\t\t\ttext-align: center;\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 4px {h1_shadow}, 0px 0px 4px {h1_shadow}, 0px 0px 5px {h1_shadow};\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\th1 a {\n' + \
            '\t\t\t\ttext-decoration: none;\n' + \
            f'\t\t\t\tcolor: {h1_color};\n' + \
            '\t\t\t\tfont-weight: bold;\n' + \
            '\t\t\t}\n\n'
    html += '\t\t/* TABLE SETTINGS */\n' + \
            '\t\t\ttable {\n' + \
            '\t\t\t\twidth: 75%;\n' + \
            '\t\t\t\tmargin: 0 auto;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\ttable,\n' + \
            '\t\t\ttbody,\n' + \
            '\t\t\ttr,\n' + \
            '\t\t\ttd {\n' + \
            f'\t\t\t\tborder: 1px solid {black};\n' + \
            '\t\t\t\tborder-collapse: collapse;\n' + \
            '\t\t\t}\n\n'
    html += '\t\t/* DEFAULT COLUMN COLORS */\n' + \
            '\t\t\t.number_col {\n' + \
            f'\t\t\t\tbackground-color: {black};\n' + \
            '\t\t\t\ttop: 0;\n' + \
            '\t\t\t\ttext-align: right;\n' + \
            '\t\t\t\tvertical-align: top;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t.detail_col {\n' + \
            '\t\t\t\tfont-weight: bold;\n' + \
            '\t\t\t\tfont-size: xx-small;\n' + \
            '\t\t\t\tpadding: 1em;\n' + \
            '\t\t\t\ttext-align: left;\n' + \
            '\t\t\t\tvertical-align: top;\n' + \
            '\t\t\t\twidth: 10%;\n' + \
            '\t\t\t\tmax-width: 10%;\n' + \
            '\t\t\t\twhite-space: nowrap;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t.title_col {\n' + \
            '\t\t\t\tpadding: 1em;\n' + \
            '\t\t\t\tpadding-left: 5%;\n' + \
            '\t\t\t\tpadding-right: 5%;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t.title_col a {\n' + \
            '\t\t\t\ttext-decoration: none;\n' + \
            '\t\t\t\tfont-weight: bold;\n' + \
            '\t\t\t}\n\n'
    html += '\t\t/* ROW HOVERING COLORS */\n' + \
            '\t\t\t/* NUMBER COLUMN */\n' + \
            '\t\t\t.table_row:hover td:first-child {\n' + \
            f'\t\t\t\tcolor: {white};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t/* DETAIL COLUMN */\n' + \
            '\t\t\t\t\t/* NAME COLOR */\n' + \
            '\t\t\t.table_row:hover td:nth-child(2) span {\n' + \
            f'\t\t\t\tcolor: {bright_blue};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n' + \
            '\t\t\t\t\t/* TIME COLOR */\n' + \
            '\t\t\t.table_row:hover td:nth-child(2) {\n' + \
            f'\t\t\t\tcolor: {white};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t/* TITLE COLUMN */\n' + \
            '\t\t\t.table_row:hover td:nth-child(3) a {\n' + \
            f'\t\t\t\tcolor: {pale_red};\n' + \
            f'\t\t\t\ttext-shadow: 0px 0px 10px {black};\n' + \
            '\t\t\t}\n\n'
    html += '\t\t/* TRANSITION TIMES */\n' + \
            '\t\t\t/* NUMBER & TIME */\n' + \
            '\t\t\t.table_row td {\n' + \
            '\t\t\t\ttransition: all 1.0s;\n' + \
            '\t\t\t}\n' + \
            '\t\t\t/* NAME & TITLE */\n' + \
            '\t\t\t.table_row span,\n' + \
            '\t\t\t.table_row a {\n' + \
            '\t\t\t\ttransition: all 0.1s;\n' + \
            '\t\t\t}\n\n'
    html += '\t\t/* TEXT SETTINGS FOR.. */\n' + \
            '\t\t\t/* ..NUMBER COLUMN */\n' + \
            '\t\t\t.table_row td:first-child {\n' + \
            f'\t\t\t\tcolor: {pale_grey};\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t/* ..DETAIL COLUMN.. */\n' + \
            '\t\t\t\t/* ..AUTHOR */\n' + \
            '\t\t\t.table_row td:nth-child(2) span {\n' + \
            f'\t\t\t\tcolor: {dark_blue};\n' + \
            '\t\t\t}\n' + \
            '\t\t\t\t/* ..TIME */\n' + \
            '\t\t\t.table_row td:nth-child(2) {\n' + \
            f'\t\t\t\tcolor: {pale_grey};\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t/* ..TITLE COLUMN */\n' + \
            '\t\t\t.table_row td:nth-child(3) a {\n' + \
            f'\t\t\t\tcolor: {title_blue};\n' + \
            '\t\t\t}\n\n'
    html += '\t\t/* ON-SCREEN BUTTONS */\n' + \
            '\t\t\t#menu-div {\n' + \
            '\t\t\t\tposition: fixed;\n' + \
            '\t\t\t\ttop: 125px;\n' + \
            '\t\t\t\tright: 0%;\n' + \
            '\t\t\t\tz-index: 9999;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t#left-div {\n' + \
            '\t\t\t\tposition: fixed;\n' + \
            '\t\t\t\ttop: 50%;\n' + \
            '\t\t\t\tleft: 0%;\n' + \
            '\t\t\t\ttransform: translateY(-50%);\n' + \
            '\t\t\t\tz-index: 9999;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t#right-div {\n' + \
            '\t\t\t\tposition: fixed;\n' + \
            '\t\t\t\ttop: 50%;\n' + \
            '\t\t\t\tright: 0%;\n' + \
            '\t\t\t\ttransform: translateY(-50%);\n' + \
            '\t\t\t\tz-index: 9999;\n' + \
            '\t\t\t}\n\n' + \
            '\t\t\t#menu-div span,\n' + \
            '\t\t\t#left-div span,\n' + \
            '\t\t\t#right-div span {\n' + \
            '\t\t\t\tfont-size:4em;\n' + \
            '\t\t\t}\n\n' + \
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
    if csv_file != sorted(os.listdir('./CSVs'))[0] and csv_file != sorted(os.listdir('./CSVs'))[-2]:
        html += '\t\t<div id="menu-div"><span><a href="index.html" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'
    # LEFT SIDE ARROW ◄ ( or ☰ )
    # If the file name isn't 2020.08.csv [0], or ALL.csv [-1] put the ◄ on the left side of the page:
    if csv_file != sorted(os.listdir('./CSVs'))[0] and csv_file != sorted(os.listdir('./CSVs'))[-1]:
        previous_index = sorted(os.listdir('./CSVs')).index(csv_file) - 1
        lname = sorted(os.listdir('./CSVs'))[previous_index].replace('./CSVs', '').replace('.csv', '')
        leftlink = f'{lname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'\t\t<div id="left-div"><span><a href="{leftlink}" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">◄</a></span></div>\n'
    # But if the file name is 2020.08.csv [0], put the ☰ on the left side of the page:
    elif csv_file == sorted(os.listdir('./CSVs'))[0]:
        html += '\t\t<div id="left-div"><span><a href="index.html" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">☰</a></span></div>\n'
    # RIGHT SIDE ARROW ► ( or ☰ )
    # If the file name isn't today's yyyy.mm.csv [-2], or ALL.csv [-1] put the ► on the right side of the page:
    if csv_file != sorted(os.listdir('./CSVs'))[-2] and csv_file != sorted(os.listdir('./CSVs'))[-1]:
        next_index = sorted(os.listdir('./CSVs')).index(csv_file) + 1
        rname = sorted(os.listdir('./CSVs'))[next_index].replace('./CSVs', '').replace('.csv', '')
        rightlink = f'{rname}.{title1}.{title2.replace(" ", ".")}.html'
        html += f'\t\t<div id="right-div"><span><a href="{rightlink}" ' + \
                f'onmouseover="this.style.color=\'{pale_red}\'" ' + \
                f'onmouseout="this.style.color=\'{pale_blue}\'">►</a></span></div>\n'
    # But if the file name is today's yyyy.mm.csv [-2], put the ☰ on the right side of the page:
    elif csv_file == sorted(os.listdir('./CSVs'))[-2]:
        html += '\t\t<div id="right-div"><span><a href="index.html" ' + \
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

    # Write this HTML page to file
    title = title.replace(title3, title2).replace(" ", ".")
    html_file = f'./Pages/{title}.html'
    with open(html_file, mode='w', encoding='utf-8') as f:
        f.write(html)
        print(f'wrote \'{html_file}\'')

# Get the list of HTML files
pattern = re.compile(r'^(\d{4}\.\d{2})\.GREATAWAKENING\.WIN\.STICKIES\.RELOADED\.html$')
html_files = []
for html_file in os.listdir('./Pages'):
    if pattern.match(html_file):
        html_files.append(html_file)

# Sort them alphabetically:
html_files = sorted(html_files, reverse=True)

# Set a flag to handle if this is the first page:
is_first_page = True

# Define the new index.html file name:
index_html_file = './Pages/index.html'

# Generate a title for the index.html
title = f'{fire} {title1} {title2} {fire}'

# Create the HTML for the index.html page:
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
        '\t\t\t}\n\n'
html += '\t\t\th1 {\n' + \
        '\t\t\t\tfont-size: 2.5em;\n' + \
        '\t\t\t\tfont-weight: normal;\n' + \
        '\t\t\t\ttext-align: center;\n' + \
        f'\t\t\t\ttext-shadow: 0px 0px 4px {h1_shadow}, 0px 0px 4px {h1_shadow}, 0px 0px 5px {h1_shadow};\n' + \
        '\t\t\t}\n\n'
html += '\t\t\th1 a {\n' + \
        '\t\t\t\ttext-decoration: none;\n' + \
        '\t\t\t\tfont-weight: bold;\n' + \
        f'\t\t\t\tcolor: {white};\n' + \
        '\t\t\t}\n\n'
html += '\t\t\ttable {\n' + \
        '\t\t\t\twidth: 75%;\n' + \
        '\t\t\t\tmargin: 0 auto;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\ttr {\n' + \
        '\t\t\t\ttext-align: center;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\ttd {\n' + \
        '\t\t\t\tpadding: 1em;\n' + \
        f'\t\t\t\tcolor: {title_blue};\n' + \
        '\t\t\t\tfont-weight: bold;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\ttd a {\n' + \
        '\t\t\t\tcolor: inherit;\n' + \
        '\t\t\t\ttext-decoration: inherit;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\t#all {\n' + \
        '\t\t\t\ttop: 25px;\n' + \
        '\t\t\t\tleft: 2%;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\t#download {\n' + \
        '\t\t\t\ttop: 25px;\n' + \
        '\t\t\t\tright: 2%;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\t#changes {\n' + \
        '\t\t\t\ttop: 125px;\n' + \
        '\t\t\t\tright: 2%;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\t#code {\n' + \
        '\t\t\t\ttop: 225px;\n' + \
        '\t\t\t\tright: 2%;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\t#all,\n' + \
        '\t\t\t#download,\n' + \
        '\t\t\t#changes,\n' + \
        '\t\t\t#code {\n' + \
        '\t\t\t\tposition: fixed;\n' + \
        '\t\t\t\tz-index: 9999;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\t#all span,\n' + \
        '\t\t\t#download span,\n' + \
        '\t\t\t#changes span,\n' + \
        '\t\t\t#code span {\n' + \
        '\t\t\t\tfont-size:3em;\n' + \
        '\t\t\t}\n\n'
html += '\t\t\t#all span a,\n' + \
        '\t\t\t#download span a,\n' + \
        '\t\t\t#changes span a,\n' + \
        '\t\t\t#code span a {\n' + \
        '\t\t\t\ttext-decoration: none;\n' + \
        '\t\t\t}\n'
html += '\t\t</style>\n'
html += '\t</head>\n'
# BODY
html += '\t<body>\n'
html += f'\t\t<h1><a href="{gaw_url}">{title}</a></h1>\n'
html += f'\t\t<div id="all"><span><a href="{all_stickies_file}{gaw_stickies_reloaded_appendix}" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' + \
        f'onmouseout="this.style.textShadow=\'none\'">{all_link}</a></span></div>\n'
html += f'\t\t<div id="download"><span><a href="{download_url}" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' + \
        f'onmouseout="this.style.textShadow=\'none\'">{download_link}</a></span></div>\n'
html += f'\t\t<div id="changes"><span><a href="{changes_url}" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' + \
        f'onmouseout="this.style.textShadow=\'none\'">{changes_link}</a></span></div>\n'
html += f'\t\t<div id="code"><span><a href="{code_url}" ' + \
        f'onmouseover="this.style.textShadow=\'0px 0px 10px {white}\';" ' + \
        f'onmouseout="this.style.textShadow=\'none\'">{code_link}</a></span></div>\n'
# TABLE
html += '\t\t<table>\n' + \
        f'\t\t\t<tbody>\n'
# Loop to create each row for the table:
for index, html_file_name in enumerate(html_files):
    # Get the base text for this row:
    row_text = html_file_name.replace('html', '').replace('.', ' ').replace(' ', '.', 1). \
        replace(gaw, title1).strip()

    # Set alternating row colors and link:
    row_color = even_row if index % 2 == 0 else odd_row
    table_row = f'\t\t\t\t<tr style="background-color: {row_color};" ' + \
                f'onmouseover="this.style.backgroundColor=\'{row_highlight}\'; ' + \
                f'this.childNodes[0].childNodes[0].style.color=\'{pale_red}\'; ' + \
                f'this.childNodes[0].childNodes[0].style.textShadow=\'0px 0px 5px {black}\';" ' + \
                f'onmouseout="this.style.backgroundColor=\'{row_color}\'; ' + \
                f'this.childNodes[0].childNodes[0].style.color=\'{title_blue}\'; ' + \
                f'this.childNodes[0].childNodes[0].style.textShadow=\'{none}\';" ' + \
                f'onclick="window.location.href=\'./{html_file_name}\'">'
    # If this is the row for the first page
    if is_first_page:
        # If name starts with this year/month's yyyy.MM pattern, it needs Reloading icons and 'reloading..' text:
        if html_file_name.startswith(f'{year}.{month}'):
            # It needs new row_text for this row:
            reloading_row_text = html_file_name.replace('html', '').replace('.', ' ').replace(' ', '.', 1). \
                replace(gaw, title1).replace(title2, title3).strip()
            table_row += f'<td><a href="./{html_file_name}" target="_self">' + \
                         f'{reloading} {fire} {reloading_row_text} {fire} {reloading}</a></td>'
        # Otherwise it's the newest reloaded page and needs Boom! New! surrounding it:
        else:
            table_row += f'<td><a href="./{html_file_name}" target="_self">' + \
                         f'{boom} {new} {fire} {row_text} {fire} {new} {boom}</a></td>'
            is_first_page = False
    # Otherwise it just needs the file name as the title
    else:
        table_row += f'<td><a href="./{html_file_name}" target="_self">' + \
                     f'{fire} {row_text} {fire}</a></td>'
    table_row += '</tr>\n'
    # Add this row to the html:
    html += table_row
# FOOTER
html += '\t\t\t</tbody>\n' + \
        '\t\t</table>\n' + \
        '\t</body>\n' + \
        '</html>\n'

# Write the index.html:
with open(index_html_file, mode='w', encoding='utf-8') as html_file_name:
    html_file_name.write(html)
    print(f'wrote \'{index_html_file}\'')
