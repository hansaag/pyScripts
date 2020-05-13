from selenium import webdriver
import time 
from collections import defaultdict


browser = webdriver.Chrome("/mnt/d/python_scripts/chromedriver.exe")


#badetassen
plasser = defaultdict(int)
browser.get('https://badetassen.no')

i = 0
e = 0


while 1:
    time.sleep(2)
    try:
        region = browser.find_elements_by_css_selector('ul')[i]
        region.click
    except IndexError as error:
        print(error)
        break
    
    while 1:

        time.sleep(1)
        try:
            plass = browser.find_elements_by_class_name('area-list-item')[e]
            plass.click()
            time.sleep(1)
            browser.execute_script("window.history.go(-1)")
            
            e+=1
        except IndexError as error:
            break

    i+=1
    time.sleep(1)
