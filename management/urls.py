from django.urls import path
from . import views
urlpatterns = [
   path('', views.Userlogin.as_view(), name="login"),
   path('create_user/', views.CreateNewUser.as_view(), name = "new_user"),
   path("purchased_items/", views.RegisterPurchaseItems.as_view(), name="add_items")
]