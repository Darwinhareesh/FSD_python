import json
from django import http
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from website.models import Products
from website.models import Users
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.

def home(request):
    products = Products.objects.all()
    
    data = {
        'title': 'Welcome to Our Store',
        'products': products
    }
    return render(request, 'website/index.html', data)

"""Modiying data 
products = Products.objects.get(id=3)
products.product_name = "New Laptop"
    products.price = 85000.00
    products.save()"""

# def home(request):

#     # prodcuts = Products.objects.all()
#     try:
#         prodcuts = Products.objects.filter(pk=2)
#         if prodcuts is not None:
#             prodcuts.delete()
#         data = {
#             'title': 'Welcome to Our Store',
#             'products': prodcuts
#         }
#     except Exception as e:
#         data = {
#             'title': 'Welcome to Our Store',
#             'products': 'nothing'
#         }
#     # Products.objects.create(product_name='Laptop', product_description='A high-performance laptop', price=999.99)
#     # Products.objects.create(product_name='Smartphone', product_description='A latest model smartphone', price=699.99)
#     # Products.objects.create(product_name='Headphones', product_description='Noise-cancelling headphones', price=199.99)
#     # Products.objects.create(product_name='Smartwatch', product_description='A smartwatch with various features', price=299.99)
#     # Products.objects.create(product_name='Tablet', product_description='A lightweight tablet for on-the-go use', price=499.99)
#     return render(request, 'website/index.html', data)

def search(request):

    return http.HttpResponse('This is search page')

def login_page(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('home')
    return render(request, 'website/login.html')

def logout_view(request):
    from django.contrib.auth import logout
    logout(request)
    return render(request, 'website/login.html')

def product_list(request):
    products = Products.objects.all().values('id','product_name','product_description','price')
    return http.JsonResponse(list(products), safe=False)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password
import json

@csrf_exempt
def signup(request):
    if request.method == "POST":
        import json
        from django.contrib.auth.hashers import make_password
        data = json.loads(request.body)
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Debug: Print data received
        print("Signup data:", username, email, password)

        hashed_password = make_password(password)

        user = Users.objects.create(
            username=username,
            email=email,
            password=hashed_password
        )
        print("User created:", user.id)
        return JsonResponse({"message": "User created successfully"})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Users  # your custom table
from django.contrib.auth.hashers import check_password

@csrf_exempt
def login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            if not username or not password:
                return JsonResponse({"success": False, "message": "Username and password required"}, status=400)

            try:
                user = Users.objects.get(username=username)
                if check_password(password,user.password):  # ⚠️ Plain text check
                    return JsonResponse({"success": True, "message": "Login successful"})
                else:
                    return JsonResponse({"success": False, "message": "Invalid username or password"}, status=401)
            except Users.DoesNotExist:
                return JsonResponse({"success": False, "message": "Invalid username or password"}, status=401)

        except Exception as e:
            print("Login error:", e)
            return JsonResponse({"success": False, "message": "Server error"}, status=500)

    return JsonResponse({"success": False, "message": "Only POST allowed"}, status=405)

@csrf_exempt
def add_product(request):
    if request.method == "POST":
        data = json.loads(request.body)
        product_name = data.get("product_name")
        product_description = data.get("product_description")
        price = data.get("price")

        # Debug: Print data received
        print("Add product data:", product_name, product_description, price)

        product = Products.objects.create(
            product_name=product_name,
            product_description=product_description,
            price=price
        )
        print("Product created:", product.id)
        return JsonResponse({"message": "Product added successfully"})

@csrf_exempt
def edit_product(request, product_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        product_name = data.get("product_name")
        product_description = data.get("product_description")
        price = data.get("price")

        try:
            product = Products.objects.get(id=product_id)
            product.product_name = product_name
            product.product_description = product_description
            product.price = price
            product.save()
            return JsonResponse({"message": "Product updated successfully"})
        except Products.DoesNotExist:
            return JsonResponse({"message": "Product not found"}, status=404)

from django.http import JsonResponse

@csrf_exempt
def get_token(request):
    if request.method == "GET":
        import secrets
        token = secrets.token_hex(16)  # Generate a random 32-character hex token
        return JsonResponse({"token": token})
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
