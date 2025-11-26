# Clothing/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'clothing/index.html')

def about(request):
    return render(request, "clothing/about.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, 'clothing/product.html', {"products": products})
    
def view_cart(request):
    # your cart logic here
    return render(request, 'clothing/cart.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with your homepage URL name
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'clothing/login.html')

class CustomLoginView(LoginView):
    template_name = 'clothing/login.html'

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f"{product.name} added to cart.")
    return redirect('product_list')  # redirect to products page or 'cart'

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'clothing/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart')

@login_required
def update_cart(request, item_id):
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Cart updated.")
        else:
            cart_item.delete()
            messages.success(request, "Item removed from cart.")
    return redirect('cart')
    
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Save to database
        Contact.objects.create(name=name, email=email, message=message_text)

        # Optional: flash message
        messages.success(request, "Thank you! Your message has been sent.")
        return redirect('contact')

    return render(request, 'clothing/contact.html')

