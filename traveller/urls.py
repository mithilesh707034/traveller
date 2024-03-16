from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home_page),
    path('signup/',views.signup_page),
    path('login/',views.login_page),
    path('profile/',views.profile_page),
    path('logout/',views.logout_page),
    #Order
    path('book-now/<int:id>/',views.add_to_cart),
    path('checkout/',views.checkout),
    path('payment-fail/',views.payment_fail_redirect),
    path('payment-success/',views.payment_success_redirect),
    path('confirm-order-now/',views.confirm_orderPage),
    path('order/',views.orderPage,name="orderPage"),
    path('about/',views.about,name="about"),
    path('search/',views.search,name="search"),
    path('update-profile/<int:id>/',views.update_profile,name="update_profile"),

    path('<str:city>/',views.package_list),
    path('<str:name>/<int:id>/',views.package_details),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
