from django.contrib import admin
from .models import Account_transaction #don't imported Account_Journal

# class Bank_Page(admin.TabularInline):
#     date_hierarchy = 'pub_date'
#     model = Account_Journal
#     extra = 5
#
#
# class AccountAdmin(admin.ModelAdmin):
#     inlines = [Bank_Page]
#     list_filter = ['bank_account_title','account_transaction_date']


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ['bank_account_title', 'account_transaction_date']



admin.site.register(Account_transaction,AuthorAdmin)
