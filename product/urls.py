from django.urls import path
from product import views
from utils.constants import LIST_CREATE, RETRIEVE_UPDATE_DESTROY


urlpatterns = [
    path('',views.category_list_create_api_view),
    path('int:id/', views.category_detail_api_view),
    path('',views.product_list_create_api_view),
    path('int:id/', views.product_detail_api_view),
    path('',views.review_list_create_api_view),
    path('int:id/', views.review_detail_api_view),
    path('', views.product_review_list_api_view),
    path('category/',views.CategoryListCreateViewSet.as_view(LIST_CREATE)),
    path('category/<int:id>/',views.CategoryListCreateViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),    
    path('product/',views.ProductListCreateViewSet.as_view(LIST_CREATE)),
    path('product/<int:id>/',views.ProductListCreateViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),
    path('product/',views.ReviewListCreateViewSet.as_view(LIST_CREATE)),
    path('product/<int:id>/',views.ReviewListCreateViewSet.as_view(RETRIEVE_UPDATE_DESTROY)),    
]