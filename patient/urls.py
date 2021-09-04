from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='patient_home'),
    path('signup/', views.signup, name='patient_signup'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]
