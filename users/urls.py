from django.urls import path
from users import views


urlpatterns = [
    path('registration/', views.registration_api_views),
    path('authorization/', views.authorization_api_views),
    path('confirm/', views.confirmation_api_views),    
]
