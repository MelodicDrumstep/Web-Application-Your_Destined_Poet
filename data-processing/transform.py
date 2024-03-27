import re

with open('output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('output.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if line.startswith('诗人生卒信息'):
            match = re.search(r'\d+', line)
            if match is not None:
                year = match.group()
                line = '诗人生卒信息: ' + year + '\n'
            else:
                line = '诗人生卒信息: None\n'
        f.write(line)