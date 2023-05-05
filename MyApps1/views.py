from django.shortcuts import render
from django.http import HttpResponse

#Create your views here.
def index(request):
    request.session.set_test_cookie()
    print('Cookies are set for Initial-request..!!')
    return HttpResponse('<h1>Index page of Cookies...</h1><hr /><h2>Request check_view/ url...</h2>')

def check_view(request):
    if request.session.test_cookie_worked():
        print('Cookies are working properly')
        request.session.delete_test_cookie()
        return HttpResponse('<h1>Cookie Checking Page Working Properly..!!!</h1><hr />')
    else:
        print('Cookies are NOT working properly')
        return HttpResponse('<h1>Cookie Checking Page NOT-Working Properly..!!!</h1><hr />')


##Cookie-Application-1
from django .shortcuts import render
#Create your views here.
def count_view(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1;

    response=render(request,'MyApps1/count.html',{'count':newcount})
    response.set_cookie('count',newcount)  #cookie with data or variable(count)
    return response;


##Application-2
from django .shortcuts import render
from MyApps1.forms import LoginForm
import datetime;
#Create your views here.
def home_view(request):
    formobj=LoginForm()
    return render(request,'MyApps1/home.html',{'formobj':formobj})

def date_time_view(request):
    #form=LoginForm(request.GET)
    name=request.GET['name']
    response=render(request,'MyApps1/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response;

def result_view(request):
    name=request.COOKIES['name']
    date_time=datetime.datetime.now()
    dict1={'name':name,'date_time':date_time}
    return render(request,'MyApps1/result.html',dict1)

##Application-3
from django .shortcuts import render
#Create your views here.
def name_view(request):
    return render(request,'MyApps1/name.html');

def age_view(request):
    name=request.GET['name']
    response=render(request,'MyApps1/age.html',{'name':name})
    response.set_cookie('name',name,15)
    return response

def parent_view(request):
    age=request.GET['age']
    name=request.COOKIES['name']
    response=render(request,'MyApps1/parent.html',{'name':name})
    response.set_cookie('age',age,15)
    return response

def result1_view(request):
    name=request.COOKIES['name']
    age=request.COOKIES['age']
    pname=request.GET['pname']
    response=render(request,'MyApps1/result1.html',{'name':name,'age':age,'pname':pname})
    response.set_cookie('pname',pname,15)
    return response


##Application-4
from django .shortcuts import render
from MyApps1.forms import ItemAddForm
#Create your views here.
def index1(request):
    return render(request,'MyApps1/home1.html')

def additem_view(request):
    formobj = ItemAddForm()
    response=render(request,'MyApps1/additem.html',{'formobj':formobj})
    if request.method=='POST':
        formobj=ItemAddForm(request.POST)
        if formobj.is_valid():
            name=formobj.cleaned_data['name']
            quantity=formobj.cleaned_data['quantity']
            print(name,quantity);
            response.set_cookie(name,quantity,180) #cookie-age is 180-sec or 3-minutes only
            #return index(request);
    return response

def displayitem_view(request):
    return render(request,'MyApps1/showitems.html');
