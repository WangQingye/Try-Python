#coding=utf-8
import sys
import datetime
import requests
from bs4 import BeautifulSoup
# reload(sys)
# sys.setdefaultencoding('utf-8')
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

#
# header = {
#     'Content-Type': 'text/html;charset=utf8',
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) App leWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/9537.53'
# }

d1 = datetime.datetime(2017, 1, 7)
d2 = datetime.datetime.now()
day = str((d2-d1).days)

def insert(str, add):
    str = str[:len(str)-1] + add
    return str
"""
天气
"""
res = requests.get("http://www.weather.com.cn/weather1d/101270101.shtml")
res.encoding = "utf-8"
sample = res.text
soup = BeautifulSoup(sample, 'html.parser')
ziwaixian = insert(soup.select('.li1')[0].p.text, "噢~")
ganmao = insert(soup.select('.li2')[0].p.text, "哟~")
tianqi = soup.select('.li3')[0].a.span.text
chuanyi = soup.select('.li3')[0].a.p.text
yundong = soup.select('.li5')[0].span.text + " 。所以" + insert(soup.select('.li5')[0].p.text, "噢~")
wuran = soup.select('.li6')[0].span.text
wuranjianyi = insert(soup.select('.li6')[0].p.text, "哟~")
#timeSource = soup.select('.time-source')[0].contents[0].strip()
temLow = soup.select('.tem')[0].find_all('span')[0].text + "℃。"
temHigh = soup.select('.tem')[1].find_all('span')[0].text + "℃"

"""
情话
"""
# res1 = requests.get("http://www.binzz.com/yulu2/3588.html")
# res1.encoding = "gbk"
# sample1 = res1.text
# soup1 = BeautifulSoup(sample1, 'html.parser')
# qinghua = soup1.select('#content')[0].find_all("p")[(d2-d1).days - 65].text.split("：")[1]

"""
星座
"""
res2 = requests.get("http://astro.sina.com.cn/fate_day_Pisces/")
res2.encoding = "utf-8"
sample2 = res2.text
soup2 = BeautifulSoup(sample2, 'html.parser')
xingzuo = soup2.select('div.words')[0].find_all("p")[3].text


"""
笑话
"""

# res3 = requests.get("http://www.jokeji.cn/jokehtml/ym/2017032820112278.htm")
# res3.encoding = "gbk"
# sample3 = res3.text
# soup3 = BeautifulSoup(sample3, 'html.parser')
# xiaohua = soup3.select('#text110')[0].find_all("p")[(d2-d1).days - 111].text[2:]


"""
歌曲
"""

browser = webdriver.PhantomJS()
browser.get('http://music.163.com/#/playlist?id=688383300')
browser.switch_to.frame('contentFrame')
aList = browser.find_element_by_tag_name('tbody')
a = aList.find_elements_by_tag_name('a')
b = aList.find_elements_by_tag_name('b')
c = a[0].get_attribute('href'), b[0].text + " - " + a[2].text
songName = b[0].text
songSinger = a[2].text
songHref = a[0].get_attribute('href')
print (c)

# res6 = requests.get("http://www.lizhi.fm/233233/")
# res6.encoding = "utf-8"
# sample6 = res6.text
# soup6 = BeautifulSoup(sample6, 'html.parser')
# fmUrl = "http://www.lizhi.fm" + soup6.find_all("a", attrs={"data-band": "233233"})[0]["href"]
# fmName = soup6.find_all("a", attrs={"data-band": "233233"})[0].select("p.audioName")[0].text

id_ = "music.163.com/#/song?id=37196629"
casablanca = "Casablanca"
content1= "亲爱的<b>李琳垚</b>:" + "<br>" +\
      "    早上好，今天是你跟<b>王清野</b>在一起的<b>第" + day +"天</b>噢~" + "<br><br>" +\
      "<b>接下来为您播报今天成都的天气情况：</b>" + "<br>" + \
      "    整体温度：" + temHigh + "～" + temLow + tianqi + "噢~所以" + chuanyi + "不要忘记啦！" + "<br>" +\
      "    感冒指数：" + ganmao + "<br>" +  \
      "    运动指数：今天的运动情况是" + yundong + "<br>" + \
      "    空气污染：程度" + wuran + "。" + "所以" + wuranjianyi + "<br>" + \
      "    紫外线指数：" + ziwaixian + "<br><br>" + \
      "<b>今日双鱼座的星座运势是：</b>" + "<br>" + \
      "    " + xingzuo[2:] + "<br><br>" + \
      "<b>今日歌曲一首</b>：<a href=" + songHref + ">" + songName + " - " + songSinger +"</a><br><br>" + \
      "<b>最后也是最重要的</b>：" + "<br>"
