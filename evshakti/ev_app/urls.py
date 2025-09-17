from .views import (add_view, show_view,update_view,delete_view,home_view,contact_view,longBatteryLife,fastandsmooth,ecofriendly)
from django.urls import path


urlpatterns=[
    path("add/",add_view,name="add"),
    path("show/",show_view,name="show"),
    path("update/<id>/",update_view,name="update"),
    path("delete/<id>/",delete_view,name="delete"),
    path('', home_view, name='home'),
    path("contact/", contact_view, name="contact"),
    path("longBatteryLife/", longBatteryLife, name="battery"),
    path("fastandsmooth/", fastandsmooth, name="fast"),
    path("ecofriendly/", ecofriendly, name="eco"),

]