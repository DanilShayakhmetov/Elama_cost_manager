from django.shortcuts import render, render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth


# Create your views here.

def Void():
    a=1

@csrf_protect
def Login(request):
    args = {}
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/')
    else:
        args['login_error'] = 'User is not defined'
        return render_to_response('loginPage.html', args)
    return render_to_response('loginPage.html', args)



def Logout(request):
    auth.logout(request)
    redirect('/')



@csrf_protect
def Registered():
    args = {}