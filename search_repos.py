import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
url_list = ['https://github.com/vinta/awesome-python']
for link in url_list:
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "lxml")
    query=str(input("Query? "))
    extlist = set()
    intlist = set()
    
    for a in soup.findAll("a", attrs={"href":True}):
        if len(a['href'].strip()) > 1 and a['href'][0] != '#' and 'javascript:' not in a['href'].strip() and 'mailto:' not in a['href'].strip() and 'tel:' not in a['href'].strip():
            if 'http' in a['href'].strip() or 'https' in a['href'].strip():
                if urlparse(link).netloc.lower() in urlparse(a['href'].strip()).netloc.lower():
                    intlist.add(a['href'])
                else:
                    extlist.add(a['href'])
            else:
                intlist.add(a['href'])
    com = list(val for val in intlist)
    for i in range(len(com)):
        if query in com[i]:
            print("Output: ",com[i])
    