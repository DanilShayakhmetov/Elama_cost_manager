from django.forms import ModelForm
from cost_manager.models import Account_transaction, Bank_Account
from django import forms

# from django.forms.extras.widgets import SelectDateWidget
#
# BIRTH_YEAR_CHOICES = (('1','1980'),('2', '1981'), ('3','1982'))
# FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
#                             ('green', 'Green'),
#                             ('black', 'Black'))
#
# class SimpleForm(forms.Form):
#     birth_year = forms.MultipleChoiceField(required=False, widget=forms.Select, choices = BIRTH_YEAR_CHOICES)
#     favorite_colors = forms.MultipleChoiceField(required=False,
#         widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
#     comment = forms.CharField(widget=forms.Textarea)





class AccountJournalStatus(ModelForm):
    class Meta():
        model = Account_transaction
        fields = ('account_jornal_status',)





class ExpenditureName(ModelForm):
    class Meta():
        model = Account_transaction
        fields = ('account_transaction_expenditure_name',)

class AccountDate(ModelForm):
    class Meta():
        model = Account_transaction
        fields = ('account_transaction_date',)


class AccountCurrency(ModelForm):
    class Meta():
        model = Account_transaction
        fields = ('account_transaction_currency',)

class AccountAmount(ModelForm):
    class Meta():
        model = Account_transaction
        fields = ('account_transaction_amount',)


class AccountComment(ModelForm):
    class Meta():
        model = Account_transaction
        fields = ('account_transaction_comment',)
