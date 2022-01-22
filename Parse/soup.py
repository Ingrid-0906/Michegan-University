# Imports
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# A list to hold the data
my_dict = list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve the <span> tag
for link in soup.find_all('span'):
	# Extracting the 'middle'
	words = link.get_text()
	# Appending in my_dict list
	my_dict.append(int(words[0:]))
	
# Printing
print(sum(my_dict))
