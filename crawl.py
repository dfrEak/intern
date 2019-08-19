from bs4 import BeautifulSoup
from tools import tools
from config import config



def convertPrice(price):
    """
    convert price into 2 price
    価格を2つの価格に変換
    :param price: str
        raw price from crawling
        クロールからの生の価格
    :return: tuple(3)
        price max and min and avg
        最大値と最小値と平均
    """
    # discard "～" char at first
    # 最初に「〜」文字を破棄
    if(price[0]=="～"):
        price=price[1:]

    priceList = price.replace("￥","").replace(",","").split("～")
    if(len(priceList)==2):
        return priceList[0],priceList[1],str((int(priceList[0])+int(priceList[1]))/2.0)
    else:
        return priceList[0],priceList[0],priceList[0]

def convertHodai(hodaiBs4):
    """
    extract whether there is nomihodai or tabehodai
    飲み放題と食べ放題があるかどうかを抽出します
    :param hodaiBs4: beautifulsoup4
        additional information list
        追加情報リスト
    :return: array(2)
        information of nomihodai and tabehodai
        飲み放題と食べ放題の情報
    """
    retval=["-","-"]
    for i in range(0, len(hodaiBs4)):
        text=hodaiBs4[i].text.strip()
        if (text == "飲み放題"):
            retval[0]=text
        if (text == "食べ放題"):
            retval[1]=text
    return retval

def soupCrawl(target_file,area_code,page):
    """
    crawling the information from file
    ファイルから情報をクロールする
    :param target_file: str
        file that want to crawl
        クロールしたいファイル
    :param area_code: str
        the area code
        エリアコード
    :param page: str
        page
        ページ
    :return:
    """
    # web url using response
    # レスポンスを使ったウェブURL
    #response = requests.get(target_url)

    # local file use open
    # ローカルファイル使用オープン
    soup = BeautifulSoup(open(target_file, encoding="utf-8"), "html.parser")

    area_name = soup.find("span","list-sidebar__item-title").text.strip()

    # list
    # リスト
    nameList = []
    ekiList = []
    ratingList = []
    commentList = []
    dinnerMinList = []
    dinnerMaxList = []
    lunchMinList = []
    lunchMaxList = []
    dinnerAvgList = []
    lunchAvgList = []
    nomihodaiList = []
    tabehodaiList = []


    # extract restaurant information
    # レストラン情報の抽出
    restaurants=soup.find_all("div","list-rst__wrap js-open-new-window")

    for r in restaurants:

        # name
        # 名前
        name = r.find("a", class_="list-rst__rst-name-target cpy-rst-name")
        if (name is not None):
            nameList.append(name.text.replace("\t"," "))
        else:
            nameList.append("-")
        
        # eki
        # 駅の名前
        eki = r.find("span", class_="list-rst__area-genre cpy-area-genre")
        if (eki is not None):
            ekiList.append(eki.text.split()[0])
        else:
            ekiList.append("-")    

        # rating
        # 評価
        rating = r.find("span", class_="c-rating__val c-rating__val--strong list-rst__rating-val")
        if (rating is not None):
            ratingList.append(rating.text)
        else:
            ratingList.append("-")

        # comment
        # コメント
        comment = r.find("em", class_="list-rst__rvw-count-num cpy-review-count")
        if (comment is not None):
            commentList.append(comment.text)
        else:
            commentList.append("0")

        # dinner
        # ディナー
        dinner = r.find("span", class_="c-rating__val list-rst__budget-val cpy-dinner-budget-val")
        if (dinner is not None):
            dinnerInfo = convertPrice(dinner.text)
            dinnerMinList.append(dinnerInfo[0])
            dinnerMaxList.append(dinnerInfo[1])
            dinnerAvgList.append(dinnerInfo[2])
        else:
            dinnerMinList.append("-")
            dinnerMaxList.append("-")
            dinnerAvgList.append("-")

        # lunch
        # ランチ
        lunch = r.find("span", class_="c-rating__val list-rst__budget-val cpy-lunch-budget-val")
        if (lunch is not None):
            lunchInfo = convertPrice(lunch.text)
            lunchMinList.append(lunchInfo[0])
            lunchMaxList.append(lunchInfo[1])
            lunchAvgList.append(lunchInfo[2])
        else:
            lunchMinList.append("-")
            lunchMaxList.append("-")
            lunchAvgList.append("-")

        # nomihodai & tabehodai
        # 飲み放題と食べ放題
        hodai = r.find_all("li", class_="list-rst__search-word-item")
        hodaiResult=convertHodai(hodai)
        nomihodaiList.append(hodaiResult[0])
        tabehodaiList.append(hodaiResult[1])


    # print total information
    # 合計情報を印刷する
    result=""
    for i in range(0, len(nameList)):
        text=area_name+"\t"+area_code+"\t"+str(page)+"\t"+nameList[i]+"\t"+\
             ekiList[i]+"\t"+ratingList[i]+"\t"+commentList[i]+"\t"+\
             dinnerMinList[i]+"\t"+dinnerMaxList[i]+"\t"+\
             lunchMinList[i]+"\t"+lunchMaxList[i]+"\t"+\
             dinnerAvgList[i]+"\t"+lunchAvgList[i]+"\t"+\
             nomihodaiList[i]+"\t"+tabehodaiList[i]+"\n"
        print(text)
        result+=text

    # remove last \n
    # 最後に\nを削除
    #result=result[:-1]
    #print(result)

    # save file
    # ファイルを保存
    tools.save(config.config['CRAWL']['FILENAME'],result)

    # sleep 1 second
    # 次のダウンロードに1秒を与える
    #time.sleep(1)


def extractWebPage():
    """
    web page extraction
    Webページの抽出
    :return: -
    """
    # getting folder path from config file
    # 設定ファイルからフォルダパスを取得する
    folder = config.config['DOWNLOAD']['FOLDER']

    # from A1301 to A1331 (Tokyo area)
    # A1301から A1331まで（東京エリア）
    for area in range(1, 32):
        area_code = "A13"+format(area, '02d')

        # somehow all area only can search page 1 to 60
        # A1331 only has 406 results (21 pages)
        # どういうわけか全域で1〜60ページしか検索できない
        # A1331の検索結果は406個です（21ページ）
        for page in range(1, 61):
            target_file = folder + "/" + area_code + "_" + str(page) + ".html"

            print("start extracting "+target_file)

            # some areas have results below 1200 (60 pages)
            # 一部の地域では1200を下回る結果が出ています（60ページ）
            #soupCrawl(target_file, area_code, page)
            try:
                soupCrawl(target_file, area_code, page)
            except FileNotFoundError:
                print(target_file+" not found")




##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

savedFile = config.config['CRAWL']['FILENAME']
tools.clearFile(savedFile)
extractWebPage()
