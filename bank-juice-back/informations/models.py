from django.db import models

# Create your models here.
class Bank(models.Model):
    fin_co_no = models.CharField(max_length=250)
    homp_url = models.CharField(max_length=250)
    cal_tel = models.CharField(max_length=250)
    kor_co_nm = models.CharField(max_length=250)
    dcls_month  = models.CharField(max_length=250)
    dcls_chrg_man = models.CharField(max_length=250)


class Deposit_Category(models.Model):
    intr_rate = models.CharField(max_length=10, null=True, blank=True)
    intr_rate2 = models.CharField(max_length=10, null=True, blank=True)
    intr_rate_type = models.CharField(max_length=10)
    save_trm = models.CharField(max_length=10)


class Deposit(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='deposit')
    fin_co_no = models.CharField(max_length=250)
    fin_co_subm_day = models.CharField(max_length=250)
    fin_prdt_cd = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_deny = models.CharField(max_length=250)
    join_member = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)
    dcls_month = models.CharField(max_length=250)
    dcls_strt_day = models.CharField(max_length=250)
    dcls_end_day = models.CharField(max_length=250, null=True, blank=True)
    etc_note = models.CharField(max_length=250)
    kor_co_nm = models.CharField(max_length=250)
    max_limit = models.CharField(max_length=250, null=True, blank=True)
    mtrt_int = models.CharField(max_length=250)
    spcl_cnd = models.CharField(max_length=250)
    deposit_category = models.ManyToManyField(Deposit_Category, related_name='deposits')


class Deposit_Options(models.Model):
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.CharField(max_length=250)
    intr_rate = models.FloatField(null=True, blank=True)
    intr_rate2 = models.FloatField(null=True, blank=True)
    intr_rate_type = models.CharField(max_length=250)
    intr_rate_type_nm = models.CharField(max_length=250)
    save_trm = models.CharField(max_length=250)


class Deposit_Output(models.Model):
    deposit = models.ForeignKey(Deposit, on_delete=models.CASCADE, related_name='outputs')
    intr_rate_6 = models.FloatField(null=True, blank=True)
    intr_rate_12 = models.FloatField(null=True, blank=True)
    interest_before_tax = models.IntegerField(null=True, blank=True, default=0)
    interest_after_tax = models.IntegerField(null=True, blank=True, default=0)
    intr_rate_24 = models.FloatField(null=True, blank=True)
    intr_rate_36 = models.FloatField(null=True, blank=True)
    kor_co_nm = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)


class Savings_Category(models.Model):
    intr_rate = models.CharField(max_length=10, null=True, blank=True)
    intr_rate2 = models.CharField(max_length=10, null=True, blank=True)
    intr_rate_type = models.CharField(max_length=10)
    rsrv_type = models.CharField(max_length=10)
    save_trm = models.CharField(max_length=10)


class Savings(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='savings', null=True, blank=True)
    fin_co_no = models.CharField(max_length=250)
    fin_co_subm_day = models.CharField(max_length=250)
    fin_prdt_cd = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_deny = models.CharField(max_length=250)
    join_member = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)
    dcls_month = models.CharField(max_length=250)
    dcls_strt_day = models.CharField(max_length=250)
    dcls_end_day = models.CharField(max_length=250, null=True, blank=True)
    etc_note = models.CharField(max_length=250)
    kor_co_nm = models.CharField(max_length=250)
    max_limit = models.CharField(max_length=250, null=True, blank=True)
    mtrt_int = models.CharField(max_length=250)
    spcl_cnd = models.CharField(max_length=250)
    savings_category = models.ManyToManyField(Savings_Category, related_name='savings')


class Savings_Options(models.Model):
    savings = models.ForeignKey(Savings, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.CharField(max_length=250)
    intr_rate = models.FloatField(null=True, blank=True)
    intr_rate2 = models.FloatField(null=True, blank=True)
    intr_rate_type = models.CharField(max_length=250)
    intr_rate_type_nm = models.CharField(max_length=250)
    rsrv_type = models.CharField(max_length=250)
    rsrv_type_nm = models.CharField(max_length=250)
    save_trm = models.CharField(max_length=250)



class Savings_Output(models.Model):
    savings = models.ForeignKey(Savings, on_delete=models.CASCADE)
    intr_rate_6 = models.FloatField(null=True, blank=True)
    intr_rate_12 = models.FloatField(null=True, blank=True)
    interest_before_tax = models.IntegerField(null=True, blank=True, default=0)
    interest_after_tax = models.IntegerField(null=True, blank=True, default=0)
    intr_rate_24 = models.FloatField(null=True, blank=True)
    intr_rate_36 = models.FloatField(null=True, blank=True)
    kor_co_nm = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)


