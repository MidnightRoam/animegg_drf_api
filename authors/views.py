from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer


class AuthorModelViewSet(ModelViewSet):
    """Author model view set"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
