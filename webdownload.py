import time
import requests
from bs4 import BeautifulSoup
import math
from urllib.request import urlopen
from config import config
from pathlib import Path


def getPageCount(target_url):
    """
    get page count by calculate all restaurant divided by 20
    すべてのレストランを20で割って計算してページ数を取得する
    :param target_url: str
        url that we want to download
        ダウンロードしたいURL
    :return: int
        the number of pages
        ページ数
    """
    response = requests.get(target_url)

    soup = BeautifulSoup(response.text, "html.parser")

    # find the restaurant count using bs4
    # bs4を使ってレストランの数を探す
    count = soup.find("div", "navi-count").find("strong")

    # 1 page 20 results
    # 1ページ20件
    restaurantCount = int(count.text.replace(',', ''))
    pageCount = math.ceil(restaurantCount/20)
    print(restaurantCount)
    print(pageCount)
    return pageCount

def getWebPage(target_url,name):
    """
    download web page only
    Webページのみをダウンロードする
    :param target_url: str
        url that we want to download
        ダウンロードしたいURL
    :param name: str
        filename we want to save
        保存したいファイル
    :return: -
    """
    html = urlopen(target_url).read().decode('utf8')
    with open(name, 'w', encoding="utf-8") as fid:
        fid.write(html)
    print("success save : "+target_url)

def downloadTokyo():
    """
    download function
    ダウンロード機能
    :return: -
    """
    # getting folder path from config file
    # 設定ファイルからフォルダパスを取得する
    folder = config.config['DOWNLOAD']['FOLDER']

    # from A1301 to A1331 (Tokyo area)
    # A1301から A1331まで（東京エリア）
    for area in range(10, 32):

        # web url using response
        # レスポンスを使ったウェブURL
        area_code = "A13"+format(area, '02d')
        target_url = "https://tabelog.com/tokyo/"+area_code
        pageCount = getPageCount(target_url)
        lastPage=61
        if(pageCount<60):
            lastPage= pageCount + 1

        # somehow all area only can search page 1 to 60
        # どういうわけか全域で1〜60ページしか検索できない
        for page in range(1, lastPage):
            url="https://tabelog.com/tokyo/A13" + format(area, '02d') +"/rstLst/" + str(page) + "/"

            #getFullWeb(url,folder)
            getWebPage(url, str(Path(folder) / (area_code + "_" + str(page) + ".html")))

            # give 1s to next download
            # 次のダウンロードに1秒を与える
            time.sleep(1)


##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

downloadTokyo()