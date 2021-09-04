from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='doct_home'),
    path('edit-doct/<int:id>', views.updateDoctor, name='doct_update'),
    path('create-doct/', views.createDoctor, name='doct_create'),
]
