from django.shortcuts import render, redirect
from dashboard.models import Category, Products, Sales
from django.db.models import Sum
from django.contrib import messages
from .forms import CreateUserForm


def index(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}. Continue to Login')
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

#------------------- Dashboard -----------------------#.

def dashboard(request):
    category = Category.objects.all()
    total_category = category.count()
    
    products = Products.objects.all()
    product_count = products.count()
    
    sales = Sales.objects.all()
    total_sales = sales.count()
    
    total_earnings = Sales.objects.aggregate(s=Sum("s_total"))["s"]
    
    context = {
        'total_category' : total_category,
        'product_count' : product_count,
        'total_sales' : total_sales,
        'total_earnings' : total_earnings
    }
    return render(request, 'dashboard.html', context)

#------------------- Category ------------------------#.

def category(request):
    category = Category.objects.all()
    return render(request, 'category/categories.html',{'category':category})

def addcategory(request):
    if request.method == 'POST':
        category_name = request.POST['category_name']
        
        data = Category.objects.create(
            category_name = category_name
            )
        data.save()
    return render(request, 'category/add_category.html')

#------------------- Products ------------------------#.    

def category_data(request):
    category = Category.objects.all()
    return render(request, 'product/add_product.html',{'show_category':category})

def products(request):
    products = Products.objects.all()
    return render(request, 'product/products.html',{'products':products})

def addproduct(request):
    if request.method == 'POST':
        product = request.POST['product']
        price = request.POST['price']
        quantity = request.POST['quantity']
        cat_name = request.POST['cat_name']
        
        data = Products.objects.create(
            product = product,
            price = price,
            quantity = quantity,
            cat_name = cat_name,
            )
        data.save()
        messages.success(request, "Added Successfuly")
        return redirect('/dashboard/products')
    return render(request, 'product/add_product.html')

def editproduct(request, id):
    data = Products.objects.get(id=id)
    return render(request, 'product/edit_product.html',{'data':data})

def updateproduct(request, id):
    if request.method == 'POST':
        data = Products.objects.get(id=id)
        product = request.POST.get('product')
        price = request.POST.get('price')
        
        data.product = product
        data.price = price
        data.save()
        messages.info(request, "Edit Successful")
        return redirect('/dashboard/products')
    return render(request, 'product/products.html')

def deleteproduct(request, id):
    data = Products.objects.get(id=id)
    data.delete()
    messages.error(request, "Added Successfuly")
    return redirect('/dashboard/products')

#------------------- Stocks -------------------------#.

def stocks(request):
    products = Products.objects.all()
    return render(request, 'stocks/stocks.html',{'products':products})

def addstocks(request, id):
    data = Products.objects.get(id=id)
    return render(request, 'stocks/add_stocks.html',{'data':data})

def add_stocks(request, id):
    if request.method == 'POST':
        data = Products.objects.get(id=id)
        quantity = request.POST.get('quantity')
        
        data.quantity = quantity
        data.save()
        messages.success(request, "Edit Successful")
        return redirect('/dashboard/stocks')
    return render(request, 'product/stocks.html')

def minusstocks(request, id):
    data = Products.objects.get(id=id)
    return render(request, 'stocks/minus_stocks.html',{'data':data})

def minus_stocks(request, id):
    if request.method == 'POST':
        data = Products.objects.get(id=id)
        quantity = request.POST.get('quantity')
        
        data.quantity = quantity
        data.save()
        messages.info(request, "Some Stocks Removed")
        return redirect('/dashboard/stocks')
    return render(request, 'product/stocks.html')

#-------------------- Sales -------------------------#.

def sales(request):
    products = Products.objects.all()
    return render(request, 'sales/sales.html',{'sales':products})

def addsales(request, id):
    data = Products.objects.get(id=id)
    return render(request, 'sales/add_sales.html',{'data':data})

def add_sales(request, id):
    if request.method == 'POST':
        caty_name = request.POST['caty_name']
        s_product = request.POST['s_product']
        s_price = request.POST['s_price']
        s_quantity = request.POST['s_quantity']
        s_total = request.POST['s_total']
        s_created_at = request.POST['s_created_at']
        
        data = Sales.objects.create(
            caty_name = caty_name,
            s_product = s_product,
            s_price = s_price,
            s_quantity = s_quantity,
            s_total = s_total,
            s_created_at = s_created_at,
            )
        datas = Products.objects.get(id=id)
        quantity = request.POST.get('quantity')
        datas.quantity = quantity
        datas.save() #update
        data.save() #insert
        messages.success(request, "New Sales Added")
        return redirect('/dashboard/sales')
    return render(request, 'sales/add_sales.html')

#----------------- Sales Report --------------------#.

def salesreport(request):
    products = Sales.objects.all()
    return render(request, 'salesreport/sales_report.html',{'salesreport':products})

