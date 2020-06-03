import requests
from bs4 import BeautifulSoup
header = {'User-Agent':'Mozilla/5.0'}
url = "https://movie.douban.com/top250"
r = requests.get(url,headers=header)
soup = BeautifulSoup(r.text,"lxml")
soup('div',class_="hd")
for i in soup('div',class_="hd"):
    i("span",class_="title")[0]
    
# OUT: <span class="title">肖申克的救赎</span>
# OUT: <span class="title">霸王别姬</span>
# OUT: <span class="title">阿甘正传</span>
# OUT: <span class="title">这个杀手不太冷</span>
# OUT: <span class="title">美丽人生</span>
# OUT: <span class="title">泰坦尼克号</span>
# OUT: <span class="title">千与千寻</span>
# OUT: <span class="title">辛德勒的名单</span>
# OUT: <span class="title">盗梦空间</span>
# OUT: <span class="title">忠犬八公的故事</span>
# OUT: <span class="title">海上钢琴师</span>
# OUT: <span class="title">楚门的世界</span>
# OUT: <span class="title">三傻大闹宝莱坞</span>
# OUT: <span class="title">机器人总动员</span>
# OUT: <span class="title">放牛班的春天</span>
# OUT: <span class="title">星际穿越</span>
# OUT: <span class="title">大话西游之大圣娶亲</span>
# OUT: <span class="title">熔炉</span>
# OUT: <span class="title">疯狂动物城</span>
# OUT: <span class="title">无间道</span>
# OUT: <span class="title">龙猫</span>
# OUT: <span class="title">教父</span>
# OUT: <span class="title">当幸福来敲门</span>
# OUT: <span class="title">怦然心动</span>
# OUT: <span class="title">触不可及</span>
for i in soup('div',class_="hd"):
    i("span",class_="title")[0].text
    

# OUT: '肖申克的救赎'
# OUT: '霸王别姬'
# OUT: '阿甘正传'
# OUT: '这个杀手不太冷'
# OUT: '美丽人生'
# OUT: '泰坦尼克号'
# OUT: '千与千寻'
# OUT: '辛德勒的名单'
# OUT: '盗梦空间'
# OUT: '忠犬八公的故事'
# OUT: '海上钢琴师'
# OUT: '楚门的世界'
# OUT: '三傻大闹宝莱坞'
# OUT: '机器人总动员'
# OUT: '放牛班的春天'
# OUT: '星际穿越'
# OUT: '大话西游之大圣娶亲'
# OUT: '熔炉'
# OUT: '疯狂动物城'
# OUT: '无间道'
# OUT: '龙猫'
# OUT: '教父'
# OUT: '当幸福来敲门'
# OUT: '怦然心动'
# OUT: '触不可及'
