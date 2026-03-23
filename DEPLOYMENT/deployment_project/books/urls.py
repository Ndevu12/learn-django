from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, UserListView

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/users/', UserListView.as_view(), name='user-list'),
]
