# Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

my_dict = list()
clock = 0
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

def parse(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	return tags

while clock < count:
    print('Retrieving: ', url)
    tags = parse(url)
    for i, item in enumerate(tags):
        if i == pos - 1:
            url = item.get('href', None)
            name = item.contents[0]
            break
        else:
            continue
    clock+=1


print('Retrieving: ', url)
