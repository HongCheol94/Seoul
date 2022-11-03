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
search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs").click()


# 검색어 입력
search.send_keys("아이폰13")
search.send_keys(Keys.ENTER) 

# 스크롤 전 높이.
before_h = browser.execute_script("return window.scrollY")

# 무한 스크롤
while True:
        #맨 아래로 스크롤을 내린다.
        browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)

        # 스크롤 사이 페이지 로딩 시간
        time.sleep(1)

        # 스크롤 후 높이
        after_h = browser.execute_script("return window.scrollY")

        if after_h == before_h:
            break
        before_h = after_h

        #상품 정보 div
        items = browser.find_elements(By.CSS_SELECTOR, ".basicList_info_area__TWvzp")

        for item in items :
            name = item.find_elements(By.CSS_SELECTOR, ".basicList_title__VfX3c").text # text만 추출
            pirce = item.find_elements(By.CSS_SELECTOR, ".price_num__S2p_v").text
            link = item.find_elements(By.CSS_SELECTOR, ".price_num__S2p_v > a").get_attribute('href')
            print(name, pirce, link)