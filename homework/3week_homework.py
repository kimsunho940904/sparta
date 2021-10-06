import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

# 브라우저 종류를 명시하는 것 -> 이것을 빼고 요청하면, 응답이 오지 않는다.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86'}
# 아래 빈 칸('')을 채워보세요
# 1. 겟 방식으로 정보를 가져온다.
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
# HTML 요소가 parsing되어 있다.
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
docs = []
# 아래 빈 칸('')을 채워보세요
# 순위 곡제목 가수
for tr in trs:

    rank = tr.select_one('.number').text.split()[0]
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    artist = tr.select_one('td.info > a.artist.ellipsis').text
    print(rank,title,artist)

    # rank = tr.select_one('td.number').text[0:2].strip()
    # title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    # artist = tr.select_one('td.info > a.artist.ellipsis').text
    # print(rank, title, artist)

    doc = {
        "rank" : rank,
        "title" : title,
        "artist" : artist
    }
    # 정보가 많을수록 느려진다.
    # db.genie.insert_one(doc)

#배열을 만든 후, 한번에 넘겨주는 방법을 추천한다.
    docs.append(doc)
db.genie.insert_many(docs)

