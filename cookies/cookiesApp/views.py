from django.shortcuts import render
from django.http import HttpResponse
from .forms import ItemForm

# Create your views here.

def home(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Home Page</h1>")

def page2(request):
    if request.session.test_cookie_worked():
        print('Cookies are enabled')
        request.session.delete_test_cookie()
    return HttpResponse("<b>Page2</b>")


def countView(request):
    if 'count' in request.COOKIES:
        count = int(request.COOKIES['count'])+1
    else:
        count = 1
    response = render(request, 'cookiesApp/count.html',{'count':count})
    response.set_cookie('count',count)
    return response


def indexView(request):
    return render(request, 'cookiesApp/index.html')

def addItem(request):
    form = ItemForm()
    response = render(request, 'cookiesApp/addItem.html',{'form':form})
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            response.set_cookie(name, quantity,120)

    return response

def displayCart(request):
    return render(request, 'cookiesApp/displayItems.html')
