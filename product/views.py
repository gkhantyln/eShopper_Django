from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.models import Settings
from product.models import CommentForm, Comment , Product, Category
from django.contrib.auth.decorators import login_required

# Create your views here.

def product(request):
  settings = Settings.objects.get(pk=1) #db_object
  products = Product.objects.all()
  context = {'settings':settings, 'products':products}
  return render(request, "products/products.html", context)

def product_by_category(request, slug):
  settings = Settings.objects.get(pk=1)
  context = {
    "settings":settings,
    #"products": Product.objects.get(slug=slug).product_set.filter(is_active=True, category__slug=slug),
    "products": Product.objects.filter(is_active=True, category__slug=slug),
		"categories": Category.objects.all(),
    }
   
  return render(request, "products/products.html", context) 

 
#def product(request):
 #  return HttpResponse("Product Page")

def product_detail(request,slug):
  settings = Settings.objects.get(pk=1) #db_object
  categorys = Category.objects.all()
  products = Product.objects.get(slug=slug)
  comments = Comment.objects.filter(status='True')
  context = {
    'settings':settings,
    'products':products, 
    "categories": categorys, 
    'comments':comments,
    }
   
  return render(request, "products/product_details.html", context)



@login_required(login_url="/login")
def addcomment(request, id):
  url = request.META.get('HTTP_REFERER') #get last url
  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      current_user = request.user
      data = Comment()
      data.user_id = current_user.id
      data.product_id = id
      data.subject = form.cleaned_data['subject']
      data.comment = form.cleaned_data['comment']
      data.rate = form.cleaned_data['rate']
      data.ip=request.META.get('REMOTE_ADDR')
      data.save()
      messages.success(request, 'Teşekkürler: Yorumunuz Başarıyla Gönderilmiştir.')
      
      return HttpResponseRedirect(url)
  messages.warning(request, 'Hata: Yorumunuz Gönderilemedi.')
  return HttpResponseRedirect(url)