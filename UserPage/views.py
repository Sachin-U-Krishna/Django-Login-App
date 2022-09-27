from multiprocessing import context
from django.template import loader
from django.http import HttpResponse

from UserPage.models import Users
# Create your views here.
def index(request):
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render({}, request))

def auth(request):
    temp = loader.get_template('auth.html')
    err = loader.get_template('err.html')
    a = request.POST['username']
    b = request.POST['pass']
    users = Users.objects.all().values()
    context = {
        'a':a
    }
    flag = 0 
    for i in users:
        if i['name']== a and i['password'] == b:
            flag = 1
            return HttpResponse(temp.render(context,request))
    if flag == 0:
        return HttpResponse(err.render())
        
            