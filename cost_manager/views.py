# from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm
#
# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#
#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "/login/"
#
#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "register.html"
#
#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()
#
#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)
#
# # Create your views here.
from django.shortcuts import render_to_response
from cost_manager.forms import AccountJournalStatus, ExpenditureName,AccountDate,AccountCurrency,AccountAmount, AccountComment
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from cost_manager.models import Account_transaction,Bank_Account
from django.contrib import auth

@csrf_protect
def  TryToSave ( request, forma_id = 1):
    form = AccountComment(request.POST)
    sec_form = Account_transaction.objects.get(id = forma_id)
    if form.is_valid()and sec_form.is_valid():
        comment = form.save(commit=False)
        title = sec_form.save(commit=True)
        form.save()
        sec_form.save()

    return  render(request ,  "trytosave.html" ,  {'form':form},{'sec_form':sec_form})




@csrf_protect
def form_test(request, account_id = 1):
    user_name = auth.get_user(request).get_username()
    bank_account_id = Bank_Account.objects.get(id=account_id)
    account_title = bank_account_id.bank_account_title
    account_status = AccountJournalStatus(request.POST or None)
    account_date = AccountDate(request.POST or None)
    account_currency = AccountCurrency(request.POST or None)
    account_amount = AccountAmount(request.POST or None)
    account_comment = AccountComment(request.POST or None)
    expenditure_name = ExpenditureName(request.POST or None)
    args = {}
    args['username']  = user_name
    args['Title'] = account_title
    args['date'] = account_date
    args['currency'] = account_currency
    args['amount'] = account_amount
    args['comment'] = account_comment
    args['expName'] = expenditure_name
    args['JrnlStat'] = account_status
    if request.method == 'POST' and user_name and account_title.is_valid() and account_status.is_valid()\
        and account_date.is_valid() and account_currency.is_valid() and account_amount.is_valid() \
        and account_comment.is_valid() and expenditure_name.is_valid() and account_status.is_valid():
        user_name.save()
        account_title.save()
        account_date.save()
        account_currency.save()
        account_amount.save()
        account_comment.save()
        expenditure_name.save()
        account_status.save()
    return render(request,'SendForm.html',args)

def AccountList(request):
    bank_account = Bank_Account.objects.all()
    user_name = auth.get_user(request).get_username()
    return render_to_response('AccountList.html',{'accounts': bank_account,'username':user_name})



def Journal(request, account_id = 1):
    user_name = auth.get_user(request).get_username()
    bank_account_id  = Bank_Account.objects.get(id = account_id)
    account =  bank_account_id.bank_account_title
    all_transactions = Account_transaction.objects.filter(bank_account=account_id)
    args = {}
    args['username'] = user_name
    args['account'] = account
    args['transactions'] =  all_transactions
    return render_to_response('Journal.html',args)












# def TryToSave(request):
#     form = AccountComment(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         form.save()
#
#     return render_to_response('trytosave.html',{'form':form}, RequestContext(request))
