from django.contrib import admin
from .models import Account_Journal,Account_transaction

class Bank_Page(admin.StackedInline):
    date_hierarchy = 'pub_date'
    model = Account_Journal
    extra = 5


class ManageAdmin(admin.ModelAdmin):
    inlines = [Bank_Page]
    list_filter = ['bank_account_title','account_transaction_date']


admin.site.register(Account_transaction,ManageAdmin)
