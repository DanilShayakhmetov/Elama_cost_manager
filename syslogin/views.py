from django.shortcuts import render, render_to_response,redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib import auth
from  django.contrib.auth.forms import UserCreationForm



@csrf_protect
def Login(request):
    args = {}
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(request,username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('/')
    else:
        args['login_error'] = 'User is not defined'
        return render(request, 'loginPage.html', args)

    # return render(request,'loginPage.html', args)



def Logout(request):
    auth.logout(request)
    return redirect('/')



@csrf_protect
def Registered(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        userform = UserCreationForm(request.POST or None)
        if userform.is_valid():
            userform.save()
            
            return redirect('/')
        else:
            args['form'] = userform
    return render(request, 'registrPage.html', args)