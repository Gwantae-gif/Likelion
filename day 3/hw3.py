import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
ranks = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# movies (tr들) 의 반복문을 돌리기
for rank in ranks:
    # rank 안에 a 가 있으면,
    a_tag = rank.select_one('td.info > a')


    if a_tag is not None:
        ranking = (rank.select_one('td.number').text.split(' ')[0]).strip()   # td 태그의 텍스트를 가져오기
        title = (rank.select_one('td.info > a.title.ellipsis').text).strip()                    # a 태그 사이의 텍스트를 가져오기
        singer = (rank.select_one('td.info > a.artist.ellipsis').text).strip()                      # a 태그 사이의 텍스트를 가져오기
        print(ranking, title,singer)