
#! start !#

import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}&radius=25"

# ? scrap 기능을 한번에 묶어주기 

#! first function
def extract_indeed_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"pagination"})

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1] 
    return max_page

# ! second function
## indeed page를 담아서 request를 원하는 만큼 만들기
    
def extract_indeed_job(last_page):
    for page in range(last_page):
        result = requests.get(f"{URL}&start={page*LIMIT}")
        print(result.status_code)


 #! third function
 ## 각 페이지로 가서 일자리 정보를 추출해서 어딘가에 담고 모든 일자리를 반환해 주기
