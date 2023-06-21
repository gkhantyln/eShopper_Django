from django.db import models
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.forms import ModelForm, TextInput, Textarea
from django.utils.text import slugify


# Create your models here.

class Settings(models.Model):
    STATUS= (
        
        ('true', 'Açık'),
        ('false', 'Kapalı'),
        
    )
    
    title=models.CharField(max_length=100)
    keywords=models.CharField(max_length=200)
    description=models.CharField(max_length=255)
    author=models.CharField(blank=True, max_length=50)
    company=models.CharField(blank=True, max_length=100)
    worktime=models.CharField(blank=True, max_length=200)
    adress=models.CharField(blank=True, max_length=100)
    phone=models.CharField(blank=True, max_length=15)
    fax=models.CharField(blank=True, max_length=15)
    email=models.CharField(blank=True, max_length=50)
    smtpserver=models.CharField(blank=True, max_length=20)
    smtpmail=models.CharField(blank=True, max_length=20)
    smtpport=models.CharField(blank=True, max_length=5)
    smtppassword=models.CharField(blank=True, max_length=10)
    icon=models.ImageField(default='images/not_found_image.png', blank=True,upload_to='images/')
    logo=models.ImageField(default='images/not_found_image.png', blank=True,upload_to='images/')
    facebook=models.CharField(blank=True, max_length=50)
    instagram=models.CharField(blank=True, max_length=50)
    twitter=models.CharField(blank=True, max_length=50)
    linkdn=models.CharField(blank=True, max_length=50)
    googleplus=models.CharField(blank=True, max_length=50)
    dribbble=models.CharField(blank=True, max_length=50)
    youtube=models.CharField(blank=True, max_length=50)
    aboutus=RichTextUploadingField(blank=True)
    references=RichTextUploadingField(blank=True)
    contactsme=RichTextUploadingField(blank=True)
    copyrighttext=models.CharField(blank=True,max_length=200)
    designtext=models.CharField(blank=True,max_length=200)
    designlink=models.CharField(blank=True,max_length=200)
    
    finfotext=models.CharField(blank=True,max_length=200)
    fimaptext=models.CharField(blank=True,max_length=200)
    
    status=models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def image_tag1(self):
        return mark_safe('<img src="{}" style="width: 40px;height: 30px;border:2px solid #81d4fa;"/>'.format(self.logo.url))
    image_tag1.short_description = 'Logo'
    image_tag1.allow_tags = True
    
    def image_tag2(self):
        return mark_safe('<img src="{}" style="width: 40px;height: 30px;border:2px solid #81d4fa;"/>'.format(self.icon.url))
    image_tag2.short_description = 'Favicon'
    image_tag2.allow_tags = True
    


class Slider(models.Model):
    title=models.CharField(max_length=50)
    link=models.CharField(max_length=250)
    sub_title=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    image=models.ImageField(default='slider/not_found_slider.png', blank=True,upload_to='slider/%y/%m/%d/')
    price_image=models.ImageField(default='slider/not_found_slider.png', blank=True,upload_to='slider/%y/%m/%d/')
    is_active = models.BooleanField(default=True)
    #status=models.CharField(max_length=10,choices=STATUS)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def image_tag(self):
        return mark_safe('<img src="{}" style="width: 40px;height: 30px;border:2px solid #81d4fa;"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
class ContactFormMessage(models.Model):
    STATUS = (
        
        ('New', 'Açık'),
        ('Read', 'Inceleniyor'),
        ('Closed', 'Kapandı'),
    )
    
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name' : TextInput(attrs={'class':'form-control', 'placeholder':'Adınız & Soyadınız'}),
            'subject' : TextInput(attrs={'class':'form-control', 'placeholder':'Konu'}),
            'email' : TextInput(attrs={'class':'form-control', 'placeholder':'E-Posta Adresiniz'}),
            'message' : Textarea(attrs={'name':'message', 'id':'message', 'class':'form-control', 'placeholder':'Lütfen Mesajınızı Yazınız', 'rows':'12'}), 
        }


class BlogCategory(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Blogs(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default='blog/not_found_slider.png', blank=True,upload_to='blog/%y/%m/%d/')
    description = RichTextUploadingField(blank=True)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
	#category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    categories = models.ManyToManyField(BlogCategory, blank=True)
    author = models.CharField(blank=True, max_length=15)
    
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def image_tag3(self):
        return mark_safe('<img src="{}" style="width: 40px;height: 30px;border:2px solid #81d4fa;"/>'.format(self.image.url))
    image_tag3.short_description = 'Image'
    image_tag3.allow_tags = True
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)