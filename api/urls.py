from django.urls import path
from .import views

urlpatterns =[
    path('api/contact/',views.ContactView, name="contact"),
    path('api/contact/<int:pk>/',views.ContactDetailView, name="contactview"),

    path('api/users/',views.UserView, name="users"),

    path('api/categorycreate',views.UserView, name="categorycreate"),

]