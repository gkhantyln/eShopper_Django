from tkinter import CASCADE
#from traceback import format_exc
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe
from django.utils.text import slugify
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


#from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    #STATUS= (
        
    #    ('true', 'Evet'),
    #    ('false', 'Hayır'),
        
    #)
    
    title=models.CharField(max_length=100, unique=True)
    description=RichTextUploadingField()
    keywords = models.CharField(max_length=255)
    image=models.ImageField(blank=True, default='images/not_found_image.png', upload_to='images/')
    #status=models.CharField(max_length=10, choices=STATUS)
    is_active = models.BooleanField(default=True)
    #slug=models.SlugField()
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    parent= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    #models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    #class MPTTMeta:
        #order_insertion_by = ['title']
    
    #kategori ve alt kategori gösterimi
    def __str__(self):
        full_path=[self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent 
        return ' / '.join(full_path[::-1])
    #/kategori ve alt kategori gösterimi
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    
    title=models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image=models.ImageField(default='images/not_found_image.png', blank=True, upload_to='images/')
    price= models.FloatField()
    amount=models.IntegerField()
    productcode=models.CharField(max_length=15)
    detail=RichTextUploadingField()
    is_home = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    
	#category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
	#category = models.ManyToManyField(Category, blank=True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" style="width: 40px;height: 30px;border:2px solid #81d4fa;"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


#Products More Images Model Class
class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(default='images/not_found_image.png', blank=True, upload_to='images/')
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" style="width: 40px;height: 30px;border:2px solid #81d4fa;"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    

class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Yayında'),
        ('False', 'Kapalı'),   
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    comment=models.TextField(max_length=255)
    rate = models.IntegerField(blank=True)
    ip = models.CharField(blank=True, max_length=20)
    #is_active = models.BooleanField(default=True)
    status = models.CharField(choices=STATUS, max_length=10, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
    