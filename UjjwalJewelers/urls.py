"""UjjwalJewelers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from home import views as home_v
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_v.home, name = 'home_page'),
    path('login/', home_v.login, name = 'login_page'),
    path('profile/', home_v.profile, name = 'profile_page'),# home's views's profile 
    path('rate/', home_v.rate, name = 'rate_page'),
    path('signup/', home_v.signup, name = 'signup_page'),
    path('logout/', home_v.logout, name = 'logout_page'),
    path('buynow/', home_v.buy_now, name = 'buy_now_page'),
    path('dashboard/', home_v.dashboard, name = 'dashboard_page'),
    path('customerdetails/', home_v.customerdetails, name = 'customerdetails_page'),
    path('addproducts/', home_v.addproducts, name = 'addproducts_page'),
    path('updateproducts/<int:id>', home_v.update, name = 'updateproducts_page'),
    path('productdetails/', home_v.productdetails, name = 'productdetails_page'),
    path('deleteproducts/<int:id>', home_v.delete, name = 'deleteproducts_page'),
    path('show/', home_v.show, name = "show")
    #path(route, view location, name of the path)
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
