from django.urls import path
from . import views
from inventory.views import InventoryView,InventoryListView,InventoryDetailView
from cart.views import CartView,CartView_detail
from rest_framework_simplejwt.views import ( TokenObtainPairView,TokenRefreshView,)
from .serializers import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [

    path('', views.getRoutes),
#    USERS
    path('inventory/',InventoryView ),
    path('inventory/<int:pk>',InventoryDetailView),
    path('inventory/search',InventoryListView.as_view()),

#    CARTS
    path('cart/',CartView),
    path('cart/<int:pk>',CartView_detail),

#   TOKEN
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]   