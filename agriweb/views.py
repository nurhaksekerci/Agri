from django.shortcuts import render

# Create your views here.
def index(request):
    context={
        'title' : 'Farmer'
    }
    return render(request, 'pages/index.html', context)
# Create your views here.
def supplier(request):
    context={
        'title' : 'Supplier'
    }
    return render(request, 'pages/business.html', context)
# Create your views here.
def blog(request):
    context={
        'title' : 'Blog'
    }
    return render(request, 'pages/business.html', context)
# Create your views here.
def contact(request):
    context={
        'title' : 'Contact'
    }
    return render(request, 'pages/business.html', context)