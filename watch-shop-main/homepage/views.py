from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from . models import Watches,WatchesUploads,Wishlisst,Cart,WatchReview
from . forms import UploadForm
from . models import CartItem

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout


def home(request):
    watches = WatchesUploads.objects.all()
    context = {'watches_t':watches}
    return render(request, "home.html",context)


def about(request):
    return render(request, "about.html")

@login_required(login_url="/login")
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()

    return render(request,"WatchUpload.html",{'form':form})



def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=user_name,password=password)
            if user is not None :
                login(request,user)
                return redirect('home')
            else :
                return render(request,"login.html",{'form':form})
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{'form':form})


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,"signup.html",{'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')


from django.shortcuts import get_object_or_404
def show_product(request,id):
    product = get_object_or_404(WatchesUploads,id=id)
    reviews_obj =  WatchReview.objects.filter(product=product)
    print("This is the object",reviews_obj)
    return render(request,"product.html",{"product":product,"reviews":reviews_obj})

# Wishlist 
def addtowish(request,id):
    user = request.user
    product = WatchesUploads.objects.get(id=id)
    obj1,created = Wishlisst.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

def show_wishlist(request):
    user = request.user
    wish_object = Wishlisst.objects.get(user=user)
    return render(request,"wishcart.html",{"user_products":wish_object.products.all()})

def removewish(request,id):
    product_rm = WatchesUploads.objects.get(id=id)
    wish_obj = Wishlisst.objects.get(user=request.user)
    wish_obj.products.remove(product_rm)
    return render(request,"wishcart.html",{"user_products":wish_obj.products.all()})

# Cart Part
def addtocart(request,id):
    # chcek if user has cart or not
    user_cart,created = Cart.objects.get_or_create(user= request.user)

    # fetch the prodcut with given id
    product = WatchesUploads.objects.get(id=id)

    # create a cart item using the product and user
    cart_item, created= CartItem.objects.get_or_create(user=user_cart,product=product)
    cart_item.product = product
    cart_item.save()
    return redirect('home')


def show_cartlist(request):
    # user - cart : get this user cart
    user_cart,created = Cart.objects.get_or_create(user=request.user)
    cart_objects = user_cart.cartitem_set.all()
    return render(request,"cart.html",{"user_products":cart_objects})

def removeCart(request,id):
    product_rm = WatchesUploads.objects.get(id=id)
    cart_obj = Cart.objects.get(user=request.user)
    cart_obj.products.remove(product_rm)
    return render(request,"wishcart.html",{"user_products":cart_obj.products.all(),"isCart":True})