class Personal_Category(models.Model):
    crdt_lend_rate_type = models.CharField(max_length=10)


class Personal_Credit_Loan(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='personal', null=True, blank=True)
    fin_co_no = models.CharField(max_length=250)
    crdt_prdt_type = models.CharField(max_length=250)
    crdt_prdt_type_nm = models.CharField(max_length=250)
    dcls_end_day = models.CharField(max_length=250, null=True, blank=True)
    dcls_strt_day = models.CharField(max_length=250)
    fin_co_subm_day = models.CharField(max_length=250)
    fin_prdt_cd = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)
    kor_co_nm = models.CharField(max_length=250)
    cb_name = models.CharField(max_length=250)
    personal_category = models.ManyToManyField(Personal_Category, related_name='personals')

    
class Personal_Options(models.Model):
    personal_credit_loan = models.ForeignKey(Personal_Credit_Loan, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.CharField(max_length=250)
    crdt_lend_rate_type = models.CharField(max_length=250)
    crdt_lend_rate_type_nm = models.CharField(max_length=250)
    crdt_grad_1 = models.FloatField(null=True, blank=True)
    crdt_grad_4 = models.FloatField(null=True, blank=True)
    crdt_grad_5 = models.FloatField(null=True, blank=True)
    crdt_grad_6 = models.FloatField(null=True, blank=True)
    crdt_grad_10 = models.FloatField(null=True, blank=True)
    crdt_grad_11 = models.FloatField(null=True, blank=True)
    crdt_grad_12 = models.FloatField(null=True, blank=True)
    crdt_grad_13 = models.FloatField(null=True, blank=True)
    crdt_grad_avg = models.FloatField(null=True, blank=True)

class Personal_Output(models.Model):
    personal = models.ForeignKey(Personal_Credit_Loan, on_delete=models.CASCADE)
    # 900점 초과
    crdt_grad_1 = models.FloatField(null=True, blank=True)
    # 801 ~ 900
    crdt_grad_4 = models.FloatField(null=True, blank=True)
    # 701 ~ 800
    crdt_grad_5 = models.FloatField(null=True, blank=True)
    # 601 ~ 700
    crdt_grad_6 = models.FloatField(null=True, blank=True)
    # 501 ~ 600
    crdt_grad_10 = models.FloatField(null=True, blank=True)
    # 401 ~ 500
    crdt_grad_11 = models.FloatField(null=True, blank=True)
    # 301 ~ 400
    crdt_grad_12 = models.FloatField(null=True, blank=True)
    # 300점 이하
    crdt_grad_13 = models.FloatField(null=True, blank=True)
    # 평균 금리
    crdt_grad_avg = models.FloatField(null=True, blank=True)
    crdt_lend_rate_type_nm = models.CharField(max_length=250, null=True, blank=True)
    loan_interest = models.IntegerField(null=True, blank=True, default=0)
    kor_co_nm = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)
    rate = models.CharField(max_length=10)


class Mortgage_Category(models.Model):
    mrtg_type = models.CharField(max_length=10)
    rpay_type = models.CharField(max_length=10)
    lend_rate_type = models.CharField(max_length=10)
    lend_rate_min = models.CharField(max_length=10, null=True, blank=True)
    lend_rate_max = models.CharField(max_length=10, null=True, blank=True)


class Mortgage_Loan(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='mortgage')
    fin_co_no = models.CharField(max_length=250)
    dcls_month=models.CharField(max_length=250)
    kor_co_nm = models.CharField(max_length=250)
    fin_prdt_cd = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)
    loan_inci_expan = models.CharField(max_length=250, null=True, blank=True)
    erly_rpay_fee = models.CharField(max_length=250)
    fin_prdt_type_nm = models.CharField(max_length=250, null=True, blank=True)
    dly_rate = models.CharField(max_length=250)
    loan_lmt = models.CharField(max_length=250)
    dcls_strt_day = models.CharField(max_length=250)
    dcls_end_day = models.CharField(max_length=250, null=True, blank=True)
    fin_co_subm_day = models.CharField(max_length=250)
    mortgage_category = models.ManyToManyField(Mortgage_Category, related_name='mortgages')


