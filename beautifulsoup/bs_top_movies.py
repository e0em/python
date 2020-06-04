import requests
from bs4 import BeautifulSoup
# 設定 Agent 讓 Web Server 不認定是爬蟲
header = {'User-Agent':'Mozilla/5.0'}
url = "https://movie.douban.com/top250"
# 取得 http get 的 結果
r = requests.get(url,headers=header)
# 用 lxml 分析器分析 html 內容 並塞到Soup 裡
soup = BeautifulSoup(r.text,"lxml")
# 抓取 Tag = "div"， attrs 屬性 = class="hd"
soup('div',class_="hd")
# 抓取符合條件的 list 裡的 內容
for i in soup('div',class_="hd"):
    print(i("span",class_="title"))
    
for i in soup('div',class_="hd"):
    for j in i("span",class_="title"):
        print(j.text,end=" ")
    print()
    #print(i("span",class_="title")[0].text)
    

