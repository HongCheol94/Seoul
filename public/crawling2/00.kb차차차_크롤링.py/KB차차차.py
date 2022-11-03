import requests
from bs4 import BeautifulSoup
 
 #차량정보
# if __name__ == "__main__":
#     url = 'https://www.kbchachacha.com/public/car/detail.kbc?carSeq=23642332'
#     response = requests.get(url)
 
#     if response.status_code == 200:
#         html = response.text
#         soup = BeautifulSoup(html, 'lxml')
        
#         # html에서 dl 태그 중 class이름이 detail-info01인 태그를 찾아라
#         detail_info01 = soup.find('div','detail-info01')
#         print(detail_info01)
 
#     else : 
#         print(response.status_code)

 #차량이미지
if __name__ == "__main__":
    url = 'https://www.kbchachacha.com/public/car/detail.kbc?carSeq=23642332'
    response = requests.get(url)
 
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        
        # html에서 dl 태그 중 class이름이 detail-info01인 태그를 찾아라
        detail_info01 = soup.find('div','slide-img')
        print(detail_info01)
 
    else : 
        print(response.status_code)






# from tokenize import tabsize
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # 브라우저 생성
# browser = webdriver.Chrome('c:/chromedriver.exe')
# # mac 의 경우 /User/내거로/Documents/chromedriver

# # 웹 사이트 열기
# browser.get('https://www.kbchachacha.com/')
# browser.implicitly_wait(10) # 로딩이 끝날 때까지 10초 기다림

# #탭 닫기
# tabs = browser.window_handles
# print(tabs)
# #살때 메뉴 들어가기
# browser.find_element(By.CSS_SELECTOR, ".navigation-global__link").click()

# # 스크롤 전 높이.
# before_h = browser.execute_script("return window.scrollY")

