
#! start !#

#python만 가지고 url입력가능 but 더 강력한 기능을 위해 request를 사용한다. 
## pip install requests ##

# html에서 정보를 추출하기에 매우 유용한 library package이다. 
## pip install beautifulsoup4 ##

import requests
from bs4 import BeautifulSoup
# ! request & BeautifulSoup 변수 만들어 주기

# 1. request 변수

indeed_result = requests.get('https://kr.indeed.com/jobs?q=python&limit=50&radius=25')



# 2. BeautifulSoup 변수
# 아래 형식으로 사용해 주어야 자료를 읽을 수 있음 
## 변수 =  BeautifulSoup(html문서, "html.parser") ##
indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# 이제부터 데이터를 수집할때 indeed_soup. 뒤에 원하는 자료를 입력하면 된다. 

# <Response 200> = okay라는 뜻
# 이 url의 모든 html을 다 가지고 온것.



# ? 우리가 가져올 정보는 이 중 page의 개수이다. 
# pagination = 페이지 목록 
# ! links = anchor(앵커 = 페이지 틀) = 리스트 만들기 
# ? pages 만 출력하기 = 페이지 수

pagination = indeed_soup.find("div", {"class":"pagination"})
links = pagination.find_all('a')


# pages 리스트 만들기
# anchor가 있고, 이 요소안에 다른요소가 있고 그 요소에 string이 오직 하나 있다면
# 그냥 anchor에서 string method를 실행하면 된다. beautiful soup이 알아서 찾아줌


pages = []
#마지막 span 빼주기 = ##[-1]## 넣어주기 
# ! -1은 마지막에서부터 시작해서 첫 item을 나타낸다.
# 나중에 pages[:-1]을 해주게 되면 리스트에서 문자열을 숫자열로 바꿀때 
# 페이지 수  추출 전이기 때문에 다른 부분이 숫자열이 아니라고 에러가 뜬다 
for link in links[:-1]:
    # ? 텍스트만 가져오기 = 마지막에 string 넣어주기
    ## pages.append(link.find("span").string) ## 
    ## == pages.append(link.string) = anchor에 들어있던 리스트에서 문자열만 가져오기 ##
    # ? 페이지 숫자를 문자열로 가져옴 = 문자열을 숫자열로 바꿔주기
    ## pages.append(link.string) ##
    pages.append(int(link.string))

# ? 페이지 수 중에서 가장 큰 수 찾기
max_page = pages[-1] 

# ? 페이지를 계속해서 request 하는 방법을 찾아야 된다. 
# ? 5개의 request를 만들어야 됨.
# range 함수 사용하기

for n in range(max_page):     
    # '0' = 첫 페이지
    # [-1]때문에 마지막 페이지 포함 안됨
    # ? range의 현재 값을 indeed에서 가져온 요소 개수만큼 곱해주기
    print(f"start={n*10}")

    




 #! 2. request를 원하는 만큼 만들기
# 최대 페이지 수 받기
def indeed_job(last_page):
    for page in range(last_page)
    print(f"start={page")








