from urllib import response
import requests
from bs4 import BeautifulSoup

#종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'

]

for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',' , '') # 현재가의 ,가 있으면 문자열을 숫자로 변환 할 수 없어서 문자열 교체 함수를 사용 앞에가 교체할 문자 뒤에가 교체가 될 문자
    print(price)