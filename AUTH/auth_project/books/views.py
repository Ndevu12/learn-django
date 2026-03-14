from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Book, User
from .permissions import IsAdminRole, IsEditorOrAdmin, IsOwnerOrAdmin
from .serializers import BookSerializer, MyTokenSerializer, UserSerializer


# ── Custom JWT Token View ──


class MyTokenView(TokenObtainPairView):
    """Login endpoint — returns JWT with username + role claims."""

    serializer_class = MyTokenSerializer


# ── Book ViewSet (CRUD with per-action permissions) ──


class BookViewSet(ModelViewSet):
    """
    list/retrieve  → AllowAny
    create         → IsEditorOrAdmin
    update/partial → IsOwnerOrAdmin
    destroy        → IsAdminRole
    """

    queryset = Book.objects.all().order_by('-pub_date')
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [AllowAny()]
        if self.action == 'create':
            return [IsEditorOrAdmin()]
        if self.action == 'destroy':
            return [IsAdminRole()]
        # update / partial_update
        return [IsOwnerOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# ── Admin-only User List ──


class UserListView(ListAPIView):
    """Admin-only: list all users and their roles."""

    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [IsAdminRole]
