import re

with open('bible.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    # remove all numbers and colons 
    text = re.sub(r'[0-9:.,;!?/()$%@*#&^-_=+\'\"\\-]', '', text)
    # remove all newlines
    text = text.replace('\n', '')
    # remove all tabs
    text = text.replace('\t', '')

# save to file
with open('bible_formatted.txt', 'w') as file:
    file.write(text)