from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('c:/chromedriver.exe')
# mac 의 경우 /User/내거로/Documents/chromedriver

# 웹 사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초 기다림

# 쇼핑 메뉴 클릭하기
browser.find_element(By.CSS_SELECTOR, "a.nav.shop").click()
time.sleep(2)

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "input__searchInput_search_ ")
search.click()

# # 검색어 입력
# search.send_keys("아이폰13")
# search.send_keys(Keys.ENTER)