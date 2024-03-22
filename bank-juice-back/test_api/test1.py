# import requests
# from pprint import pprint

# api_key = '51d6d121000ea1f6bb2fd0be296e5260'
# url = f'http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={api_key}&topFinGrpNo=030200&pageNo=1'
# response = requests.get(url).json()

# pprint(response['result'].get('baseList'))
# # print(len(response['result'].get('baseList')))
# # pprint(response['result'].get('optionList'))


# banks = [
#     {
#         "dcls_month":"201511",
#         "fin_co_no":"0010001",
#         "kor_co_nm":"우리은행",
#         "dcls_chrg_man":"영업기획팀 02-6950-7976",
#         "homp_url":"http://www.shinhancard.co.kr",
#         "cal_tel":"15447000"
#      },
#      {
#         "dcls_month":"201511",
#         "fin_co_no":"0010002",
#         "kor_co_nm":"한국스탠다드차타드은행",
#         "dcls_chrg_man":"카드상품부 02-3702-4718",
#         "homp_url":"http://www.standardchartered.co.kr",
#         "cal_tel":"15881599"
#     },
#     {
#         "dcls_month":"201511",
#         "fin_co_no":"0010006",
#         "kor_co_nm":"한국씨티은행",
#         "dcls_chrg_man":"카드포트폴리오부 02-2004-1224",
#         "homp_url":"http://www.citibank.co.kr",
#         "cal_tel":"15660777"
#     },
#     {
#         "dcls_month":"201511",
#         "fin_co_no":"0010013",
#         "kor_co_nm":"한국외환은행",
#         "dcls_chrg_man":"기업공시국 02-222-3333",
#         "homp_url":"http://www.kfb.or.kr",
#         "cal_tel":"0237055000"
#     },
#     {
#         "dcls_month":"201511",
#         "fin_co_no":"0010016",
#         "kor_co_nm":"대구은행",
#         "dcls_chrg_man":"카드사업부 053-740-2915",
#         "homp_url":"http://www.dgb.co.kr",
#         "cal_tel":"15665050"
#     }]


# test_bank = [
#     {'cal_tel': '15885000',
#   'dcls_chrg_man': '개인고객부, 1588-5000\n부동산금융부,  1588-5000',
#   'dcls_month': '202310',
#   'fin_co_no': '0010001',
#   'homp_url': 'https://spot.wooribank.com/pot/Dream?withyou=po',
#   'kor_co_nm': '우리은행'},
#  {'cal_tel': '15881599',
#   'dcls_chrg_man': 'SC제일은행 고객센터\n1588-1599',
#   'dcls_month': '202310',
#   'fin_co_no': '0010002',
#   'homp_url': 'http://www.standardchartered.co.kr',
#   'kor_co_nm': '한국스탠다드차타드은행'},
#  {'cal_tel': '15885050',
#   'dcls_chrg_man': '개인여신기획부, 053-740-2230                                  '
#                    '리테일마케팅부, 053-740-2162',
#   'dcls_month': '202310',
#   'fin_co_no': '0010016',
#   'homp_url': 'http://www.dgb.co.kr/dgb_ebz_main.jsp',
#   'kor_co_nm': '대구은행'},
#  {'cal_tel': '15886200',
#   'dcls_chrg_man': '(예금)마케팅추진부, 051-620-3339\n'
#                    '(대출)여신기획부, 051-620-3423\n'
#                    '실제 상담은 인근 영업점이나 당행 콜센터(1588-6200)로 문의',
#   'dcls_month': '202310',
#   'fin_co_no': '0010017',
#   'homp_url': 'http://www.busanbank.co.kr',
#   'kor_co_nm': '부산은행'},
#  {'cal_tel': '15883388',
#   'dcls_chrg_man': '영업추진부 수신지원팀 062-239-5206          여신지원팀 062-239-6509\n'
#                    '카드사업부 062-239-6107\n'
#                    '*실제 상담은 인근영업점이나 당행 콜센터(1588-3388)로 문의',
#   'dcls_month': '202310',
#   'fin_co_no': '0010019',
#   'homp_url': 'http://www.kjbank.com',
#   'kor_co_nm': '광주은행'},
#  {'cal_tel': '15880079',
#   'dcls_chrg_man': '영업추진본부, 064-720-0287',
#   'dcls_month': '202310',
#   'fin_co_no': '0010020',
#   'homp_url': 'https://e-jejubank.com',
#   'kor_co_nm': '제주은행'},
#  {'cal_tel': '15884477',
#   'dcls_chrg_man': '마케팅추진부 \n'
#                    '마케팅추진팀,\n'
#                    '063-250-7469\n'
#                    '여신기획부,\n'
#                    '063-250-7370\n'
#                    '* 실제 상담은 인근 영업점이나 당행 콜센터(1588-4477)로 문의',
#   'dcls_month': '202310',
#   'fin_co_no': '0010022',
#   'homp_url': 'https://www.jbbank.co.kr/EFINANCE_MAIN.act',
#   'kor_co_nm': '전북은행'},
#  {'cal_tel': '16008585',
#   'dcls_chrg_man': '리테일금융부(대출문의),055-290-8743\n마케팅추진부(예·적금상품),1600-8585',
#   'dcls_month': '202310',
#   'fin_co_no': '0010024',
#   'homp_url': 'https://www.knbank.co.kr/ib20/mnu/FPMDPT020000000',
#   'kor_co_nm': '경남은행'},
#  {'cal_tel': '15662566',
#   'dcls_chrg_man': '고객 문의 1566-2566',
#   'dcls_month': '202310',
#   'fin_co_no': '0010026',
#   'homp_url': 'http://www.ibk.co.kr',
#   'kor_co_nm': '중소기업은행'},
#  {'cal_tel': '0215881500',
#   'dcls_chrg_man': '(예금)수신기획부, 02-787-7410\n'
#                    '(개인대출)지역성장지원실, 051-640-3372\n'
#                    '(기업대출)영업기획부, 02-787-6929',
#   'dcls_month': '202310',
#   'fin_co_no': '0010030',
#   'homp_url': 'https://www.kdb.co.kr',
#   'kor_co_nm': '한국산업은행'},
#  {'cal_tel': '15889999',
#   'dcls_chrg_man': '(예금)수신상품부(P), 02-1588-9999\n(대출)개인여신부(P), 02-1588-9999',
#   'dcls_month': '202310',
#   'fin_co_no': '0010927',
#   'homp_url': 'http://www.kbstar.com',
#   'kor_co_nm': '국민은행'},
#  {'cal_tel': '15778000',
#   'dcls_chrg_man': '개인고객부 1577-8000(수신)\n개인고객부 1577-8000(여신)',
#   'dcls_month': '202310',
#   'fin_co_no': '0011625',
#   'homp_url': 'http://www.shinhan.com',
#   'kor_co_nm': '신한은행'},
#  {'cal_tel': '16613000',
#   'dcls_chrg_man': '마케팅지원부, 02-2080-7799(여신), 7776(수신)',
#   'dcls_month': '202310',
#   'fin_co_no': '0013175',
#   'homp_url': 'https://banking.nonghyup.com',
#   'kor_co_nm': '농협은행주식회사'}
# ]
# for bank in banks:
#     pprint(bank)