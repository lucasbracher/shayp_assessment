from rest_framework import viewsets, permissions
from shayp_assessment.library.models import Book, User
from shayp_assessment.library.serializers import UserBookSerializer, BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('-date_joined')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]