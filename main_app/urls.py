from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('capybaras/', views.cap_index, name="index"),
    path('capybaras/<int:capybara_id>/', views.cap_detail, name='detail'),
    
]