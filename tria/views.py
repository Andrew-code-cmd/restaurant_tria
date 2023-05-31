from email.message import EmailMessage
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Product, Cart, Salat, Fish, Soup, Profile
from django.contrib.auth.models import User

import smtplib
import ssl
from email.message import EmailMessage

def order(request):
    products = Cart.objects.all()
    one = [product.title for product in products]
    two = [str(product.price) for product in products]
    res = str([{one[i]: two[i]} for i in range(len(one))])
    email_sender = 'lonelycoder11@gmail.com'
    email_password = 'jvcsinovawbqtzxc'
    email_receiver = 'andrey.khlebov@bk.ru'
    subject = 'Заказ'
    body = f'{res}'
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
    return redirect('cart')

def home(request):
    products = Product.objects.all()
    salats = Salat.objects.all()
    fishs = Fish.objects.all()
    soup = Soup.objects.all()
    cart_amount = len(list(Cart.objects.all()))
    return render(request, 'index.html', {'products': products, 'salats': salats, 'fishs': fishs, 'soup': soup, 'cart_amount': cart_amount})

def product(request, id):
    product = Product.objects.get(pk=id)
    cart = Cart()
    cart.title = product.title
    cart.price = product.price
    cart.save()
    return redirect('home') 

def salat(request, id):
    product = Salat.objects.get(pk=id)
    cart = Cart()
    cart.title = product.title
    cart.price = product.price
    cart.save()
    return redirect('home')

def fish(request, id):
    product = Fish.objects.get(pk=id)
    cart = Cart()
    cart.title = product.title
    cart.price = product.price
    cart.save()
    return redirect('home')

def soup(request, id):
    product = Soup.objects.get(pk=id)
    cart = Cart()
    cart.title = product.title
    cart.price = product.price
    cart.save()
    return redirect('home')


def cart(request):
    products = Cart.objects.all()
    titles = [product.title for product in products]
    count = [i.count for i in products]
    cart_amount = len(list(Cart.objects.all()))
    one = [product.price for product in products]
    amount = 0
    for i in range(len(one)):
        amount += one[i]*count[i]
    
    res = dict()
    for i in range(len(one)):
        res[titles[i]] = count[i]
    result = ''
    for key, val in res.items():
        result += f'{key}: {val}\n'
    print(result)
    one = '\n'.join([product.title for product in products])  
    
    return render(request, 'cart.html', {'products': products, 'amount': amount, 'cart_amount': cart_amount, 'order_detail': result})

def delete(request, id):
    product = Cart.objects.get(pk=id)
    product.delete()
    return redirect('cart')

def delete_one(request, id):
    product = Cart.objects.get(pk=id)
    product.count -= 1
    product.save()
    if product.count == 0:
        product.delete()
        return redirect('cart')
    return redirect('cart')

def add_one(request, id):
    product = Cart.objects.get(pk=id)
    product.count += 1
    product.save()
    return redirect('cart')

def zal(request):
    cart_amount = len(list(Cart.objects.all()))
    return render(request, 'zal.html', {'cart_amount': cart_amount})
def ver(request):
    cart_amount = len(list(Cart.objects.all()))
    return render(request, 'ver.html', {'cart_amount': cart_amount})
def cabinet(request):
    data = User.objects.all()
    cart_amount = len(list(Cart.objects.all()))
    return render(request, 'cabinet.html',  {'data': data, 'cart_amount': cart_amount})

    


