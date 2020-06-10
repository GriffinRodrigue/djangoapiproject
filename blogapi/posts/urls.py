from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import PostViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls

# urlpatterns = [
#     path('users/', UserViewSet.as_view()),
#     path('users/<int:pk>/', UserViewSet.as_view()),
#     path('', PostViewSet.as_view()),
#     path('<int:pk>/', PostViewSet.as_view()),

# ]