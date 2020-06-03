import requests
from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0'}
url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming-zongbang-2020.html"
r = requests.get(url,headers=header)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text,"lxml")
soup('div',class_="hd")
for i in soup('tr',class_="alt"):
    print("All:" + str(i.find_all("td")))
    
for i in soup('tr',class_="alt"):
    print("排名:" + str(i.find_all("td")[0].text))
    print("學校:" + str(i.find_all("td")[1].text))
    
