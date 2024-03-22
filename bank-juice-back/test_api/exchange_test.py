import requests
from pprint import pprint

API_KEY='SK1AOcKyetZo6Yb299x6479RJBV4ZbIo'
# url=f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate=20180102&data=AP01'
url=f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&data=AP01'

response = requests.get(url).json()
pprint(response)