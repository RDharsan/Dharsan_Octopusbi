from django.urls import path
from .views import UserView, HobbyView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:pk>/', UserView.as_view()),
    path('users/<int:pk>/hobby/', HobbyView.as_view()),
    path('users/<int:pk>/hobby/<int:pk>/', HobbyView.as_view())


    
]