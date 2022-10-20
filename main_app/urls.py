from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('capybaras/', views.cap_index, name="index"),
    path('capybaras/<int:capybara_id>/', views.cap_detail, name='detail'),
    path('capybaras/create/', views.CapCreate.as_view(), name='caps_create'),
    path('capybaras/<int:pk>/update/', views.CapUpdate.as_view(), name='caps_update'),
    path('capybaras/<int:pk>/delete/', views.CapDelete.as_view(), name='caps_delete'),
    path('capybaras/<int:capybara_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    
]