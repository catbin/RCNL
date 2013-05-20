from django.shortcuts import render
from users.utils import UserFormToLogin, Authendicator
from django.http import HttpResponseRedirect

def login (request):
    if request.method == 'POST':
        form = UserFormToLogin(request.POST) 
        if form.is_valid():
            a = Authendicator 
            result = a.login_me(form.cleaned_data['uname'], form.cleaned_data['password'], request)()
            if result:
                return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = UserFormToLogin()
    return render(request, 'users/login.html', {'form': form,})