from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
#from django.utils.safestring import mark_safe
from product.models import Category, Product, Images, Comment

# Register your models here.

class ProductImageInline(admin.TabularInline):
    list_display = ['image_tag']
    readonly_fields = ('image_tag',)
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'is_active', 'image', 'slug']
    search_fields = ['title', 'description']
    readonly_fields = ['slug']
    list_filter = ['is_active']

admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'category', 'price', 'amount', 'image_tag', 'is_active', 'is_home', 'is_featured', 'is_recommended']
    readonly_fields = ('image_tag',)
    list_editable = ['is_home', 'is_featured' , 'is_recommended','is_active']
    search_fields = ['title', 'description']
    readonly_fields = ['slug']
    list_filter = ['is_active','category', 'is_home', 'is_featured', 'is_recommended']
    inlines= [ProductImageInline]

admin.site.register(Product,ProductAdmin)

class ImagesAdmin(admin.ModelAdmin):
     list_display = ['title', 'product', 'image_tag'] 
     readonly_fields = ('image_tag',)

admin.site.register(Images,ImagesAdmin)


class CommentAdmin(admin.ModelAdmin):
     list_display = ['subject', 'rate', 'status', 'product', 'user', 'ip' , 'update_at','create_at']
     list_editable = ['status']
     search_fields = ['subject', 'comment']
     list_filter = ['status', 'rate']

admin.site.register(Comment,CommentAdmin)
