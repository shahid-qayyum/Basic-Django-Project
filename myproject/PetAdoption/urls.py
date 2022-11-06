from django.urls import path
from .views import (
    homepage,
    registerview,
    loginview,
    logoutview,
    alldogs,
    allcats,
    petbreed,
    shelters,
    articles,
    petdetails,
    contactus,
    search,
    checkoutview
)

urlpatterns = [
    path('home', homepage, name='home'),
    path('register', registerview, name='register'),
    path('login', loginview, name='login'),
    path('logout', logoutview, name='logout'),
    path('alldogpet', alldogs, name='dogs'),
    path('allcatpet', allcats, name='cats'),
    path('petbreed', petbreed, name='breed'),
    path('shelters', shelters, name='shelter'),
    path('pet-care-articles', articles, name='article'),
    path(r'^petdetails/<pk>/', petdetails.as_view(), name='petdetail'),
    path('ContactUs', contactus.as_view(), name= 'contact'),
    path('search', search, name='search'),
    path(r'checkout/<id>/', checkoutview, name='checkout'),
]