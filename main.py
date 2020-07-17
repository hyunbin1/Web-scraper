#python만 가지고 url입력가능 but 더 강력한 기능을 위해 request를 사용한다. 

import requests
from bs4 import BeautifulSoup



#!  indeed 


# soup이라는 변수 만들어 주기
# BeautifulSoup(html문서, "html.parser")
#형식으로 사용해 주어야 자료를 읽을 수 있음 
indeed_soup = BeautifulSoup(indeed_resurlt.text, "html.parser")


indeed_result = requests.get('https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&l=#')

print(indeed_result)

# <Response 200> = okay라는 뜻
# 이 url의 모든 html을 다 가지고 온것.


#우리가 가져올 정보는 이 중 page의 개수이다. 
# pip install beautifulsoup4 
# html에서 정보를 추출하기에 매우 유용한 library package이다. 