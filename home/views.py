from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from home.models import Settings, ContactFormu, ContactFormMessage, Blogs, BlogCategory, Slider
from django.contrib import messages
from product.models import Product, Category
from product.views import Product
#from django.forms import messages

def index(request):
   settings = Settings.objects.get(pk=1) #db_object
   products = Product.objects.all()
   category = Category.objects.all()
   slider = Slider.objects.all()
   context = {'settings':settings, 'page':'home', 'sliders':slider, 'products':products, 'categories':category}
   
   return render(request, "home/index.html", context)

def home(request):
   settings = Settings.objects.get(pk=1) #db_object
   products = Product.objects.all()
   category = Category.objects.all()
   slider = Slider.objects.all()
   context = {'settings':settings, 'page':'home', 'sliders':slider, 'products':products, 'categories':category}
   
   return render(request, "home/index.html", context)

def contact(request):
   if request.method == "POST":
      form = ContactFormu(request.POST)
      if form.is_valid():
         data = ContactFormMessage() #model ile bağlantı
         data.name = form.cleaned_data['name']
         data.email = form.cleaned_data['email']
         data.subject = form.cleaned_data['subject']
         data.message = form.cleaned_data['message']
         data.ip = request.META.get('REMOTE_ADDR')
         data.save() #veritabanına kaydet
         messages.success(request, "Mesajınız Yetkili Birime Aktarılmıştır. Teşekkürler.")
         return HttpResponseRedirect('/contact') 
      
   settings = Settings.objects.get(pk=1)
   form = ContactFormu() 
   context = {'settings':settings, 'form':form}
   return render(request, "home/contact.html", context)


def about(request):
   settings = Settings.objects.get(pk=1) #db_object
   context = {'settings':settings}
   
   return render(request, "home/about.html", context)

def login_request(request):
   settings = Settings.objects.get(pk=1) #db_object
   
   context = {'settings':settings}

   if request.method == "POST":
      username = request.POST["username"]
      password = request.POST["password"]
      
      user = authenticate(request, username=username, password=password)
      
      if user is not None:
         login(request, user)
         return redirect("/")
      else:
         error = {'settings':settings, "error": "Kullanıcı adı veya Parolanız Hatalıdır."}
         return render(request, "home/login.html", error)

   return render(request, "home/login.html", context)

def logout_request(request):
   
   logout(request)
   return redirect('/')
   

def sign_up(request):
   settings = Settings.objects.get(pk=1) #db_object
   
   context = {'settings':settings}

   if request.method == "POST":
      
      firstname = request.POST["firstname"]
      lastname = request.POST["lastname"]
      email = request.POST["email"]
      username = request.POST["username"]
      password = request.POST["password"]
      repassword = request.POST["re-password"]
      
      if password == repassword:
         
         if User.objects.filter(username=username).exists():
            
            error = {
               
               'settings':settings, 
               'rerror': "Bu Kullanıcı Adı Kullanılıyor",
               
               'firstname' : firstname,
               'lastname' : lastname,
               'email' : email,
               'username' : username 
               
            }
            return render(request, "home/signup.html", error)
         else:
            
            if User.objects.filter(email=email).exists():
               
               error = {
                  'settings':settings, "rerror": "Bu E-Posta Kullanılıyor",
                  'firstname' : firstname,
                  'lastname' : lastname,
                  'email' : email,
                  'username' : username
               }   
                  
               return render(request, "home/signup.html", error)
            else:
               
               user = User.objects.create_user(username=username, email=email, first_name=firstname, last_name=lastname, password=password)
               user.save()
               
               success = {'settings':settings, "success": "Tebrikler, Kayıt Başarılı. Giriş Yapabilirsniz."}
               
               
               return render(request, "home/login.html", success)
            
            
               
      else:
         
         error = {
            'settings':settings, "rerror": "Şifreleriniz Eşleşmiyor.",
            'firstname' : firstname,
            'lastname' : lastname,
            'email' : email,
            'username' : username
                  
         }
         
         return render(request, "home/signup.html", error)
         

   return render(request, "home/signup.html", context)



def cart(request):
  settings = Settings.objects.get(pk=1) #db_object
  context = {'settings':settings}
   
  return render(request, "order/cart.html", context)

def checkout(request):
  settings = Settings.objects.get(pk=1) #db_object
  context = {'settings':settings}
   
  return render(request, "order/checkout.html", context)

def blogs(request):
   settings = Settings.objects.get(pk=1)
   blogs = Blogs.objects.all()
   categories = BlogCategory.objects.all()
   context = {"settings":settings, "blogs": blogs, "categories": categories}
   return render(request, "blogs/blogs.html", context)

def blogs_details(request, slug):
	settings = Settings.objects.get(pk=1) #db_object
	blogs = Blogs.objects.get(slug=slug)
	context = {"settings":settings, "blogs": blogs}
	return render(request, "blogs/blogs_details.html", context)


def blogs_by_category(request, slug):
   settings = Settings.objects.get(pk=1)
   context = {
      "settings":settings,
      "blogs": Blogs.objects.filter(is_active=True, categories__slug=slug),
	   "categories": BlogCategory.objects.all(),
      "selected_category": slug,
      
	}
   return render(request, "blogs/blogs.html", context)


def handler404(request, exception=None):
   
   settings = Settings.objects.get(pk=1) #db_object
   context = {'settings':settings}
   return render(request, "home/404.html", context)


def account(request):
   settings = Settings.objects.get(pk=1) #db_object
   
   context = {'settings':settings, 'page':'account'}
   
   return render(request, "account/my_account.html", context)

def wishlist(request):
   settings = Settings.objects.get(pk=1) #db_object
   
   context = {'settings':settings, 'page':'wishlist'}
   
   return render(request, "home/wishlist.html", context)
 