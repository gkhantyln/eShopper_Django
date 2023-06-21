from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    #path('home/', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('blogs/', views.blogs, name='blogs'),
    path('category/<slug:slug>/', views.blogs_by_category, name='blogs_by_category'),
    path('blogs/<slug:slug>/', views.blogs_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about, name='about'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('sign-up/', views.sign_up, name='account'),

    
    
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]