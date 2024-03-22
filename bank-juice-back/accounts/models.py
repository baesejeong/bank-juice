from django.db import models
from django.contrib.auth.models import AbstractUser
from informations.models import Personal_Credit_Loan, Mortgage_Loan, Jeonse_Loan, Deposit, Savings
# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.BooleanField(default=True, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    
    # 사용자가 가입한 상품
    deposit = models.ManyToManyField(Deposit, related_name='users')
    savings = models.ManyToManyField(Savings, related_name='users')
    personal = models.ManyToManyField(Personal_Credit_Loan, related_name='users')
    mortgage = models.ManyToManyField(Mortgage_Loan, related_name='users')
    jeonse = models.ManyToManyField(Jeonse_Loan, related_name='users')

    
    #superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

