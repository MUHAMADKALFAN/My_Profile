from django.urls import path,include
from  . import views


urlpatterns = [
    path('',views.Home,name="Home"),
    path('customerform',views.customerform,name="customerform"),
    path('singleview/<int:id>',views.singleview,name="singleview"),
]
