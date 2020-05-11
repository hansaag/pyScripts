import requests
from bs4 import BeautifulSoup
import urllib3
import json

bildeDict = {}
bildeDict['plasser'] = []
bildeMangler = []


badefil = open("/mnt/d/python_scripts/oppdaterte_badeplasser.JSON", "r")
innData = json.load(badefil)
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}
i = 0
bing = "https://www.bing.com"
yahoo = "https://images.search.yahoo.com/"


for p in innData:
    query = p['name'] 
    query.replace(' ', '+')
    url = f"https://images.search.yahoo.com/search/images;_ylt=AwrJ7Jpf.J5ejO0AwAFXNyoA;_ylu=X3oDMTB0N2Noc21lBGNvbG8DYmYxBHBvcwMxBHZ0aWQDBHNlYwNwaXZz?p={query}&fr2=piv-web"
    url2 = f"https://www.bing.com/images/search?q={query}&go=S%C3%B8k&qs=ds&form=QBIR&scope=images"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        #kan bruke saltvann/ikke for bildeklassifiseringen
        try:
            g = soup.find_all('a')[1]
            print(g)
            pic_href = soup.select(g["href"])
            
            print(pic_href)
            #soup = BeautifulSoup(response.content, pic_href)
            

        
            items = {"img_src" : g['src']}
            p.update(items)
            bildeDict['plasser'].append(p)
            print(i)
        except IndexError:
            i+=1
            bildeMangler.append(p['name'])
            continue
        
    
    i+=1
    if (i == 10):
        break
    


with open('bilder_yahoo.JSON', 'w') as outfile:
    json.dump(bildeDict, outfile, indent = 4)


print(len(bildeMangler))

    




href="/images/search?view=detailV2&ccid=BKgA0CNk&id=0CEBE8C0EAF7B5A314EECAF3F0495668BFA86051&thid=OIP.BKgA0CNkE7xTZQn1YEfZdgAAAA&mediaurl=https%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2fthumb%2f9%2f96%2fAksdalsvatnet.jpg%2f220px-Aksdalsvatnet.jpg&exph=147&expw=220&q=aksdalsvatnet&simid=608046976611845316&selectedIndex=0"
