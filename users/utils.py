from users.models import User
from django.forms import ModelForm

class Authendicator:
    FAILED = 0
    AUTHENDICATED = 1
    
    
    @staticmethod
    def login( username, password, request ):
        try:
            user = User.objects.select_related().filter( Q( uname = id ) )
            if not user.exists():
                return Authendicator.FAILED
            if user[0].password == password:
                request.session['user'] = user[0]
                return AUTHENDICATED
            return FAILED
        except:
            return FAILED
    
    @staticmethod
    def logout ( request ):
        request.session.flush()
        
class UserFormToLogin(ModelForm):
    class Meta:
        model = User
        fields = ['uname', 'password']
    
def RCNL_login_required(function):
    def wrapper( request, *args, **kwargs ):
        if not request.session.get( 'user' ):
                request.session['next'] = request.META['PATH_INFO']
                return HttpResponseRedirect( "/users/login/?next=" + request.META['PATH_INFO'] )

        return f( request, *args, **kwargs )
    
    return wrapper