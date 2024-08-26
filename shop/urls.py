"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import home_page
from products.views import about_page, not_found_page, search, product_page, add_product_to_cart, user_cart
from django.conf.urls.static import static
from django.conf import settings
from users.views import register_view, logout_view, profile_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about', about_page),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', register_view, name='signup'),
    path('profile', profile_view, name='profile'),
    path('search', search),
    path('products/<int:id>', product_page),
    path('notfound', not_found_page, name='notfound'),
    path('add_to_cart/<int:id>', add_product_to_cart),
    path('user_cart', user_cart, name='user_cart')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
