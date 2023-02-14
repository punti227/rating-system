from django.http import HttpResponse
from .models import Products
from django.shortcuts import render, redirect



def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products': products})

def addproduct(request):
    if request.method == 'POST':
        pname = request.POST.get('name')
        pdescription = request.POST.get('description')
        new_product = Products(name=pname, description=pdescription)
        new_product.save()
        print("saved")
        #MyModel.objects.create(title=title, description=description)
        return redirect('index')
    return render(request, 'addproduct.html')

def removeproduct(request, product_id):
    if request.method == 'POST':
        pname = request.POST.get('name')
    product = Products.objects.get(id=product_id)
    product.delete()
    return render(request, 'removeproduct.html')