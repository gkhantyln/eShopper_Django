from django.contrib import admin
from home.models import Settings, Slider, ContactFormMessage, Blogs, BlogCategory
from django.utils.safestring import mark_safe
from home.views import home
# Register your models here.

class SettingsAdmin(admin.ModelAdmin):
    
    list_display = ['company', 'phone', 'email', 'image_tag1', 'image_tag2', 'status' ,'create_at']
    readonly_fields = ('image_tag1','image_tag2')
    list_editable = ['status']

admin.site.register(Settings,SettingsAdmin)



class SliderAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'image_tag', 'update_at', 'is_active', 'create_at']
    readonly_fields = ('image_tag',)
    list_editable = ['is_active']
    search_fields = ['title', 'description']


admin.site.register(Slider, SliderAdmin)


class ContactFormMessageAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'subject', 'email', 'status', 'update_at' ,'create_at']
    #readonly_fields = ('message',)
    list_editable = ['status']
    search_fields = ['name', 'message']
    list_filter = ['status']
    
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)


class BlogAdmin(admin.ModelAdmin):
	list_display = ("title", "image_tag3","is_active", "is_home", "slug", "selected_categories")
	list_editable = ("is_active", "is_home")
	search_fields = ("title", "description")
	readonly_fields = ("slug","image_tag3")
	list_filter = ("is_active", "is_home", "categories")
 
	
	def selected_categories(self, obj):
		html = "<ul>"
		
		for category in obj.categories.all():
			html += "<li>" + category.name + "</li>"
		
		html += "</ul>"
		return mark_safe(html)

admin.site.register(Blogs, BlogAdmin)



class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_active")

admin.site.register(BlogCategory, BlogCategoryAdmin)
