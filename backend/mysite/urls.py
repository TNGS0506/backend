from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.getData , name="GetData"),
    path('allshoes/', views.getShoesTop, name="getShoesTop"),   
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('shoes/<str:shoeId>/',views.getShoe, name='getShoe'),
    path('categories/<str:category_name>/', views.getShoesByCategory, name='getShoesByCategory'),
    path('categories/', views.getCategories, name="Get All categories"),
    path('user/EditProfile/', views.update_profile, name='update_profile'),
]