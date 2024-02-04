from django.urls import path
from . import views
urlpatterns = [
   path('', views.Userlogin.as_view(), name="login"),
   path('sign_in/', views.CreateNewUser.as_view(), name="signUp"),
   path('create_user/', views.CreateNewUser.as_view(), name = "new_user"),
   path("add_purchased_items/", views.RegisterPurchaseItems.as_view(), name="add_items"),
   path("fetch_groceries/<str:month>/", views.FetchGroceries.as_view(), name="purchase_items"),
   path("purchased_items/<int:id>/", views.ParticularPurchaseItems.as_view(), name="items"),
   # path("fetch_groceris/", views.PurchasedItemSerializers, name="purchase_items"),
]