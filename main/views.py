from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ProductsForm, Signup
from main.models import Products
from main.models import Accounts
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def show_main(request):
    products = Products.objects.all()
    if 'first_name' in request.session:
        message = "Welcome, " + request.session['first_name'] + "!"
    else:
        message = "Welcome to My Shop!"

    context = {
        'welcome' : message,
        'name' : 'Baju',
        'price': 'Rp1.000.000',
        'description': 'Baju dengan kualitas terbaik di Indonesia',
        'products' : products
    }

    return render(request, "main.html", context)

def create_products(request):
    form = ProductsForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_accounts.html", context)

def create_accounts(request):
    form = Signup(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        name = request.POST.get('first_name')
        request.session['first_name'] = name
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_accounts.html", context)

def show_xml(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Products.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Products.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def clear_session(request):
    # Clear all session data
    request.session.flush()
    return HttpResponse('Session cleared')