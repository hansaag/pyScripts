import requests
from bs4 import BeautifulSoup
import urllib3
import json

bildeDict = {}
bildeDict['plasser'] = []
bildeMangler = []


badefil = open("/mnt/d/python_scripts/BathingLocations.JSON", "r")
innData = json.load(badefil)
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent" : USER_AGENT}
i = 0



for p in innData['plasser']:
    query = p['name'] + "+bade"
    query.replace(' ', '+')
    url = f"https://images.search.yahoo.com/search/images;_ylt=AwrJ7Jpf.J5ejO0AwAFXNyoA;_ylu=X3oDMTB0N2Noc21lBGNvbG8DYmYxBHBvcwMxBHZ0aWQDBHNlYwNwaXZz?p={query}&fr2=piv-web"
    url2 = f"https://www.bing.com/images/search?q={query}&go=S%C3%B8k&qs=ds&form=QBIR&scope=images"
    response = requests.get(url2, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        #kan bruke saltvann/ikke for bildeklassifiseringen
        try:
            g = soup.find_all('img', class_= "mimg")[0]    
        
            items = {"img_src" : g['src']}
            p.update(items)
            bildeDict['plasser'].append(p)
            print(i)
        except IndexError:
            i+=1
            bildeMangler.append(p['name'])
            continue
        
    
    i+=1
    


with open('bilder.JSON', 'w') as outfile:
    json.dump(bildeDict, outfile, indent = 4)


print(len(bildeMangler))

    





