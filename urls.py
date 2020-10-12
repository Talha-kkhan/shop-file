from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="about"),  
    path("contact/", views.contact, name="contactUs"),  
    path("tracker/", views.tracker, name="tracker"),  
    path("search/", views.search, name="search"),  
    path("productview/<int:myid>", views.productView, name="productView"),  
    path("checkout/", views.checkout, name="checkout"),  
    path("design/", views.design, name="design"),
]
