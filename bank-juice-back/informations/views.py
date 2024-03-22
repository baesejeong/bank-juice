from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
import requests
from pprint import pprint
from django.contrib.auth import get_user_model
from math import floor
from django.conf import settings


from .models import Bank, Exchange
from .models import Deposit, Savings, Personal_Credit_Loan, Mortgage_Loan, Jeonse_Loan
from .models import Deposit_Options, Savings_Options, Personal_Options, Mortgage_Options, Jeonse_Options
from .models import Deposit_Category, Savings_Category, Personal_Category, Mortgage_Category, Jeonse_Category
from .models import Deposit_Output, Savings_Output, Personal_Output, Mortgage_Output, Jeonse_Output
from .serializers import BankSerializer, PersonalSerializer, PersonalOptionSerializer, MortgageSerializer, MortgageOptionSerializer, JeonseSerializer, JeonseOptionSerializer
from .serializers import DepositSerializer, DepositOptionSerializer, SavingSerializer, SavingOptionSerializer, ExchangeSerializer
from .serializers import DepositOutputSerializer, SavingsOutputSerializer, PersonalOutputSerializer, MortgageOutputSerializer, JeonseOutputSerializer
from django.conf import settings

# 은행 정보
@api_view(['GET', 'POST',])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def bank(request):
    if request.method == 'GET':
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        API_KEY = settings.FINANCE_API_KEY
        FinGrpNo = ['020000', '030200', '030300', '050000', '060000']
        for pageNo in range(1, 4):
            for topFinGrpNo in FinGrpNo :
                url = f'http://finlife.fss.or.kr/finlifeapi/companySearch.json?auth={API_KEY}&topFinGrpNo={topFinGrpNo}&pageNo={pageNo}'
                response = requests.get(url).json()
                banks = response['result'].get('baseList')
                for bank in banks:
                    if not Bank.objects.filter(fin_co_no=bank['fin_co_no']).exists():
                        serializer = BankSerializer(data=banks, many=True)
                        if serializer.is_valid(raise_exception=True):
                            serializer.save()
        return Response({ 'message': 'bank 저장 완료' })


@api_view(['GET',])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def bank_detail(request, bank_pk):
    if request.method == 'GET':
        bank = Bank.objects.get(pk=bank_pk)
        serializer = BankSerializer(bank)
        return Response(serializer.data)


