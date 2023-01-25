from django.contrib import admin
from django.urls import path,include
from Fashion_App import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("shopping", views.Shopping.as_view()),
    path("cart",views.Cartpage.as_view() ),
    path("orders",views.Orderspage.as_view() ),
    path("register",views.Registerpage.as_view() ),
    path("homepage",views.Details.as_view() ),
] 