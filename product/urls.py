from django.urls import path
from product import views

urlpatterns = [
    path('',views.category_list_create_api_view),
    path('int:id/', views.category_detail_api_view),
    path('',views.product_list_create_api_view),
    path('int:id/', views.product_detail_api_view),
    path('',views.review_list_create_api_view),
    path('int:id/', views.review_detail_api_view),
    path('', views.product_review_list_api_view)
]