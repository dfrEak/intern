import requests
from bs4 import BeautifulSoup

target_file = 'C:/Users/staff/work/eric/downloads/tabelog/tabelog.com/tokyo/A1301/index.html'
#response = requests.get(target_url)


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
for i in range(0, len(name)):
    print(name[i].text+"\t"+rating[i].text+"\t"+dinner[i].text+"\t"+lunch[i].text)