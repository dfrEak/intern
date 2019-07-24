#import requests
from bs4 import BeautifulSoup
from tools import tools

def soupCrawl(target_file):
    # web url using response
    #response = requests.get(target_url)

    # local file use open
    soup = BeautifulSoup(open(target_file), "html.parser")

    # name
    name=soup.find_all("a", class_="list-rst__rst-name-target cpy-rst-name")

    # rating
    rating=soup.find_all("span", class_="c-rating__val c-rating__val--strong list-rst__rating-val")

    # dinner
    dinner=soup.find_all("span", class_="c-rating__val list-rst__budget-val cpy-dinner-budget-val")

    # lunch
    lunch=soup.find_all("span", class_="c-rating__val list-rst__budget-val cpy-lunch-budget-val")

    # looping print
    result=""
    print(len(name))
    for i in range(0, len(name)):
        print(name[i].text+"\t"+rating[i].text+"\t"+dinner[i].text+"\t"+lunch[i].text+"\n")
        result+=name[i].text+"\t"+rating[i].text+"\t"+dinner[i].text+"\t"+lunch[i].text+"\n"

    # remove last \n
    result=result[:-1]
    #print(result)

    #save file
    tools.save("../result.txt",result)



# dummy for area A1301 first page
target_file = 'C:/Users/staff/work/eric/downloads/tabelog/tabelog.com/tokyo/A1301/index.html'
soupCrawl(target_file)

# dummy for area A1301 2nd page to 50th page
for pageList in range(2, 51):
    target_file = "C:/Users/staff/work/eric/downloads/tabelog/tabelog.com/tokyo/A1301/rstLst/"+str(pageList)+"/index.html"
    print(pageList)
    soupCrawl(target_file)

