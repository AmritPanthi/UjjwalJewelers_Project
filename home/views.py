from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'home/index.html')

def profile(request):
    return render(request,'home/Profile.html')

def rate(request):
    return render(request,'home/Rate.html')

def buy_now(request):
    products = Products.objects.all()
    context = {
        'products' : products
    }
    return render(request,'home/Buynow.html', context)

def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('buy_now_page')
        else:
            context = {
            "error" : "Enter valid username and password"
            }
            return render(request, "home/Login.html", context)
    else:
        return render(request, "home/Login.html", context)


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            this_user = User.objects.get(username = username)
            return render(request, 'home/Login.html', {'error': 'Username taken'})
        except User.DoesNotExist:
            this_user = User.objects.create_user(username = username, email = email, password = password )
            auth.login(request, this_user)
            return redirect('home_page')
    
    return redirect('login_page')

def logout(request):
    auth.logout(request)
    return render(request, 'home/index.html')

def dashboard(request):
    return render(request,'home/Dashboard.html',)

def customerdetails(request):

    user = User.objects.all()
    paginator = Paginator(user, 2)
    page = request.GET.get('page')
    try:
        user= paginator.page(page)
    except PageNotAnInteger:
        user = paginator.page(1)
    except EmptyPage:
        user = paginator.page(paginator.num_pages)
    context = {
        'users' : user
    }
    return render(request,'home/Customerdetails.html', context)


def addproducts(request):
    if request.method == 'POST':
        new_product = Products(name = request.POST['name'], price = request.POST['price'], image = request.FILES['image'])
        new_product.save()
        return redirect('productdetails_page')
    return render(request,'home/Addproducts.html')

def edit(request,product_id):
	product=Products.objects.get(product_id=product_id)
	return render(request,"edit.html",{'product':product})

def update(request, id):
    if request.method == 'POST':
        new_product = Products.objects.get(id=id)
        new_product.name = request.POST['name']
        new_product.price = request.POST['price']
        new_product.image = request.FILES['image']
        new_product.save()
        return redirect('productdetails_page')

    product = Products.objects.get(id=id)
    context = {
        'product' : product
    }
    return render(request,'home/updateproducts.html', context)
	

def delete(request, id):
	product = Products.objects.get(id=id)
	product.delete()
	return redirect('productdetails_page')


def productdetails(request):
    products = Products.objects.all()
    paginator = Paginator(products, 2)
    page = request.GET.get('page')
    try:
        products= paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'products' : products
    }
    return render(request,'home/ProductDetails.html', context)
def show(request):               #searching the flights details
    if request.method =='POST':
        product_detail = Products.objects.filter(name__icontains = request.POST['searchTerm']).values()
        print(request.POST['searchTerm'])
        return JsonResponse(list(product_detail), safe=False)