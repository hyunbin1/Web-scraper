
#! indeed와 stackoverflow의 구직 자료들 한눈에 보기
#! start

#? indeed #?
# indeed page가 몇 페이지 까지 있는지 알기


## 1. indeed page 함수 작동시키기 ##
from indeed import extract_indeed_page, extract_indeed_job

last_page = extract_indeed_page()
 
## 2. request 원하는 만큼 만들기 ##
# indeed페이지를 2번째 함수에 넣어줘서 원하는 만큼 request 해주기
extract_indeed_job(last_page)

 ## 3. 각 페이지로 가서 일자리 정보를 추출해서 어딘가에 담고 모든 일자리를 반환해 주기
