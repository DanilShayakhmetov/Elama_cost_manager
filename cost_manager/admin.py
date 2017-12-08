from django.contrib import admin
from .models import Account_transaction, Bank_Account #don't imported Account_Journal

class Bank_Page(admin.TabularInline):
    date_hierarchy = 'pub_date'
    model = Account_transaction
    list_filter = ['bank_account_title', 'account_transaction_date']
    extra = 1

#
#
# class AccountAdmin(admin.ModelAdmin):
#     inlines = [Bank_Page]
#     list_filter = ['bank_account_title','account_transaction_date']


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['bank_account_title']
    fields = ['bank_account_title','bank_account_balance']
    inlines = [Bank_Page]


admin.site.register(Bank_Account,AuthorAdmin)
