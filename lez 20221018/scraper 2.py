import requests
from bs4 import BeautifulSoup
url = 'https://vbanet.eu/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("List of all the h1, h2, h3 :")
for heading in soup.find_all(["h1", "h2", "h3", "h4"]):
    print(heading.name + ' ' + heading.text.strip())

