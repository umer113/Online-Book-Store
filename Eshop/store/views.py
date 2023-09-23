from django.shortcuts import render,HttpResponse,redirect
from .models.product import Product
from .models.customer import Customer
from django.contrib.auth.hashers import make_password ,check_password 
import re

# Create your views here.
def index(request):
    return render(request,"index.html")

def books(request):
    product = Product.get_all_products();
    return render(request,"book.html",{'products':product})

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        email = postData.get('email')
        password = postData.get('password')
        retype_password = postData.get('retype_password')
        # validation
        error_messages = []
        customer = Customer(email=email, password=password, retype_password=retype_password)

        if not email:
            error_messages.append("Email is required!")
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            error_messages.append("Enter the email address in the format someone@example.com.")
        elif len(email) < 8:
            error_messages.append("Email must have at least 8 characters!")

        elif len(password) < 8:
            error_messages.append("Password must have at least 8 characters!")

        if not retype_password:
            error_messages.append("Retype password is required!")
        elif password != retype_password:
            error_messages.append("Passwords do not match!")
        elif customer.isExist():
            error_messages.append("Email address already registered")
        # saving
        if not error_messages:     
            customer.password = make_password(customer.password)
            customer.retype_password = make_password(customer.retype_password)  
            customer.register()
            return redirect('home')
        else:
            return render(request, "signup.html", {'error_messages': error_messages})
def aboutus(request):
    return render(request,'aboutus.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html') 
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['email'] = customer.email
                return redirect('home')
            else:
                error_message = 'Email or Password Invalid'
        else:
            error_message = 'Email or Password Invalid'

    
        return render(request, 'login.html', {'error': error_message})
    
def add_to_cart(request):
    return render(request,"cart.html")

def post(request):
    product = request.POST.get('product')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        if quantity:
            cart[product] = quantity+1
        else:
            cart[product] = 1

    else:
        cart = {}
        cart[product] = 1
        
    request.session['cart'] = cart
    print(request.session['cart'])
   