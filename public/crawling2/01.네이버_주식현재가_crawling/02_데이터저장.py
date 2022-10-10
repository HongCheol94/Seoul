from urllib import response
import openpyxl
import requests
from bs4 import BeautifulSoup
import openpyxl

fpath = r'/Users/kims/Desktop/java1/java/factory/git/seoul/public/crawling2/01.네이버_주식현재가_crawling/date.xlsx'
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 황성화된 시트 선택


#종목 코드 리스트
codes = [
    '005930',
    '000660',
    '035720'

]

row = 2 # 행값 변수로 지정
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one("#_nowVal").text
    price = price.replace(',' , '') # 현재가의 ,가 있으면 문자열을 숫자로 변환 할 수 없어서 문자열 교체 함수를 사용 앞에가 교체할 문자 뒤에가 교체가 될 문자
    print(price)
    ws[f'B{row}'] =  int(price )#첫번째 for문을 돌면 B2에 지정 되고
    row = row + 1 # 2 +1 이 돼서 B3에 저장
    wb.save(fpath)