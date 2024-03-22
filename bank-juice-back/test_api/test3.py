import requests
from pprint import pprint

api_key = '51d6d121000ea1f6bb2fd0be296e5260'
url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
response = requests.get(url).json()

# pprint(response['result'].get('baseList')[0])
pprint(response['result'].get('optionList'))
print(len(response['result'].get('optionList')))