#import requests
from bs4 import BeautifulSoup
from tools import tools
import time

folder = "C:/Users/bpd-staff/Documents/Eric/download"

def soupCrawl(target_file):
    # web url using response
    #response = requests.get(target_url)

    # local file use open
    soup = BeautifulSoup(open(target_file), "html.parser")

    # list
    nameList = []
    ratingList = []
    dinnerList = []
    lunchList = []

    # extract restaurant information
    restaurants=soup.find_all("div","list-rst__wrap js-open-new-window")



    for r in restaurants:
        #another method using find
        #example
        #if soup.find("div", {"class": "info"}) is not None:
        #    print("Tag Found")

        # name
        name = r.find_all("a", class_="list-rst__rst-name-target cpy-rst-name")
        if (len(name) == 1):
            nameList.append(name[0].text)
        else:
            nameList.append("-")

        # rating
        rating = r.find_all("span", class_="c-rating__val c-rating__val--strong list-rst__rating-val")
        if (len(rating) == 1):
            ratingList.append(rating[0].text)
        else:
            ratingList.append("-")

        # dinner
        dinner = r.find_all("span", class_="c-rating__val list-rst__budget-val cpy-dinner-budget-val")
        if (len(dinner) == 1):
            dinnerList.append(dinner[0].text)
        else:
            dinnerList.append("-")

        # lunch
        lunch = r.find_all("span", class_="c-rating__val list-rst__budget-val cpy-lunch-budget-val")
        if (len(lunch) == 1):
            lunchList.append(lunch[0].text)
        else:
            lunchList.append("-")

    # looping print
    result=""
    print("name "+str(len(nameList)))
    print("rating "+str(len(ratingList)))
    print("dinner "+str(len(dinnerList)))
    print("lunch "+str(len(lunchList)))

    for i in range(0, len(nameList)):
        #print(str(nameList[i])+"\t"+str(ratingList[i])+"\t"+str(dinnerList[i])+"\t"+str(lunchList[i])+"\n")
        result+=nameList[i]+"\t"+ratingList[i]+"\t"+dinnerList[i]+"\t"+lunchList[i]+"\n"

    # remove last \n
    #result=result[:-1]
    #print(result)

    # save file
    tools.save("../result.txt",result)

    # sleep 1 second
    #time.sleep(1)


# dummy for area A1301 first page
target_file = folder+"/tabelog/tabelog.com/tokyo/A1301/index.html"
soupCrawl(target_file)

# dummy for area A1301 2nd page to 60th page
for pageList in range(2, 61):
#for pageList in range(3, 4):
    target_file = folder+"/tabelog/tabelog.com/tokyo/A1301/rstLst/"+str(pageList)+"/index.html"
    print(pageList)
    soupCrawl(target_file)

