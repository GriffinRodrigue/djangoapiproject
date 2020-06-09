from django.urls import path

from .views import PostViewSet, UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view()),
    path('users/<int:pk>/', UserViewSet.as_view()),
    path('', PostViewSet.as_view()),
    path('<int:pk>/', PostViewSet.as_view()),

]