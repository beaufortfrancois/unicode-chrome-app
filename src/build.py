#!/usr/bin/env python3

import json
import urllib.request

UNICODE_DATA_URL = 'http://www.unicode.org/Public/UCD/latest/ucd/UnicodeData.txt'
UNICODE_BLOCKS_URL = 'http://www.unicode.org/Public/UCD/latest/ucd/Blocks.txt'

blocks_data = {}
unicode_data_html = ''

started_block = False

with urllib.request.urlopen(UNICODE_BLOCKS_URL) as f:
    lines = f.read().decode('utf-8').split('\n')
    for line in lines[:-1]:
        if line.startswith('#') or not line:
            continue
        data = line.split('..')
        blocks_data[data[0]] = data[1].split(';')[1].strip()

with urllib.request.urlopen(UNICODE_DATA_URL) as f:
    lines = f.read().decode('utf-8').split('\n')
    for line in lines[:-1]:
        data = line.split(';')
        if data[0] in blocks_data:
            if started_block:
                unicode_data_html += '</div>'
            unicode_data_html += '<div class="hidden" data-block="' + blocks_data[data[0]] + '">'
            started_block = True
            unicode_data_html += '<h2>' + blocks_data[data[0]] + '</h2>'
        title = data[1]
        if title == '<control>':
            title = data[10]
        unicode_data_html += '<span title="' + title + ' - U+' + data[0] + '">&#x' + data[0] + '</span>'

if started_block:
    unicode_data_html += '</div>'

with open("unicodeData.html", "w") as f:
    f.write(unicode_data_html)
