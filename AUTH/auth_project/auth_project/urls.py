"""
URL configuration for auth_project project.

JWT endpoints (login / refresh / logout) at project level.
Book + user API endpoints delegated to books app.
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenBlacklistView, TokenRefreshView

from books.views import MyTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/', include('books.urls')),
]
