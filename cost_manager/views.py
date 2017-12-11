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
from cost_manager.forms import AccountJournalStatus, ExpenditureName,AccountDate,AccountCurrency,AccountAmount, AccountComment, ProtoForm, ProtoBankForm,ProtoGoalsForm
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from cost_manager.models import Account_transaction,Bank_Account
from django.contrib import auth
from django.contrib.auth.models import User


@csrf_protect
def  TryToSave ( request):
    user_name = auth.get_user(request).get_username()


    return  render(request ,  'Startpage.html' ,  {'username':user_name})







@csrf_protect
def form_test(request):

    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    current_user = User.objects.get(id=USER_ID)
    current_acc = Bank_Account.objects.get(id = 3)
    form_m = ProtoForm(request.POST or None)
    args = {}
    args['ID'] = USER_ID
    args['username'] = user_name
    args['form'] = form_m
    args['a'] = current_acc
    if request.method == 'POST' and form_m.is_valid():
        author = form_m.save(commit=False)
        author.user = current_user
        author.bank_account = current_acc.id
        author.save()
    return render(request,'SendForm.html',args)




@csrf_protect
def CreateAccount(request):
    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    current_user = User.objects.get(id=USER_ID)
    bank_form = ProtoBankForm(request.POST or None)
    args = {}
    args['ID'] = USER_ID
    args['username'] = user_name
    args['bankform'] = bank_form
    if request.method == 'POST' and bank_form.is_valid():
        author = bank_form.save(commit=False)
        author.user = current_user
        author.save()
    return render(request,'CreateAccount.html',args)





def AccountList(request):
    bank_account = Bank_Account.objects.all()
    user_name = auth.get_user(request).get_username()
    return render_to_response('AccountList.html',{'accounts': bank_account,'username':user_name})



def Journal(request, account_id = 1):
    user_name = auth.get_user(request).get_username()
    bank_account_id  = Bank_Account.objects.get(id = account_id)
    account =  bank_account_id.bank_account_title
    userID = bank_account_id.user_id
    all_transactions = Account_transaction.objects.filter(bank_account_id=account_id)
    args = {}
    args['ID'] = userID
    args['username'] = user_name
    args['account'] = account
    args['transactions'] =  all_transactions
    return render_to_response('Journal.html',args)





@csrf_protect
def Goals(request):
    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    current_user = User.objects.get(id=USER_ID)
    form_g = ProtoGoalsForm(request.POST or None)
    args = {}
    args['ID'] = USER_ID
    args['username'] = user_name
    args['form'] = form_g
    if request.method == 'POST' and form_g.is_valid():
        author = form_g.save(commit=False)
        author.user = current_user
        author.save()

    return render(request,'MyGoals.html',args)






# def TryToSave(request):
#     form = AccountComment(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         form.save()
#
#     return render_to_response('trytosave.html',{'form':form}, RequestContext(request))
