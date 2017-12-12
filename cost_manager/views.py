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
from cost_manager.forms import AccountJournalStatus, ExpenditureName,AccountDate,AccountCurrency,AccountAmount, AccountComment, ProtoForm, ProtoBankForm,ProtoGoalsForm, ProtoMotionOne, ProtoMotionTwo
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from cost_manager.models import Account_transaction,Goals_Account
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import connection, transaction

@csrf_protect
def  TryToSave ( request):
    user_name = auth.get_user(request).get_username()
    return  render(request ,  'Startpage.html' ,  {'username':user_name})



def HOME(request):
    user_name = auth.get_user(request).get_username()
    return render(request, 'HOME.html', {'username': user_name})


@csrf_protect
def form_test(request):
    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    current_user = User.objects.get(id=USER_ID)
    form_m = ProtoForm(request.POST or None)
    args = {}
    args['ID'] = USER_ID
    args['username'] = user_name
    args['form'] = form_m
    if request.method == 'POST' and form_m.is_valid():
        author = form_m.save(commit=False)
        author.user = current_user
        author.save()
    return render(request,'SendForm.html',args)




@csrf_protect
def CreateAccount(request):
    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    current_user = User.objects.filter(id=USER_ID)
    bank_form = ProtoBankForm(request.POST or None)
    args = {}
    args['ID'] = USER_ID
    args['username'] = user_name
    args['bankform'] = bank_form
    if request.method == 'POST' and bank_form.is_valid():
        author = bank_form.save(commit=False)
        author.user = request.user
        author.save()
    return render(request,'CreateAccount.html',args)







def AccountList(request):
    USER = request.user
    USER_ID = USER.id
    bank_account = Account_transaction.objects.filter(user_id = USER_ID)
    user_name = auth.get_user(request).get_username()
    return render_to_response('AccountList.html',{'accounts': bank_account,'username':user_name})



def Journal(request, account_id = 1):
    user_name = auth.get_user(request).get_username()
    selected_bank_account  = Account_transaction.objects.filter(id = account_id)
    args = {}
    args['username'] = user_name
    args['account'] = selected_bank_account
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


def GoalsList(request):
    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    list_of_goals = Goals_Account.objects.filter(user_id=USER_ID)
    args = {}
    args['username'] = user_name
    args['goals'] = list_of_goals
    return render_to_response('GoalsList.html',args)


def Balance(request):
    args = {}
    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    values = Account_transaction.objects.filter(user_id=USER_ID)
    balance_response_USD = 0
    balance_response_EUR = 0
    balance_response_RUR = 0
    for value in values:
        if value.account_transaction_currency == 'USD':
            if value.account_jornal_status == '+':
                balance_response_USD = balance_response_USD + value.account_transaction_amount
            elif value.account_jornal_status == '-':
                balance_response_USD = balance_response_USD - value.account_transaction_amount
            else:
                continue
        elif value.account_transaction_currency == 'EUR':
            if value.account_jornal_status == '+':
                balance_response_EUR = balance_response_EUR + value.account_transaction_amount
            elif value.account_jornal_status == '-':
                balance_response_EUR = balance_response_EUR - value.account_transaction_amount
            else:
                continue
        elif value.account_transaction_currency == 'RUR':
            if value.account_jornal_status == '+':
                balance_response_RUR = balance_response_RUR + value.account_transaction_amount
            elif value.account_jornal_status == '-':
                balance_response_RUR = balance_response_RUR - value.account_transaction_amount
            else:
                continue
    args['username'] = user_name
    args['balance_USD'] = balance_response_USD
    args['balance_EUR'] = balance_response_EUR
    args['balance_RUR'] = balance_response_RUR
    return render_to_response('Balance.html',args)









@csrf_protect
def Motion(request):
    user_name = auth.get_user(request).get_username()
    USER = request.user
    USER_ID = USER.id
    DONOR = ProtoMotionOne(request.POST or None)
    ACCEPTOR = ProtoMotionTwo(request.POST or None)
    current_user = User.objects.get(id=USER_ID)
    args = {}
    args['username'] = user_name
    args['ID'] = USER_ID
    args['DONOR'] = DONOR
    args['ACCEPTOR'] = ACCEPTOR
    if request.method == 'POST' and DONOR.is_valid() and ACCEPTOR.is_valid():
        one = DONOR.save(commit=False)
        two =  ACCEPTOR.save(commit=False)
        one.user = current_user
        two.user = current_user
        one.account_journal_status = '-'
        two.account_journal_status = '+'
        one.save()
        two.save()
    return render(request, 'Motion.html', args)


#
# def Template(request):
#     args ={}
#     cursor = connection.cursor()
#     cursor.execute
#     user_name = auth.get_user(request).get_username()
#     USER = request.user
#     USER_ID = USER.id
#     my_dict = {
#         'id': 10,
#         'city': 20,
#         'state': 30
#     }
#
#     Account_transaction.objects.raw('SELECT * from cost_manager_all transaction
#                            where user = %(USER_ID)s and
#                            account_amount = %(ac)s and
#                            state = %(state)s ', my_dict)
#
#




    # form_m = ProtoForm(request.POST or None)
    # args = {}
    # args['ID'] = USER_ID
    # args['username'] = user_name
    # args['form'] = form_m
    # if request.method == 'POST' and form_m.is_valid():

        # author = form_m.save(commit=False)
        # author.user = current_user
        # author.save()
    # return render(request, 'SendForm.html', args)

#






# def TryToSave(request):
#     form = AccountComment(request.POST)
#     if form.is_valid():
#         comment = form.save(commit=False)
#         form.save()
#
#     return render_to_response('trytosave.html',{'form':form}, RequestContext(request))
