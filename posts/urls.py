from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import PostViewset, UserViewset
# from .views import PostList, PostDetail, UserList, UserDetail

# urlpatterns = [
#     path('<int:pk>/', PostDetail.as_view()),
#     path('', PostList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('users/', UserList.as_view()),
    
# ]

router = SimpleRouter()

router.register('', PostViewset, basename='posts')
router.register('users', UserViewset, basename='users')

urlpatterns = router.urls