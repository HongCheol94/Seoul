from cgitb import text
import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입려하세요>>>>")
lastpage = pyautogui.prompt("마지막 페이지번호를 입력해 주세요")
pageNum = 1
for i in range(1, int(lastpage) * 10, 10):   
    print(f"{pageNum}페이지 입니다.==============================")  
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}") #get("") 안에 크롤링 하려는 사이트 입력
    html = response.text # response 에서 html 줌
    soup = BeautifulSoup(html, 'html.parser') # html 번역선생님으로 수프 만듦
    links = soup.select(".news_tit") # links 안에서 id(#) 값이 or class(.) 값이 ("")인 놈 한개를 찾아냄 한개를 찾을거면 select_one 여러개면 select
    for link in links:
        title = link.text #태그 안에 텍스트 요소를 가져온다
        url = link.attrs['href'] # href의 속성값을 가져온다
        print(title,url)
    pageNum = pageNum + 1
    # print(links) # ( a , b)  변수값 a안에 있는 b 형식을 가져온다 결과는 리스트로 나온다