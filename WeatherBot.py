##########################
# Twitterで高知県中部のデータを定期的に呟くプログラム
# サーバはUTCのため、JST向けの編集内容。JSTの設定とTweetをオフにしたら本番。
# やりたいこと
# 毎時実行のため、時間によって弾く(1日4回のツイート)
##########################

import re
import key
import nowtime
import urllib.request
from bs4 import BeautifulSoup

Tarm1 = 6
Tarm2 = 13
Tarm3 = 24

print("Server at: " + str(nowtime.getNow()))
jst = nowtime.getJst()
print("JST    at: " + str(jst))

hour = int(jst.hour)
if hour != Tarm1:
    if hour != Tarm2:
        hour += 24
        if hour != Tarm3:
            print("指定時間外:" + str(hour - 24) + "時")
            exit()
            # 指定したTarmの自国でなければプログラムを終了する

url = "https://www.jma.go.jp/jp/yoho/344.html"
# URLにアクセスする htmlが帰ってくる → <html><head><title>...
html = urllib.request.urlopen(url)
# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")
table = soup.find("table", id="forecasttablefont", class_="forecast")
rate = table.find_all("td", {"align": "right"})
cell = table.find("td", class_="max")
# 最初に見つかった<div class="font-size-clear">の下の<td>を全て探す
for i in range(8):
    print(rate[i].string)
maxium = re.sub(r'\D', '', cell.string)
# JMAからデータ取得終わり

# Tweet準備
span = ["00-06: ", "06-12: ", "12-18: ", "18-24: "]
today = str(jst.month) + "月" + str(jst.day) + "日"
tommorow = str(jst.month) + "月" + str(jst.day+1) + "日"
text = "高知中部の降水確率は\n" + today + " 最高気温:" + maxium + "度\n"
s = int(hour/6)
for i in range(s, 4):
    text += "   " + span[i] + rate[i].string + "\n"
if s != 0:
    text += tommorow + "\n"
    for i in range(0, s):
        text += "   " + span[i] + rate[4+i].string + "\n"
text += "です. (データ取得: " + str(hour) + "時)"
try:
    key.tw.statuses.update(status=text) #Twitterに投稿
    print("ツイート完了 {\n" + text + "\n}")
except:
    print("ツイートできませんでした")


print("Finish at: " + str(nowtime.getJst()))
