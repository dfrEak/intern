#import requests
from bs4 import BeautifulSoup
from tools import tools
import time

folder = "C:/Users/bpd-staff/Documents/Eric/download"

# convert price into 2 price
# 価格を2つの価格に変換
def convertPrice(price):
    # discard "～" char at first
    # 最初に「〜」文字を破棄
    if(price[0]=="～"):
        price=price[1:]

    priceList = price.replace("￥","").replace(",","").split("～")
    if(len(priceList)==2):
        return priceList[0],priceList[1]
    else:
        return priceList[0],priceList[0]


def soupCrawl(target_file):
    # web url using response
    # レスポンスを使ったウェブURL
    #response = requests.get(target_url)

    # ローカルファイル使用オープン
    soup = BeautifulSoup(open(target_file, encoding="utf-8"), "html.parser")

    # list
    # リスト
    nameList = []
    ratingList = []
    dinnerList = []
    lunchList = []
    dinnerMinList = []
    dinnerMaxList = []
    dinnerAvgList = []
    lunchAvgList = []


    # extract restaurant information
    # レストラン情報の抽出
    restaurants=soup.find_all("div","list-rst__wrap js-open-new-window")

    for r in restaurants:

        # name
        # 名前
        name = r.find("a", class_="list-rst__rst-name-target cpy-rst-name")
        if (name is not None):
            nameList.append(name.text)
        else:
            nameList.append("-")

        # rating
        # 評価
        rating = r.find("span", class_="c-rating__val c-rating__val--strong list-rst__rating-val")
        if (rating is not None):
            ratingList.append(rating.text)
        else:
            ratingList.append("-")

        # dinner
        # ディナー
        dinner = r.find_all("span", class_="c-rating__val list-rst__budget-val cpy-dinner-budget-val")
        if (dinner is not None):
            dinnerList.append(dinner.text)
        else:
            dinnerList.append("-")

        # lunch
        # ランチ
        lunch = r.find_all("span", class_="c-rating__val list-rst__budget-val cpy-lunch-budget-val")
        if (lunch is not None):
            lunchList.append(lunch.text)
        else:
            lunchList.append("-")

    # print total information
    # 合計情報を印刷する
    result=""
    print("name "+str(len(nameList)))
    print("rating "+str(len(ratingList)))
    print("dinner "+str(len(dinnerList)))
    print("lunch "+str(len(lunchList)))

    for i in range(0, len(nameList)):
        #print(str(nameList[i])+"\t"+str(ratingList[i])+"\t"+str(dinnerList[i])+"\t"+str(lunchList[i])+"\n")
        result+=nameList[i]+"\t"+ratingList[i]+"\t"+dinnerList[i]+"\t"+lunchList[i]+"\n"

    # remove last \n
    # 最後に\nを削除
    #result=result[:-1]
    #print(result)

    # save file
    # ファイルを保存
    tools.save("../result.txt",result)

    # sleep 1 second
    # 次のダウンロードに1秒を与える
    #time.sleep(1)



def extractWebFull():
    # area A1301 first page
    # エリアA1301の最初のページ
    target_file = folder+"/tabelog/tabelog.com/tokyo/A1301/index.html"
    soupCrawl(target_file)

    # area A1301 2nd page to 60th page
    # エリアA1301 2〜60ページ
    for pageList in range(2, 61):
        target_file = folder+"/tabelog/tabelog.com/tokyo/A1301/rstLst/"+str(pageList)+"/index.html"
        print(pageList)
        soupCrawl(target_file)

def extractWebPage():
    # from A1301 to A1331 (Tokyo area)
    # A1301から A1331まで（東京エリア）
    for area in range(1, 2):
        area_code = "A13"+format(area, '02d')
        # somehow all area only can search page 1 to 60
        # どういうわけか全域で1〜60ページしか検索できない
        for page in range(1, 2):
            target_file = folder + "/" + area_code + "_" + str(page) + ".html"
            soupCrawl(target_file)
            #try:
                #soupCrawl(target_file)
            #except:
                #print(target_file+" not found")




##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


extractWebPage()