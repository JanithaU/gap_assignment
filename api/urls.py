from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

#URL CONF
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('users/', views.userList, name="user-list"),
    path('users/register', views.userCreate, name="register-list"),

    path('categories/', views.categoryList, name="category-list"),
    path('category/create', views.catCreate, name="category-create"),
    path('category/<str:pk>', views.catDetail, name="category-detail"),
    path('category/update/<str:pk>',views.catUpdate, name="category-update"),
    path('category/delete/<str:pk>',views.catDelete, name="category-delete"),
    
   
    path('parts/', views.partList, name="part-list"),
    path('part/details/<int:pk>', views.partDetails, name="part-detail"),
    
    path('cart/', views.cartList, name="cart"),
    path('cart/create/',views.cartCreate, name="cart-create"),
    path('cart/delete/<str:pk>',views.cartDelete, name="cart-delete"),
   
    path('orders/', views.orderList, name="order"),
    path('order/<int:pk>', views.orderView, name="order-view"),
    path('order/update/<int:pk>/shipped', views.orderUpdate, name="order-update"),
    path('order/create/', views.orderCreate, name="order-create"),
    path('order/update/<int:pk>/delivered', views.orderDelivered, name="order-delivered"),

    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]