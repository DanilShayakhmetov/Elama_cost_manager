from django.db import models
from django.utils import timezone



class Account_transaction(models.Model):
    class Meta():
        db_table = 'all transaction'

    TEXT_TITLE = "Введите имя счета, например: Основной \n Валютный \n Сберегательный"
    TEXT_EXP = "Введите имя расхода, например: ЖКХ \n Продукты \n Перевод на чужую карту"
    bank_account_title = models.CharField(max_length=30,blank=True, help_text=TEXT_TITLE)
    account_transaction_expenditure_name = models.CharField(max_length=30,help_text=TEXT_EXP)
    account_transaction_date = models.DateTimeField(default=timezone.now)
    ACCOUNT_TRANSACTION_CURRENCY =(('USD', 'dollars'), ('EUR', 'euro'),('RUR', 'rubles'))
    account_transaction_currency = models.CharField(max_length=10,blank=True,choices=ACCOUNT_TRANSACTION_CURRENCY)



class Account_Journal(models.Model):
    class Meta():
        db_table = 'bank account journal'
    account_jornal_amount = models.CharField(max_length=30)
    ACCOUNT_JOURNAL_STATUS = (('+', 'Приход'), ('-', 'Расход'))
    account_jornal_status = models.CharField(max_length=10, choices=ACCOUNT_JOURNAL_STATUS)
    bank_account_transaction = models.ForeignKey(Account_transaction)



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
