from selenium import webdriver
import time 
from collections import defaultdict


browser = webdriver.Chrome("/Users/Hansi/Desktop/pyScripts/chromedriver")


#badetassen
plasser = defaultdict(int)
browser.get('https://badetassen.no')

i = 1
e = 1


while 1:
    time.sleep(2)
    try:
        region = browser.find_element_by_css_selector("div > div > div > div.region-filter > ul > li:nth-child(%d) > a"%i).click()
        #bør bruke wait()
        i+=1

        while 1:

            time.sleep(1)
            try:#må fikse selector
                plass = browser.find_elements_by_class_name("div > div > div > div.area-list.Grid.Grid-center.Grid--cols-3 > div:nth-child(%d) > a"%e).click()
                
                browser.execute_script("window.history.go(-1)")
                
                e+=1
            except Exception as error:
                break

    
       
    except Exception as error:
        print(error)
        break
