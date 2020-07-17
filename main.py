
#! start !#

#python만 가지고 url입력가능 but 더 강력한 기능을 위해 request를 사용한다. 
## pip install requests ##

# html에서 정보를 추출하기에 매우 유용한 library package이다. 
## pip install beautifulsoup4 ##

import requests
from bs4 import BeautifulSoup

# ! ruquset & BeautifulSoup 변수 만들어 주기

# 1. request 변수

indeed_result = requests.get('https://kr.indeed.com/jobs?q=python%2C+%ED%8C%8C%EC%9D%B4%EC%8D%AC&l=&ts=1594971727745&rq=1&rsIdx=0&fromage=last&newcount=912')



# 2. BeautifulSoup 변수
# 아래 형식으로 사용해 주어야 자료를 읽을 수 있음 
## 변수 =  BeautifulSoup(html문서, "html.parser") ##
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# 이제부터 데이터를 수집할때 indeed_soup. 뒤에 원하는 자료를 입력하면 된다. 

# <Response 200> = okay라는 뜻
# 이 url의 모든 html을 다 가지고 온것.



# ? 우리가 가져올 정보는 이 중 page의 개수이다. 
# pagination = 페이지 목록 
# pages = 리스트
# ? span만 출력하기 = 페이지 수

pagination = indeed_soup.find("div", {"class":"pagination"})
pages = pagination.find_all('a')


#span 리스트 만들기
spans = []
for link in pages:
    spans.append(link.find("span"))

#마지막 span 빼주기
# -1은 마지막에서부터 시작해서 첫 item을 나타낸다.
spans = spans[:-1]
print(spans)
