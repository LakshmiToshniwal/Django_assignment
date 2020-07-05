from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('cse',views.cse,name="cse"),
     path('etc',views.cse,name="etc"),
      path('mech',views.cse,name="mech"),
       path('civil',views.cse,name="civil")
]
