from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('seccond/',views.seccond),
    path('third/',views.third),
    path('details/',views.details),
]
