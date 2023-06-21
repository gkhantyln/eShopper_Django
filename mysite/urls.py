from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


handler404 = 'home.views.handler404'  #urls.py dosyasına eklenecek kısım
app_name = "home"

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('products/', include('product.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#if settings.DEBUG: # new
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
