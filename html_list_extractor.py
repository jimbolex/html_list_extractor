#import re # Imports the regular expression library
from bs4 import BeautifulSoup

# file names
file_name_in = 'test.html'
file_name_out = 'output/list.txt'

# Reading the html file
with open(file_name_in, 'r', encoding='UTF8') as ifile:
    html = ifile.read()

# pattern = r'<li[^>]*>\s*<a[^>]*>(.*?)<\/a>\s*<\/li>'
# matches = re.findall(pattern, html)

soup = BeautifulSoup(html, 'html.parser')
texts = [a.get_text(strip=True) for a in soup.select('li > a')]

print(texts)

with open(file_name_out, 'w', encoding='utf8') as ofile:
    for line in texts:
        ofile.write(line + "\n")


