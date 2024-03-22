import requests
from pprint import pprint

API_KEY='51d6d121000ea1f6bb2fd0be296e5260'
# 주택 담보대출
url=f'http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={API_KEY}&topFinGrpNo=050000&pageNo=1'
# 전세자금 대출 
# url=f'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={API_KEY}&topFinGrpNo=050000&pageNo=1'
# 개인신용 대출
# url=f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={API_KEY}&topFinGrpNo=050000&pageNo=1'
response = requests.get(url).json()
pprint(response)
