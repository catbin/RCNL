from django.shortcuts import render
from users.utils import UserFormToLogin, Authendicator
from django.http import HttpResponseRedirect

def login (request):
    if request.method == 'POST':
        form = UserFormToLogin(request.POST) 
        if form.is_valid(): 
            if Authendicator.login(form['uname'], form['password'], request)():
                return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = UserFormToLogin()
    return render(request, 'users/login.html', {'form': form,})