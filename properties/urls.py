"""properties URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.views.static import serve
from django.conf import settings
from accounts.views import signup, profile
from rentedproperties.views import property_list, property_detail, add_property, home_page
from reviews.views import write_review
from billing.views import add_credit_card, remove_credit_card, make_payment, subscribe, unsubscribe




urlpatterns = [
    path('admin/', admin.site.urls),
    path('property_list/',property_list, name='home'),
    path('',home_page, name='home_page'),
    path('add_property/', add_property, name='add_property'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('property_detail/<int:id>/', property_detail, name='property_detail'),
    path('billing/add_credit_card/', add_credit_card, name='add_credit_card'),
    path('reviews/add/<int:id>', write_review, name='write_review'),
    path('billing/remove_credit_card/', remove_credit_card, name='remove_credit_card'),
    path('billing/make_payment/', make_payment, name='make_payment'),
    path('billing/subscribe/', subscribe, name='subscribe'),
    path('billing/unsubscribe/', unsubscribe, name='unsubscribe'),
    path('media/<path:path>', serve, {'document_root':settings.MEDIA_ROOT}),
    
]