# 환율 정보 
@api_view(['GET', 'POST',])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def exchange(request):
    if request.method == 'GET':
        exchanges = Exchange.objects.all()
        serializer = ExchangeSerializer(exchanges, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        API_KEY = settings.EXCHANGE_API_KEY
        url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&data=AP01'
        exchanges = requests.get(url).json()
        serializer = ExchangeSerializer(data=exchanges, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({ 'message': 'Exchange 저장 완료' })


# 예금 정보
@api_view(['GET', 'POST',])
# @permission_classes([IsAuthenticated])
@permission_classes([AllowAny])
def deposit(request):
    if request.method == 'GET':
        tariff = float(request.GET.get('tariff'))
        amount = int(request.GET.get('amount'))
        period = int(request.GET.get('period'))
        rate = 0

        if request.GET.get('joinWay') == 'all':
            deposits = Deposit_Output.objects.all()
        elif request.GET.get('joinWay') == 'online':
            deposits = Deposit_Output.objects.filter(join_way__contains='인터넷') \
                | Deposit_Output.objects.filter(join_way__contains='스마트폰') 
        elif request.GET.get('joinWay') == 'visit':
            deposits = Deposit_Output.objects.filter(join_way__contains='영업점')

        if period == 6:
            filtered_deposits = deposits.exclude(intr_rate_6=None).order_by('-intr_rate_6')
        elif period == 12:
            filtered_deposits = deposits.exclude(intr_rate_12=None).order_by('-intr_rate_12')
        elif period == 24:
            filtered_deposits = deposits.exclude(intr_rate_24=None).order_by('-intr_rate_24')
        elif period == 36:
            filtered_deposits = deposits.exclude(intr_rate_36=None).order_by('-intr_rate_36')

        for deposit in filtered_deposits:
            if period == 6:
                rate = float(deposit.intr_rate_6)
            elif period == 12:
                rate = float(deposit.intr_rate_12)
            elif period == 24:
                rate = float(deposit.intr_rate_24)
            elif period == 36:
                rate = float(deposit.intr_rate_36)

            deposit.interest_before_tax = ((rate * 0.01) * amount) * (1 - tariff)
            deposit.interest_after_tax = (rate * 0.01) * amount
            deposit.save()
        
        serializer = DepositOutputSerializer(filtered_deposits, many=True)

        return Response(serializer.data)


    elif request.method == 'POST':
        API_KEY = settings.FINANCE_API_KEY
        url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
        response = requests.get(url).json()

        products = response['result'].get('baseList')
        for product in products:
            bank = Bank.objects.get(fin_co_no=product['fin_co_no'])
            if not Deposit.objects.filter(fin_prdt_cd=product['fin_prdt_cd']).exists():
                deposit_serializer = DepositSerializer(data=product)
                if deposit_serializer.is_valid(raise_exception=True):
                    deposit_serializer.save(bank=bank)

        options = response['result'].get('optionList')
        for option in options:
            deposit = Deposit.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            if not Deposit_Options.objects.filter(deposit=deposit).filter(
                fin_prdt_cd = option['fin_prdt_cd'],
                intr_rate = option['intr_rate'] ,
                intr_rate2 = option['intr_rate2'] ,
                intr_rate_type = option['intr_rate_type'] ,
                intr_rate_type_nm = option['intr_rate_type_nm'] ,
                save_trm = option['save_trm']
            ).exists():
                option_serializer = DepositOptionSerializer(data=option)
                if option_serializer.is_valid(raise_exception=True):
                    option_serializer.save(deposit=deposit)
                
                # 상품 카테고리 생성
                deposit_category = Deposit_Category()
                if not option['intr_rate'] :
                    deposit_category.intr_rate = option['intr_rate']
                else:
                    deposit_category.intr_rate = str(floor(option['intr_rate']))
                
                
                if not option['intr_rate2']:
                    deposit_category.intr_rate2 = option['intr_rate2']
                else:
                    deposit_category.intr_rate2 = str(floor(option['intr_rate2']))

                deposit_category.intr_rate_type = option['intr_rate_type']
                
                deposit_category.save_trm = option['save_trm']
                
                # Deposit_Category Model에 해당 카테고리가 존재한다면
                # filter로 찾은 값의 첫번째 인덱스의 값을 category에 넣고
                # 존재하지 않는다면 위에서 생성한 인스턴스를 저장 후 category에 넣는다.   
                if Deposit_Category.objects.filter(
                    intr_rate = deposit_category.intr_rate,
                    intr_rate2 = deposit_category.intr_rate2,
                    intr_rate_type = deposit_category.intr_rate_type,
                    save_trm = deposit_category.save_trm
                ).exists():
                    deposit_category = Deposit_Category.objects.filter(
                    intr_rate = deposit_category.intr_rate,
                    intr_rate2 = deposit_category.intr_rate2,
                    intr_rate_type = deposit_category.intr_rate_type,
                    save_trm = deposit_category.save_trm
                )[0]
                
                else:        
                    deposit_category.save()
        
                # 저장한 category 가 해당 deposit 상품에 존재하지 않는다면 추가
                if not deposit.deposit_category.filter(
                    intr_rate = deposit_category.intr_rate,
                    intr_rate2 = deposit_category.intr_rate2,
                    intr_rate_type = deposit_category.intr_rate_type,
                    save_trm = deposit_category.save_trm
                ).exists():
                    deposit.deposit_category.add(deposit_category)
           
        # deposit output data setting
        deposits = Deposit.objects.all()
        for deposit in deposits:
            deposit_output = Deposit_Output()
            for option in deposit.options.all():
                if option.save_trm == '6':
                    if option.intr_rate:
                        deposit_output.intr_rate_6 = option.intr_rate
                    elif option.intr_rate2:
                        deposit_output.intr_rate_6 = option.intr_rate2
                    else:
                        deposit_output.intr_rate_6 = None
                elif option.save_trm == '12':
                    if option.intr_rate:
                        deposit_output.intr_rate_12 = option.intr_rate
                    elif option.intr_rate2:
                        deposit_output.intr_rate_12 = option.intr_rate2
                    else:
                        deposit_output.intr_rate_12 = None
                elif option.save_trm == '24':
                    if option.intr_rate:
                        deposit_output.intr_rate_24 = option.intr_rate
                    elif option.intr_rate2:
                        deposit_output.intr_rate_24 = option.intr_rate2
                    else:
                        deposit_output.intr_rate_24 = None
                elif option.save_trm == '36':
                    if option.intr_rate:
                        deposit_output.intr_rate_36 = option.intr_rate
                    elif option.intr_rate2:
                        deposit_output.intr_rate_36 = option.intr_rate2
                    else:
                        deposit_output.intr_rate_36 = None
            deposit_output.kor_co_nm = deposit.kor_co_nm
            deposit_output.fin_prdt_nm = deposit.fin_prdt_nm
            deposit_output.join_way = deposit.join_way
            deposit_output.deposit = deposit
            deposit_output.save()

        return Response({ 'message': 'Deposit 저장 완료' })
    

@api_view(['GET',])
@permission_classes([AllowAny])
def deposit_detail(request, deposit_pk):
    if request.method == 'GET':
        deposit = Deposit.objects.get(pk=deposit_pk)
        serializer = DepositSerializer(deposit)
        return Response(serializer.data)

    
@api_view(['GET', 'POST',])
@permission_classes([IsAuthenticated])
# @permission_classes([AllowAny])
def deposit_save(request, deposit_pk):
    if request.method == 'GET':
        deposit = Deposit.objects.get(pk=deposit_pk)
        categories = deposit.deposit_category.all()
        
        recommend_deposit = set()
        
        for category in categories:
            for category_deposit in category.deposits.all():
                if category_deposit != deposit:
                    recommend_deposit.add(category_deposit)
        
        recommend_deposit = list(recommend_deposit)
        
        serializer = DepositSerializer(recommend_deposit, many=True)
        
        return Response(serializer.data)
        
    
    elif request.method == 'POST':
        user = get_user_model().objects.get(username=request.user.username)
        deposit = Deposit.objects.get(pk=deposit_pk)
        if user.deposit.filter(fin_prdt_cd=deposit.fin_prdt_cd).exists(): 
            user.deposit.remove(deposit)        
            return Response({'message':'저장취소'})
        else :
            user.deposit.add(deposit)
            return Response({'message':'저장완료'})                       


@api_view(['GET', 'POST',])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def savings(request):
    if request.method == 'GET':
        tariff = float(request.GET.get('tariff'))
        amount = int(request.GET.get('amount'))
        period = int(request.GET.get('period'))
        rate = 0

        if request.GET.get('joinWay') == 'all':
            savings = Savings_Output.objects.all()
        elif request.GET.get('joinWay') == 'online':
            savings = Savings_Output.objects.filter(join_way__contains='인터넷') \
                | Savings_Output.objects.filter(join_way__contains='스마트폰') 
        elif request.GET.get('joinWay') == 'visit':
            savings = Savings_Output.objects.filter(join_way__contains='영업점')

        if period == 6:
            filtered_savings = savings.exclude(intr_rate_6=None).order_by('-intr_rate_6')
        elif period == 12:
            filtered_savings = savings.exclude(intr_rate_12=None).order_by('-intr_rate_12')
        elif period == 24:
            filtered_savings = savings.exclude(intr_rate_24=None).order_by('-intr_rate_24')
        elif period == 36:
            filtered_savings = savings.exclude(intr_rate_36=None).order_by('-intr_rate_36')
        for save in filtered_savings:
            if period == 6:
                rate = float(save.intr_rate_6)
            elif period == 12:
                rate = float(save.intr_rate_12)
            elif period == 24:
                rate = float(save.intr_rate_24)
            elif period == 36:
                rate = float(save.intr_rate_36)

            save.interest_before_tax = ((rate * 0.01) * amount) * (1 - tariff)
            save.interest_after_tax = (rate * 0.01) * amount
            save.save()
        
        serializer = SavingsOutputSerializer(filtered_savings, many=True)

        return Response(serializer.data)


    elif request.method == 'POST':
        api_key = settings.FINANCE_API_KEY
        url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
        response = requests.get(url).json()

        products = response['result'].get('baseList')
        for product in products:
            bank = Bank.objects.get(fin_co_no=product['fin_co_no'])
            if not Savings.objects.filter(fin_prdt_cd=product['fin_prdt_cd']).exists():
                savings_serializer = SavingSerializer(data=product)
                if savings_serializer.is_valid(raise_exception=True):
                    savings_serializer.save(bank=bank)

        options = response['result'].get('optionList')
        for option in options:
            savings = Savings.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            if not Savings_Options.objects.filter(savings=savings).filter(
                fin_prdt_cd = option['fin_prdt_cd'],
                intr_rate = option['intr_rate'] ,
                intr_rate2 = option['intr_rate2'] ,
                intr_rate_type = option['intr_rate_type'] ,
                intr_rate_type_nm = option['intr_rate_type_nm'] ,
                rsrv_type = option['rsrv_type'],
                rsrv_type_nm = option['rsrv_type_nm'],
                save_trm = option['save_trm']
            ).exists():
                option_serializer = SavingOptionSerializer(data=option)
                if option_serializer.is_valid(raise_exception=True):
                    option_serializer.save(savings=savings)
            
            # 상품 카테고리 생성
            savings_category = Savings_Category()
            if not option['intr_rate']:
                savings_category.intr_rate = option['intr_rate']
            else :
                savings_category.intr_rate = str(floor(option['intr_rate']))
            
            if not option['intr_rate2']:
                savings_category.intr_rate2 = option['intr_rate2']
            else :
                savings_category.intr_rate2 = str(floor(option['intr_rate2']))
            savings_category.intr_rate_type = option['intr_rate_type']
            savings_category.rsrv_type = option['rsrv_type']
            savings_category.save_trm = option['save_trm']
            
            if Savings_Category.objects.filter(
                intr_rate = savings_category.intr_rate,
                intr_rate2 = savings_category.intr_rate2,
                intr_rate_type = savings_category.intr_rate_type,
                save_trm = savings_category.save_trm
            ).exists():
                savings_category = Savings_Category.objects.filter(
                intr_rate = savings_category.intr_rate,
                intr_rate2 = savings_category.intr_rate2,
                intr_rate_type = savings_category.intr_rate_type,
                save_trm = savings_category.save_trm
            )[0]
            else :
                savings_category.save()

            if not savings.savings_category.filter(
                intr_rate = savings_category.intr_rate,
                intr_rate2 = savings_category.intr_rate2,
                intr_rate_type = savings_category.intr_rate_type,
                save_trm = savings_category.save_trm
            ).exists():
                savings.savings_category.add(savings_category)
                
        # savings output data setting
        savings = Savings.objects.all()
        for save in savings:
            savings_output = Savings_Output()
            for option in save.options.all():
                if option.save_trm == '6':
                    if option.intr_rate:
                        savings_output.intr_rate_6 = option.intr_rate
                    elif option.intr_rate2:
                        savings_output.intr_rate_6 = option.intr_rate2
                    else:
                        savings_output.intr_rate_6 = None
                elif option.save_trm == '12':
                    if option.intr_rate:
                        savings_output.intr_rate_12 = option.intr_rate
                    elif option.intr_rate2:
                        savings_output.intr_rate_12 = option.intr_rate2
                    else:
                        savings_output.intr_rate_12 = None
                elif option.save_trm == '24':
                    if option.intr_rate:
                        savings_output.intr_rate_24 = option.intr_rate
                    elif option.intr_rate2:
                        savings_output.intr_rate_24 = option.intr_rate2
                    else:
                        savings_output.intr_rate_24 = None
                elif option.save_trm == '36':
                    if option.intr_rate:
                        savings_output.intr_rate_36 = option.intr_rate
                    elif option.intr_rate2:
                        savings_output.intr_rate_36 = option.intr_rate2
                    else:
                        savings_output.intr_rate_36 = None
            savings_output.kor_co_nm = save.kor_co_nm
            savings_output.fin_prdt_nm = save.fin_prdt_nm
            savings_output.join_way = save.join_way
            savings_output.savings = save
            savings_output.save()

        return Response({ 'message': 'Saving 저장 완료' })


@permission_classes([AllowAny])
@api_view(['GET',])
def savings_detail(request, savings_pk):
    if request.method == 'GET':
        savings = Savings.objects.get(pk=savings_pk)
        serializer = SavingSerializer(savings)
        return Response(serializer.data)


# @permission_classes([AllowAny])
@api_view(['GET', 'POST',])
@permission_classes([IsAuthenticated])
def savings_save(request, savings_pk):
    if request.method == 'GET':
        savings = Savings.objects.get(pk=savings_pk)
        categories = savings.savings_category.all()
        
        recommend_savings = set()
        
        for category in categories:
            for category_savings in category.savings.all():
                if category_savings != savings:
                    recommend_savings.add(category_savings)
        
        recommend_savings = list(recommend_savings)
        
        serializer = SavingSerializer(recommend_savings, many=True)
        
        return Response(serializer.data)
    
    elif request.method =='POST':    
        user = get_user_model().objects.get(username=request.user.username)
        savings = Savings.objects.get(pk=savings_pk)
        if user.savings.filter(fin_prdt_cd=savings.fin_prdt_cd).exists(): 
            user.savings.remove(savings)        
            return Response({'message':'저장취소'})
        else :
            user.savings.add(savings)
            return Response({'message':'저장완료'})


@api_view(['GET', 'POST',])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def personal(request):
    if request.method == 'GET':
        rateType = request.GET.get('rateType')
        amount = int(request.GET.get('amount'))
        creditScore = int(request.GET.get('creditScore'))
        
        rate = 0

        if request.GET.get('joinWay') == 'all':
            personals = Personal_Output.objects.all()
        elif request.GET.get('joinWay') == 'online':
            personals = Personal_Output.objects.filter(join_way__contains='인터넷') \
                | Personal_Output.objects.filter(join_way__contains='스마트폰') 
        elif request.GET.get('joinWay') == 'visit':
            personals = Personal_Output.objects.filter(join_way__contains='영업점')

        if rateType == '1': 
            filtered_personals = personals.filter(crdt_lend_rate_type_nm__contains='기준금리')
        elif rateType == '2':
            filtered_personals = personals.filter(crdt_lend_rate_type_nm__contains='가산금리')
        elif rateType == '3':
            filtered_personals = personals.filter(crdt_lend_rate_type_nm__contains='가감조정금리')
        
        
        for personal in filtered_personals:
            current_rate = {
                300: [
                    personal.crdt_grad_12, 
                    personal.crdt_grad_11,
                    personal.crdt_grad_10,
                    personal.crdt_grad_6,
                    personal.crdt_grad_5,
                    personal.crdt_grad_4,
                    personal.crdt_grad_1
                    ],
                400: [
                    personal.crdt_grad_13, 
                    personal.crdt_grad_11,
                    personal.crdt_grad_10,
                    personal.crdt_grad_6,
                    personal.crdt_grad_5,
                    personal.crdt_grad_4,
                    personal.crdt_grad_1
                ],
                500: [
                    personal.crdt_grad_12, 
                    personal.crdt_grad_10,
                    personal.crdt_grad_13,
                    personal.crdt_grad_6,
                    personal.crdt_grad_5,
                    personal.crdt_grad_4,
                    personal.crdt_grad_1
                ],
                600: [
                    personal.crdt_grad_11, 
                    personal.crdt_grad_6,
                    personal.crdt_grad_12,
                    personal.crdt_grad_5,
                    personal.crdt_grad_13,
                    personal.crdt_grad_4,
                    personal.crdt_grad_1
                ],
                700: [
                    personal.crdt_grad_10, 
                    personal.crdt_grad_5,
                    personal.crdt_grad_11,
                    personal.crdt_grad_4,
                    personal.crdt_grad_12,
                    personal.crdt_grad_1,
                    personal.crdt_grad_13
                ],
                800: [
                    personal.crdt_grad_6, 
                    personal.crdt_grad_4,
                    personal.crdt_grad_10,
                    personal.crdt_grad_1,
                    personal.crdt_grad_11,
                    personal.crdt_grad_12,
                    personal.crdt_grad_13
                ],
                900: [
                    personal.crdt_grad_5, 
                    personal.crdt_grad_1,
                    personal.crdt_grad_6,
                    personal.crdt_grad_10,
                    personal.crdt_grad_11,
                    personal.crdt_grad_12,
                    personal.crdt_grad_13
                ],
                1000: [
                    personal.crdt_grad_4, 
                    personal.crdt_grad_5,
                    personal.crdt_grad_6,
                    personal.crdt_grad_10,
                    personal.crdt_grad_11,
                    personal.crdt_grad_12,
                    personal.crdt_grad_13
                ],
            }
                
            rate = 0
            if creditScore <= 300:
                if personal.crdt_grad_13 :
                    rate = float(personal.crdt_grad_13)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[300][idx]:
                            rate = float(current_rate[300][idx])
                        idx += 1
                        
            elif creditScore <= 400:
                if personal.crdt_grad_12 :
                    rate = float(personal.crdt_grad_12)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[400][idx]:
                            rate = float(current_rate[400][idx])
                        idx += 1
            elif creditScore <= 500:
                if personal.crdt_grad_11 :
                    rate = float(personal.crdt_grad_11)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[500][idx]:
                            rate = float(current_rate[500][idx])
                        idx += 1
            elif creditScore <= 600:
                if personal.crdt_grad_10 :
                    rate = float(personal.crdt_grad_10)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[600][idx]:
                            rate = float(current_rate[600][idx])
                        idx += 1
            elif creditScore <= 700:
                if personal.crdt_grad_6 :
                    rate = float(personal.crdt_grad_6)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[700][idx]:
                            rate = float(current_rate[700][idx])
                        idx += 1
            elif creditScore <= 800:
                if personal.crdt_grad_5 :
                    rate = float(personal.crdt_grad_5)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[800][idx]:
                            rate = float(current_rate[800][idx])
                        idx += 1
            elif creditScore <= 900:
                if personal.crdt_grad_4 :
                    rate = float(personal.crdt_grad_4)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[900][idx]:
                            rate = float(current_rate[900][idx])
                        idx += 1
            elif creditScore <= 1000:
                if personal.crdt_grad_1 :
                    rate = float(personal.crdt_grad_1)
                else:
                    idx = 0
                    while not rate:
                        if current_rate[1000][idx]:
                            rate = float(current_rate[1000][idx])
                        idx += 1
            personal.rate = rate
            personal.loan_interest = round(((rate * 0.01) * amount) / 12, -3)
            personal.save()
        
        serializer = PersonalOutputSerializer(filtered_personals, many=True)

        return Response(serializer.data)


    elif request.method == 'POST':
        api_key = settings.FINANCE_API_KEY
        url = f'http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
        response = requests.get(url).json()

        products = response['result'].get('baseList')
        for product in products:
            bank = None
            if Bank.objects.filter(fin_co_no=product['fin_co_no']).exists():
                bank = Bank.objects.get(fin_co_no=product['fin_co_no'])
            
            if not Personal_Credit_Loan.objects.filter(fin_prdt_cd=product['fin_prdt_cd']).exists():
                personal_serializer = PersonalSerializer(data=product)
                if personal_serializer.is_valid(raise_exception=True):
                    personal_serializer.save(bank=bank)                    

        options = response['result'].get('optionList')
        for option in options:
            personal = Personal_Credit_Loan.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            if not Personal_Options.objects.filter(personal_credit_loan=personal).filter(
                fin_prdt_cd = option['fin_prdt_cd'],
                crdt_lend_rate_type = option['crdt_lend_rate_type'] ,
                crdt_lend_rate_type_nm = option['crdt_lend_rate_type_nm'] ,
                crdt_grad_1 = option['crdt_grad_1'] ,
                crdt_grad_4 = option['crdt_grad_4'] ,
                crdt_grad_5 = option['crdt_grad_5'] ,
                crdt_grad_6 = option['crdt_grad_6'] ,
                crdt_grad_10 = option['crdt_grad_10'] ,
                crdt_grad_11 = option['crdt_grad_11'] ,
                crdt_grad_12 = option['crdt_grad_12'] ,
                crdt_grad_13 = option['crdt_grad_13'] ,
                crdt_grad_avg = option['crdt_grad_avg']
                ).exists():
                option_serializer = PersonalOptionSerializer(data=option)
                if option_serializer.is_valid(raise_exception=True):
                    option_serializer.save(personal_credit_loan=personal)
                    
                # 상품 카테고리 생성
                personal_category = Personal_Category()
                
                personal_category.crdt_lend_rate_type = option['crdt_lend_rate_type']
  
                if Personal_Category.objects.filter(
                        crdt_lend_rate_type = personal_category.crdt_lend_rate_type
                    ).exists():
                    personal_category = Personal_Category.objects.filter(
                        crdt_lend_rate_type = personal_category.crdt_lend_rate_type
                    )[0]
                
                else:        
                    personal_category.save()
        
                if not personal.personal_category.filter(
                        crdt_lend_rate_type = personal_category.crdt_lend_rate_type
                    ).exists():
                    personal.personal_category.add(personal_category)

            # personal output data setting
        personals = Personal_Credit_Loan.objects.all()
        for personal in personals:
            for option in personal.options.all():
                personal_output = Personal_Output()
                personal_output.crdt_grad_1 = option.crdt_grad_1
                personal_output.crdt_grad_4 = option.crdt_grad_4
                personal_output.crdt_grad_5 = option.crdt_grad_5
                personal_output.crdt_grad_6 = option.crdt_grad_6
                personal_output.crdt_grad_10 = option.crdt_grad_10
                personal_output.crdt_grad_11 = option.crdt_grad_11
                personal_output.crdt_grad_12 = option.crdt_grad_12
                personal_output.crdt_grad_13 = option.crdt_grad_13
                personal_output.crdt_grad_avg = option.crdt_grad_avg
                personal_output.crdt_lend_rate_type_nm = option.crdt_lend_rate_type_nm
                personal_output.kor_co_nm = personal.kor_co_nm
                personal_output.fin_prdt_nm = personal.fin_prdt_nm
                personal_output.join_way = personal.join_way
                personal_output.personal = personal
                personal_output.save()

        return Response({ 'message': 'Personal 저장 완료' })


@permission_classes([AllowAny])
@api_view(['GET',])
def personal_detail(request, personal_pk):
    if request.method == 'GET':
        personal = Personal_Credit_Loan.objects.get(pk=personal_pk)
        serializer = PersonalSerializer(personal)
        return Response(serializer.data)


# @permission_classes([AllowAny])
@api_view(['GET', 'POST',])
@permission_classes([IsAuthenticated])
def personal_save(request, personal_pk):
    if request.method == 'GET':
        personal = Personal_Credit_Loan.objects.get(pk=personal_pk)
        categories = personal.personal_category.all()
        
        recommend_personal = set()
        
        for category in categories:
            for category_personal in category.personals.all():
                if category_personal != personal:
                    recommend_personal.add(category_personal)
        
        recommend_personal = list(recommend_personal)
        
        serializer = PersonalSerializer(recommend_personal, many=True)
        
        return Response(serializer.data)
    
    elif request.method =='POST':
        user = get_user_model().objects.get(username=request.user.username)
        personal = Personal_Credit_Loan.objects.get(pk=personal_pk)
        if user.personal.filter(fin_prdt_cd=personal.fin_prdt_cd).exists(): 
            user.personal.remove(personal)        
            return Response({'message':'저장취소'})
        else :
            user.personal.add(personal)
            return Response({'message':'저장완료'})


@permission_classes([AllowAny])
@api_view(['GET', 'POST',])
# @permission_classes([IsAuthenticated])
def mortgage(request):
    if request.method == 'GET':
        houseType = request.GET.get('houseType')
        joinWay = request.GET.get('joinWay')
        repayWay = request.GET.get('repayWay')
        rateType = request.GET.get('rateType')
        amount = int(request.GET.get('amount'))
        period = int(request.GET.get('period'))
        
        if houseType == '1':
            filtered_house_type_mortgages = Mortgage_Output.objects.filter(mrtg_type_nm='아파트')
        elif houseType == '2':
            filtered_house_type_mortgages = Mortgage_Output.objects.filter(mrtg_type_nm='아파트외')

        if joinWay == 'all':
            filtered_join_way_mortgages = filtered_house_type_mortgages
        elif joinWay == 'online':
            filtered_join_way_mortgages = filtered_house_type_mortgages.filter(join_way__contains='인터넷') \
                | filtered_house_type_mortgages.filter(join_way__contains='스마트폰') 
        elif joinWay == 'visit':
            filtered_join_way_mortgages = filtered_house_type_mortgages.filter(join_way__contains='영업점')

        if repayWay == '1':
            filtered_repay_way_mortgages = filtered_join_way_mortgages.filter(rpay_type_nm='분할상환방식')
        elif repayWay == '2':
            filtered_repay_way_mortgages = filtered_join_way_mortgages.filter(rpay_type_nm='만기일시상환방식')

        if rateType == '1':
            mortgages = filtered_repay_way_mortgages.filter(lend_rate_type_nm='고정금리')
        elif rateType == '2':
            mortgages = filtered_repay_way_mortgages.filter(lend_rate_type_nm='변동금리')
            
        for mortgage in mortgages:
            mortgage.loan_interest_min = ((amount * (float(mortgage.lend_rate_min) * 0.01))) / (12 * period)
            mortgage.loan_interest_max = ((amount * (float(mortgage.lend_rate_max) * 0.01))) / (12 * period)
            
            mortgage.save()     
        
        serializer = MortgageOutputSerializer(mortgages, many=True)
        
        return Response(serializer.data)
        
        
    elif request.method == 'POST':
        api_key = settings.FINANCE_API_KEY
        url = f'http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
        response = requests.get(url).json()

        products = response['result'].get('baseList')
        for product in products:
            bank = ''
            if Bank.objects.filter(fin_co_no=product['fin_co_no']).exists():
                bank = Bank.objects.get(fin_co_no=product['fin_co_no'])

            if not Mortgage_Loan.objects.filter(fin_prdt_cd=product['fin_prdt_cd']).exists():
                mortgage_serializer = MortgageSerializer(data=product)
                if mortgage_serializer.is_valid(raise_exception=True):
                    mortgage_serializer.save(bank=bank)                    

        options = response['result'].get('optionList')
        for option in options:
            mortgage_loan = Mortgage_Loan.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            if not Mortgage_Options.objects.filter(mortgage_loan=mortgage_loan).filter(
                fin_prdt_cd = option['fin_prdt_cd'],
                mrtg_type = option['mrtg_type'] ,
                mrtg_type_nm = option['mrtg_type_nm'] ,
                rpay_type = option['rpay_type'] ,
                rpay_type_nm = option['rpay_type_nm'] ,
                lend_rate_type = option['lend_rate_type'] ,
                lend_rate_type_nm = option['lend_rate_type_nm'] ,
                lend_rate_min = option['lend_rate_min'] ,
                lend_rate_max = option['lend_rate_max'] ,
                lend_rate_avg = option['lend_rate_avg'] ,
            ).exists():
                option_serializer = MortgageOptionSerializer(data=option)
                if option_serializer.is_valid(raise_exception=True):
                    option_serializer.save(mortgage_loan=mortgage_loan)

                # 상품 카테고리 생성
                mortgage_category = Mortgage_Category()
                
                mortgage_category.mrtg_type = option['mrtg_type']
                
                mortgage_category.rpay_type = option['rpay_type']
                
                mortgage_category.lend_rate_type = option['lend_rate_type']

                if not option['lend_rate_min']:
                    mortgage_category.lend_rate_min = option['lend_rate_min']
                else:
                    mortgage_category.lend_rate_min = str(floor(option['lend_rate_min']))
                
                
                if not option['lend_rate_max']:
                    mortgage_category.lend_rate_max = option['lend_rate_max']
                else:
                    mortgage_category.lend_rate_max = str(floor(option['lend_rate_max']))
  
                if Mortgage_Category.objects.filter(
                        mrtg_type = mortgage_category.mrtg_type,
                        rpay_type = mortgage_category.rpay_type,
                        lend_rate_type = mortgage_category.lend_rate_type,
                        lend_rate_min = mortgage_category.lend_rate_min,
                        lend_rate_max = mortgage_category.lend_rate_max
                    ).exists():
                        mortgage_category = Mortgage_Category.objects.filter(
                        mrtg_type = mortgage_category.mrtg_type,
                        rpay_type = mortgage_category.rpay_type,
                        lend_rate_type = mortgage_category.lend_rate_type,
                        lend_rate_min = mortgage_category.lend_rate_min,
                        lend_rate_max = mortgage_category.lend_rate_max
                    )[0]
                else:        
                    mortgage_category.save()
        
                if not mortgage_loan.mortgage_category.filter(
                    mrtg_type = mortgage_category.mrtg_type,
                    rpay_type = mortgage_category.rpay_type,
                    lend_rate_type = mortgage_category.lend_rate_type,
                    lend_rate_min = mortgage_category.lend_rate_min,
                    lend_rate_max = mortgage_category.lend_rate_max
                ).exists():
                    mortgage_loan.mortgage_category.add(mortgage_category)
            
        # mortgage output data setting
        mortgages = Mortgage_Loan.objects.all()
        for mortgage in mortgages:
            for option in mortgage.options.all():
                mortgage_output = Mortgage_Output()
                
                mortgage_output.lend_rate_min = option.lend_rate_min
                mortgage_output.lend_rate_max = option.lend_rate_max
                mortgage_output.mrtg_type_nm = option.mrtg_type_nm
                mortgage_output.rpay_type_nm = option.rpay_type_nm
                mortgage_output.lend_rate_type_nm = option.lend_rate_type_nm
                
                mortgage_output.kor_co_nm = mortgage.kor_co_nm
                mortgage_output.fin_prdt_nm = mortgage.fin_prdt_nm
                mortgage_output.join_way = mortgage.join_way
                mortgage_output.mortgage = mortgage
                mortgage_output.save()
                    
        return Response({ 'message': 'Mortgage 저장 완료' })


@api_view(['GET',])
@permission_classes([AllowAny])
def mortgage_detail(request, mortgage_pk):
    if request.method == 'GET':
        mortgage = Mortgage_Loan.objects.get(pk=mortgage_pk)
        serializer = MortgageSerializer(mortgage)
        return Response(serializer.data)


@api_view(['GET', 'POST',])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def mortgage_save(request, mortgage_pk):
    if request.method == 'GET':
        mortgage = Mortgage_Loan.objects.get(pk=mortgage_pk)
        categories = mortgage.mortgage_category.all()
        
        recommend_mortgage = set()
        
        for category in categories:
            for category_mortgage in category.mortgages.all():
                if category_mortgage != mortgage:
                    recommend_mortgage.add(category_mortgage)
        
        recommend_mortgage = list(recommend_mortgage)
        
        serializer = MortgageSerializer(recommend_mortgage, many=True)
        
        return Response(serializer.data)
    

    elif request.method =='POST':
        user = get_user_model().objects.get(username=request.user.username)
        mortgage = Mortgage_Loan.objects.get(pk=mortgage_pk)
        if user.mortgage.filter(fin_prdt_cd=mortgage.fin_prdt_cd).exists(): 
            user.mortgage.remove(mortgage)        
            return Response({'message':'저장취소'})
        else :
            user.mortgage.add(mortgage)
            return Response({'message':'저장완료'})



@api_view(['GET', 'POST',])
@permission_classes([AllowAny])
# @permission_classes([IsAuthenticated])
def jeonse(request):
    if request.method == 'GET':
        joinWay = request.GET.get('joinWay')
        repayWay = request.GET.get('repayWay')
        rateType = request.GET.get('rateType')
        amount = int(request.GET.get('amount'))
        period = int(request.GET.get('period'))
        
        if joinWay == 'all':
            filtered_join_way_jeonses = Jeonse_Output.objects.all()
        elif joinWay == 'online':
            filtered_join_way_jeonses = Jeonse_Output.objects.filter(join_way__contains='인터넷') \
                | Jeonse_Output.objects.filter(join_way__contains='스마트폰') 
        elif joinWay == 'visit':
            filtered_join_way_jeonses = Jeonse_Output.objects.filter(join_way__contains='영업점')

        if repayWay == '1':
            filtered_repay_way_jeonses = filtered_join_way_jeonses.filter(rpay_type_nm='분할상환방식')
        elif repayWay == '2':
            filtered_repay_way_jeonses = filtered_join_way_jeonses.filter(rpay_type_nm='만기일시상환방식')

        if rateType == '1':
            jeonses = filtered_repay_way_jeonses.filter(lend_rate_type_nm='고정금리')
        elif rateType == '2':
            jeonses = filtered_repay_way_jeonses.filter(lend_rate_type_nm='변동금리')
            
        for jeonse in jeonses:
            jeonse.loan_interest_min = ((amount * (float(jeonse.lend_rate_min) * 0.01))) / (12 * period)
            jeonse.loan_interest_max = ((amount * (float(jeonse.lend_rate_max) * 0.01))) / (12 * period)
            
            jeonse.save()     
        
        serializer = JeonseOutputSerializer(jeonses, many=True)
        
        return Response(serializer.data)


    elif request.method == 'POST':
        api_key = settings.FINANCE_API_KEY
        url = f'http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
        response = requests.get(url).json()

        products = response['result'].get('baseList')
        for product in products:
            bank = ''
            if Bank.objects.filter(fin_co_no=product['fin_co_no']).exists():
                bank = Bank.objects.get(fin_co_no=product['fin_co_no'])

            if not Jeonse_Loan.objects.filter(fin_prdt_cd=product['fin_prdt_cd']).exists():
                jeonse_serializer = JeonseSerializer(data=product)
                if jeonse_serializer.is_valid(raise_exception=True):
                    jeonse_serializer.save(bank=bank)                    

        options = response['result'].get('optionList')
        for option in options:
            jeonse_loan = Jeonse_Loan.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
            if not Jeonse_Options.objects.filter(jeonse_loan=jeonse_loan).filter(
                fin_prdt_cd = option['fin_prdt_cd'],
                rpay_type = option['rpay_type'] ,
                rpay_type_nm = option['rpay_type_nm'] ,
                lend_rate_type = option['lend_rate_type'] ,
                lend_rate_type_nm = option['lend_rate_type_nm'] ,
                lend_rate_min = option['lend_rate_min'] ,
                lend_rate_max = option['lend_rate_max'] ,
                lend_rate_avg = option['lend_rate_avg']
            ).exists():
                option_serializer = JeonseOptionSerializer(data=option)
                if option_serializer.is_valid(raise_exception=True):
                    option_serializer.save(jeonse_loan=jeonse_loan)
                    
                # 상품 카테고리 생성
                jeonse_category = Jeonse_Category()
                
                jeonse_category.rpay_type = option['rpay_type']
                
                jeonse_category.lend_rate_type = option['lend_rate_type']

                if not option['lend_rate_min']:
                    jeonse_category.lend_rate_min = option['lend_rate_min']
                else:
                    jeonse_category.lend_rate_min = str(floor(option['lend_rate_min']))
                
                
                if not option['lend_rate_max']:
                    jeonse_category.lend_rate_max = option['lend_rate_max']
                else:
                    jeonse_category.lend_rate_max = str(floor(option['lend_rate_max']))

                if Jeonse_Category.objects.filter(
                    rpay_type = jeonse_category.rpay_type,
                    lend_rate_type = jeonse_category.lend_rate_type,
                    lend_rate_min = jeonse_category.lend_rate_min,
                    lend_rate_max = jeonse_category.lend_rate_max
                ).exists():
                    jeonse_category = Jeonse_Category.objects.filter(
                    rpay_type = jeonse_category.rpay_type,
                    lend_rate_type = jeonse_category.lend_rate_type,
                    lend_rate_min = jeonse_category.lend_rate_min,
                    lend_rate_max = jeonse_category.lend_rate_max
                )[0]
                
                else:        
                    jeonse_category.save()
        
                if not jeonse_loan.jeonse_category.filter(
                    rpay_type = jeonse_category.rpay_type,
                    lend_rate_type = jeonse_category.lend_rate_type,
                    lend_rate_min = jeonse_category.lend_rate_min,
                    lend_rate_max = jeonse_category.lend_rate_max
                ).exists():
                    jeonse_loan.jeonse_category.add(jeonse_category)
                    
        # jeonse output data setting
        jeonses = Jeonse_Loan.objects.all()
        for jeonse in jeonses:
            for option in jeonse.options.all():
                jeonse_output = Jeonse_Output()
                
                jeonse_output.lend_rate_min = option.lend_rate_min
                jeonse_output.lend_rate_max = option.lend_rate_max
                jeonse_output.rpay_type_nm = option.rpay_type_nm
                jeonse_output.lend_rate_type_nm = option.lend_rate_type_nm
                
                jeonse_output.kor_co_nm = jeonse.kor_co_nm
                jeonse_output.fin_prdt_nm = jeonse.fin_prdt_nm
                jeonse_output.join_way = jeonse.join_way
                jeonse_output.jeonse = jeonse
                jeonse_output.save()
                    
        return Response({ 'message': 'Jeonse 저장 완료' })
    
    
@api_view(['GET',])
@permission_classes([AllowAny])
def jeonse_detail(request, jeonse_pk):
    if request.method == 'GET':
        jeonse = Jeonse_Loan.objects.get(pk=jeonse_pk)
        serializer = JeonseSerializer(jeonse)
        return Response(serializer.data)


@api_view(['GET', 'POST',])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def jeonse_save(request, jeonse_pk):
    if request.method == 'GET':
        jeonse = Jeonse_Loan.objects.get(pk=jeonse_pk)
        categories = jeonse.jeonse_category.all()
        
        recommend_jeonse = set()
        
        for category in categories:
            for category_jeonse in category.jeonses.all():
                if category_jeonse != jeonse:
                    recommend_jeonse.add(category_jeonse)
        
        recommend_jeonse = list(recommend_jeonse)
        
        serializer = JeonseSerializer(recommend_jeonse, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        user = get_user_model().objects.get(username=request.user.username)
        jeonse = Jeonse_Loan.objects.get(pk=jeonse_pk)
        if user.jeonse.filter(fin_prdt_cd=jeonse.fin_prdt_cd).exists(): 
            user.jeonse.remove(jeonse)        
            return Response({'message':'저장취소'})
        else :
            user.jeonse.add(jeonse)
            return Response({'message':'저장완료'})
   

@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_recommend_deposit(request):
    if request.method == 'GET':

        login_user = get_user_model().objects.get(username=request.user.username)
        
        users_age_gender = get_user_model().objects.filter(
                gender = login_user.gender
            )&get_user_model().objects.filter(
                age__range = (login_user.age - 3, login_user.age + 3)
            )

        users_salary = get_user_model().objects.filter(
            salary__range = (login_user.salary - 300, login_user.salary + 300)
        )

        user_list = set()

        for user in users_age_gender:
            user_list.add(user)
        
        for user in users_salary:
            user_list.add(user)

        recommend_products = set()

        
        for user in list(user_list):
            for deposit in user.deposit.all():
                if deposit not in login_user.deposit.all():
                    recommend_products.add(deposit)
        
        recommend_products = list(recommend_products)    

        serializer = DepositSerializer(recommend_products, many=True)

        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_recommend_savings(request):
    if request.method == 'GET':

        login_user = get_user_model().objects.get(username=request.user.username)
        
        users_age_gender = get_user_model().objects.filter(
                gender = login_user.gender
            )&get_user_model().objects.filter(
                age__range = (login_user.age - 3, login_user.age + 3)
            )

        users_salary = get_user_model().objects.filter(
            salary__range = (login_user.salary - 300, login_user.salary + 300)
        )

        user_list = set()

        for user in users_age_gender:
            user_list.add(user)
        
        for user in users_salary:
            user_list.add(user)

        recommend_products = set()

        for user in list(user_list):
            for savings in user.savings.all():
                if savings not in login_user.savings.all():
                    recommend_products.add(savings)
        
        recommend_products = list(recommend_products)    

        serializer = SavingSerializer(recommend_products, many=True)

        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_recommend_personal(request):
    if request.method == 'GET':

        login_user = get_user_model().objects.get(username=request.user.username)
        
        users_age_gender = get_user_model().objects.filter(
                gender = login_user.gender
            )&get_user_model().objects.filter(
                age__range = (login_user.age - 3, login_user.age + 3)
            )

        users_salary = get_user_model().objects.filter(
            salary__range = (login_user.salary - 300, login_user.salary + 300)
        )

        user_list = set()

        for user in users_age_gender:
            user_list.add(user)
        
        for user in users_salary:
            user_list.add(user)

        recommend_products = set()

        for user in list(user_list):
            for personal in user.personal.all():
                if personal not in login_user.personal.all():
                    recommend_products.add(personal)
        
        recommend_products = list(recommend_products)    

        serializer = PersonalSerializer(recommend_products, many=True)

        return Response(serializer.data)
    

@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_recommend_mortgage(request):
    if request.method == 'GET':

        login_user = get_user_model().objects.get(username=request.user.username)
        
        users_age_gender = get_user_model().objects.filter(
                gender = login_user.gender
            )&get_user_model().objects.filter(
                age__range = (login_user.age - 3, login_user.age + 3)
            )

        users_salary = get_user_model().objects.filter(
            salary__range = (login_user.salary - 300, login_user.salary + 300)
        )

        user_list = set()

        for user in users_age_gender:
            user_list.add(user)
        
        for user in users_salary:
            user_list.add(user)

        recommend_products = set()

        for user in list(user_list):
            for mortgage in user.mortgage.all():
                if mortgage not in login_user.mortgage.all():
                    recommend_products.add(mortgage)
        
        recommend_products = list(recommend_products)    

        serializer = MortgageSerializer(recommend_products, many=True)

        return Response(serializer.data)


@api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_recommend_jeonse(request):
    if request.method == 'GET':

        login_user = get_user_model().objects.get(username=request.user.username)
        
        users_age_gender = get_user_model().objects.filter(
                gender = login_user.gender
            )&get_user_model().objects.filter(
                age__range = (login_user.age - 3, login_user.age + 3)
            )

        users_salary = get_user_model().objects.filter(
            salary__range = (login_user.salary - 300, login_user.salary + 300)
        )

        user_list = set()

        for user in users_age_gender:
            user_list.add(user)
        
        for user in users_salary:
            user_list.add(user)

        recommend_products = set()

        for user in list(user_list):
            for jeonse in user.jeonse.all():
                if jeonse not in login_user.jeonse.all():
                    recommend_products.add(jeonse)
        
        recommend_products = list(recommend_products)    

        serializer = JeonseSerializer(recommend_products, many=True)

        return Response(serializer.data)

# 검색 기능 구현
@api_view(['GET',])
@permission_classes([AllowAny])
def deposit_search(request, keyword):
    deposits = Deposit.objects.filter(fin_prdt_nm__contains=keyword) | Deposit.objects.filter(kor_co_nm__contains=keyword) 
    deposit_serializer = DepositSerializer(deposits, many=True)
    return Response(deposit_serializer.data)


@api_view(['GET',])
@permission_classes([AllowAny])
def savings_search(request, keyword):
    savings = Savings.objects.filter(fin_prdt_nm__contains=keyword) | Savings.objects.filter(kor_co_nm__contains=keyword)  
    savings_serializer = SavingSerializer(savings, many=True)
    return Response(savings_serializer.data)


@api_view(['GET',])
@permission_classes([AllowAny])
def personal_search(request, keyword):
    personals = Personal_Credit_Loan.objects.filter(fin_prdt_nm__contains=keyword) | Personal_Credit_Loan.objects.filter(kor_co_nm__contains=keyword)    
    personal_serializer = PersonalSerializer(personals, many=True)
    return Response(personal_serializer.data)


@api_view(['GET',])
@permission_classes([AllowAny])
def mortgage_search(request, keyword):
    mortgages = Mortgage_Loan.objects.filter(fin_prdt_nm__contains=keyword) | Mortgage_Loan.objects.filter(kor_co_nm__contains=keyword)    
    mortgage_serializer = MortgageSerializer(mortgages, many=True)
    return Response(mortgage_serializer.data)


@api_view(['GET',])
@permission_classes([AllowAny])
def jeonse_search(request, keyword):
    jeonses = Jeonse_Loan.objects.filter(fin_prdt_nm__contains=keyword) | Jeonse_Loan.objects.filter(kor_co_nm__contains=keyword)    
    jeonse_serializer = JeonseSerializer(jeonses, many=True)
    return Response(jeonse_serializer.data)


@api_view(['GET',])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_join_deposit(request):
    if request.method == 'GET':
        user = get_user_model().objects.get(username=request.user.username)
        deposits = user.deposit.all()
        serializer = DepositSerializer(deposits, many=True)
        return Response(serializer.data)


@api_view(['GET',])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_join_savings(request):
    if request.method == 'GET':
        user = get_user_model().objects.get(username=request.user.username)
        savings = user.savings.all()
        serializer = SavingSerializer(savings, many=True)
        return Response(serializer.data)
    

@api_view(['GET',])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_join_personal(request):
    if request.method == 'GET':
        user = get_user_model().objects.get(username=request.user.username)
        personals = user.personal.all()
        serializer = PersonalSerializer(personals, many=True)
        return Response(serializer.data)


@api_view(['GET',])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_join_mortgage(request):
    if request.method == 'GET':
        user = get_user_model().objects.get(username=request.user.username)
        mortgages = user.mortgage.all()
        serializer = MortgageSerializer(mortgages, many=True)
        return Response(serializer.data)


@api_view(['GET',])
# @permission_classes([AllowAny])
@permission_classes([IsAuthenticated])
def user_join_jeonse(request):
    if request.method == 'GET':
        user = get_user_model().objects.get(username=request.user.username)
        jeonses = user.jeonse.all()
        serializer = JeonseSerializer(jeonses, many=True)
        return Response(serializer.data)













