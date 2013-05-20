from users.models import User
from django import forms
from django.db.models import Q
from django.http import HttpResponseRedirect

class Authendicator:
    FAILED = 0
    AUTHENDICATED = 1
    
    
    @staticmethod
    def login_me( username, password, request ):
        try:
            user = User.objects.select_related().filter( Q( uname = username ) )
            if not user.exists():
                return Authendicator.FAILED
            if user[0].password == password:
                request.session['user'] = user[0]
                return Authendicator.AUTHENDICATED
            return Authendicator.FAILED
        except:
            return Authendicator.FAILED
    
    @staticmethod
    def logout_me ( request ):
        request.session.flush()
        
class UserFormToLogin(forms.Form):
    uname = forms.CharField( max_length = 14)
    password = forms.CharField( max_length = 75 , widget = forms.PasswordInput() )

    
    
def RCNL_login_required(function):
    def wrapper( request, *args, **kwargs ):
        if not request.session.get( 'user' ):
                request.session['next'] = request.META['PATH_INFO']
                return HttpResponseRedirect( "/users/login/?next=" + request.META['PATH_INFO'] )

        return function( request, *args, **kwargs )
    
    return wrapper