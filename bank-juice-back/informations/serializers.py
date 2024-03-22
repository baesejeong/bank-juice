from rest_framework import serializers
from .models import Bank
from .models import Deposit, Deposit_Options, Savings, Savings_Options, Exchange
from .models import Personal_Credit_Loan, Personal_Options, Mortgage_Loan, Mortgage_Options, Jeonse_Loan, Jeonse_Options
from .models import Deposit_Output, Savings_Output, Personal_Output, Mortgage_Output, Jeonse_Output
from django.contrib.auth import get_user_model

class BankSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Bank
        fields = '__all__'


class PersonalOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Options
        fields = '__all__'
        read_only_fields = ('personal_credit_loan',)


class PersonalSerializer(serializers.ModelSerializer):
    options = PersonalOptionSerializer(many=True, read_only=True)
    class Meta : 
        model = Personal_Credit_Loan
        fields = '__all__'
        read_only_fields = ('bank','personal_category',)


class PersonalOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal_Output
        fields = '__all__'
        read_only_fields = ('personal',)


class MortgageOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortgage_Options
        fields = '__all__'
        read_only_fields = ('mortgage_loan',)

class MortgageSerializer(serializers.ModelSerializer):
    options = MortgageOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Mortgage_Loan
        fields = '__all__'
        read_only_fields = ('bank','mortgage_category',)


class MortgageOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortgage_Output
        fields = '__all__'
        read_only_fields = ('mortgage',)


class JeonseOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jeonse_Options
        fields = '__all__'
        read_only_fields = ('jeonse_loan',)

class JeonseSerializer(serializers.ModelSerializer):
    options = JeonseOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Jeonse_Loan
        fields = '__all__'
        read_only_fields = ('bank','jeonse_category',)


class JeonseOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jeonse_Output
        fields = '__all__'
        read_only_fields = ('jeonse',)

        
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit_Options
        fields = '__all__'
        read_only_fields = ('deposit',)


class DepositSerializer(serializers.ModelSerializer):
    options = DepositOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Deposit
        fields = '__all__'
        read_only_fields = ('bank', 'deposit_category',)


class DepositOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit_Output
        fields = '__all__'
        read_only_fields = ('deposit',)


class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings_Options
        fields = '__all__'
        read_only_fields = ('savings',)


class SavingSerializer(serializers.ModelSerializer):
    options = SavingOptionSerializer(many=True, read_only=True)
    class Meta:
        model = Savings
        fields = '__all__'
        read_only_fields = ('bank','savings_category',)


class SavingsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Savings_Output
        fields = '__all__'
        read_only_fields = ('savings',)


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'