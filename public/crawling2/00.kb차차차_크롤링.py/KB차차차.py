from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 브라우저 생성
browser = webdriver.Chrome('c:/chromedriver.exe')
# mac 의 경우 /User/내거로/Documents/chromedriver

# 웹 사이트 열기
browser.get('https://www.kbchachacha.com/')
browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초 기다림

#살때 메뉴 들어가기
browser.find_element(By.CSS_SELECTOR, ".navigation-global__link").click()

# 스크롤 전 높이.
before_h = browser.execute_script("return window.scrollY")

