from multiprocessing import context
from unicodedata import name
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


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

def signup(request):
    temp = loader.get_template('signup.html')
    return HttpResponse(temp.render({}, request))

def signin(request):
    x = request.POST['username']
    y = request.POST['pass']
    Users.objects.create(name=x,password=y)
    return HttpResponseRedirect(reverse('index'))
        
            