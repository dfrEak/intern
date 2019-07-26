from pywebcopy import save_webpage
import time
import requests
from bs4 import BeautifulSoup
import math

kwargs = {'project_name': 'tabelog'}
folder = "C:/Users/bpd-staff/Documents/Eric/download"

def getPageCount(target_url):
    response = requests.get(target_url)

    soup = BeautifulSoup(response.text, "html.parser")

    # find the restaurant count using bs4
    count = soup.find("div", "navi-count").find("strong")

    # 1 page 20 results
    restaurantCount = int(count.text.replace(',', ''))
    pageCount = math.ceil(restaurantCount/20)
    print(restaurantCount)
    print(pageCount)
    return pageCount

# from A1301 to A1331 (Tokyo area)
for area in range(1, 2):

    # web url using response
    target_url = "https://tabelog.com/tokyo/A13"+format(area, '02d')
    #pageCount = getPageCount(target_url)

    # dummy for area A1301
    #for pageList in range(51,pageCount+1):
    #for pageList in range(43,44):
    # somehow all area only can search page 1 to 60
    for pageList in range(1,61):
        save_webpage(
            url="https://tabelog.com/tokyo/A13"+format(area, '02d')+"/rstLst/"+str(pageList)+"/",
            project_folder=folder,
            **kwargs)
        # give 1s to next download
        time.sleep(1)

#########################################################
#NOTE : Before run, they will open a lot of pages
#########################################################