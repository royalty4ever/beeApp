from django.urls import path 
from beeApp import views

urlpatterns = [
    path("", views.index, name='index'),

    path("register", views.register, name="register"),
    
    path("login", views.login, name="login"),
 
    path("logout", views.logout, name="logout"),

    path("dashboard", views.dashboard, name="dashboard"),

    path("bee_rules", views.bee_rules, name="bee_rules"),

    path("gallery", views.gallery, name="gallery"),

    path("create_record", views.create_record, name="create_record"),

    path('update-record/<int:pk>', views.update_record, name="update-record"),

    path('record/<int:pk>', views.singular_record, name="record"),

    path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
   
]