class Mortgage_Options(models.Model) :
    mortgage_loan = models.ForeignKey(Mortgage_Loan, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.CharField(max_length=250)
    mrtg_type = models.CharField(max_length=250)
    mrtg_type_nm = models.CharField(max_length=250)
    rpay_type = models.CharField(max_length=250)
    rpay_type_nm = models.CharField(max_length=250)
    lend_rate_type = models.CharField(max_length=250)
    lend_rate_type_nm = models.CharField(max_length=250)
    lend_rate_min = models.CharField(max_length=250)
    lend_rate_max = models.CharField(max_length=250)
    lend_rate_avg = models.CharField(max_length=250, null=True, blank=True)


class Mortgage_Output(models.Model):
    mortgage = models.ForeignKey(Mortgage_Loan, on_delete=models.CASCADE)
    lend_rate_min = models.FloatField(null=True, blank=True)
    lend_rate_max = models.FloatField(null=True, blank=True)
    loan_interest_min = models.IntegerField(null=True, blank=True, default=0)
    loan_interest_max = models.IntegerField(null=True, blank=True, default=0)
    mrtg_type_nm = models.CharField(max_length=250)
    rpay_type_nm = models.CharField(max_length=250)
    lend_rate_type_nm = models.CharField(max_length=250)
    kor_co_nm = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)


class Jeonse_Category(models.Model):
    rpay_type = models.CharField(max_length=10)
    lend_rate_type = models.CharField(max_length=10)
    lend_rate_min = models.CharField(max_length=10, null=True, blank=True)
    lend_rate_max = models.CharField(max_length=10, null=True, blank=True)


class Jeonse_Loan(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='jeonse')
    fin_co_no = models.CharField(max_length=250)
    dcls_month=models.CharField(max_length=250)
    kor_co_nm = models.CharField(max_length=250)
    fin_prdt_cd = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)
    loan_inci_expan = models.CharField(max_length=250, null=True, blank=True)
    erly_rpay_fee = models.CharField(max_length=250)
    fin_prdt_type_nm = models.CharField(max_length=250, null=True, blank=True)
    dly_rate = models.CharField(max_length=250)
    loan_lmt = models.CharField(max_length=250)
    dcls_strt_day = models.CharField(max_length=250)
    dcls_end_day = models.CharField(max_length=250, null=True, blank=True)
    fin_co_subm_day = models.CharField(max_length=250)
    jeonse_category = models.ManyToManyField(Jeonse_Category, related_name='jeonses')


class Jeonse_Options(models.Model) :
    jeonse_loan = models.ForeignKey(Jeonse_Loan, on_delete=models.CASCADE, related_name='options')
    fin_prdt_cd = models.CharField(max_length=250)
    rpay_type = models.CharField(max_length=250)
    rpay_type_nm = models.CharField(max_length=250)
    lend_rate_type = models.CharField(max_length=250)
    lend_rate_type_nm = models.CharField(max_length=250)
    lend_rate_min = models.CharField(max_length=250)
    lend_rate_max = models.CharField(max_length=250)
    lend_rate_avg = models.CharField(max_length=250, null=True, blank=True)


class Jeonse_Output(models.Model):
    jeonse = models.ForeignKey(Jeonse_Loan, on_delete=models.CASCADE)
    lend_rate_min = models.FloatField(null=True, blank=True)
    lend_rate_max = models.FloatField(null=True, blank=True)
    loan_interest_min = models.IntegerField(null=True, blank=True, default=0)
    loan_interest_max = models.IntegerField(null=True, blank=True, default=0)
    kor_co_nm = models.CharField(max_length=250)
    fin_prdt_nm = models.CharField(max_length=250)
    rpay_type_nm = models.CharField(max_length=250)
    lend_rate_type_nm = models.CharField(max_length=250)
    join_way = models.CharField(max_length=250)   


class Exchange(models.Model):
    cur_unit = models.CharField(max_length=250, null=True, blank=True)
    cur_nm = models.CharField(max_length=250, null=True, blank=True)
    ttb = models.CharField(max_length=250, null=True, blank=True)
    tts = models.CharField(max_length=250, null=True, blank=True)
    deal_bas_r = models.CharField(max_length=250, null=True, blank=True)
    bkpr = models.CharField(max_length=250, null=True, blank=True)
    yy_efee_r = models.CharField(max_length=250, null=True, blank=True)
    ten_dd_efee_r = models.CharField(max_length=250, null=True, blank=True)
    kftc_deal_bas_r = models.CharField(max_length=250, null=True, blank=True)
    kftc_bkpr = models.CharField(max_length=250, null=True, blank=True)