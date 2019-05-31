from bs4 import BeautifulSoup as bs
import requests

#1. reqeusts야 네이버 실시간 검색 정보좀 가져와줘! 그리고 그거 글로 좀 바꿔줘!

url = 'http://www.naver.com'
response = requests.get(url).text


#2. Beautifulsoup 개게에서 resapnse라고 하는 변수안에 담긴  객체를 파싱하고, 그 결과를 다시 Beautifulsoup 객체로 반환한다.
soup = bs(response, 'html.parser')
print(type(soup))

#3. Beautifulsuoup 객체에 담긴 q변수에서 css selector를 활용해 특정정보를 가져온ㅇ다
keyword = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div')

for index, keyword in enumerate(keywords):
    print(index, keyword)