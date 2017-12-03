from django.db import models
from django.utils import timezone


class Account_transaction(models.Model):
    class Meta():
        db_table = 'all transaction'

    ACCOUNT_JOURNAL_STATUS = (('+', 'Приход'), ('-', 'Расход'))
    ACCOUNT_TRANSACTION_CURRENCY = (('USD', 'dollars'), ('EUR', 'euro'), ('RUR', 'rubles'))
    TEXT_TITLE = "Введите имя счета, например: Основной \n Валютный \n Сберегательный"
    TEXT_EXP = "Введите статью расходов или источник дохода"
    account_jornal_status = models.CharField(max_length=10, verbose_name='Operation status:', default='Приход',choices=ACCOUNT_JOURNAL_STATUS)
    bank_account_title = models.CharField(verbose_name='Account Name:',max_length=30,blank=True, help_text=TEXT_TITLE)
    account_transaction_expenditure_name = models.CharField(verbose_name='Expenditure name:',max_length=30,help_text=TEXT_EXP)
    account_transaction_date = models.DateTimeField(verbose_name='Date/time:',default=timezone.now)
    account_transaction_currency = models.CharField(verbose_name='Currency:',max_length=10,blank=True,default='rubles',choices=ACCOUNT_TRANSACTION_CURRENCY)
    account_transaction_amount = models.IntegerField(verbose_name='Amount:',default=0)
    account_transaction_comment = models.CharField(verbose_name='comment:',max_length=30,default="comment...")



# class Account_Journal(models.Model):
#     class Meta():
#         db_table = 'bank account journal'
#     account_jornal_amount = models.CharField(max_length=30)
#     ACCOUNT_JOURNAL_STATUS = (('+', 'Приход'), ('-', 'Расход'))
#     account_jornal_status = models.CharField(max_length=10, choices=ACCOUNT_JOURNAL_STATUS)
#     bank_account_transaction = models.ForeignKey(Account_transaction)



# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)
#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
