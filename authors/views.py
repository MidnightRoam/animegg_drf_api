from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Author
from .serializers import AuthorSerializer


class AuthorModelViewSet(ModelViewSet):
    """Author model view set"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self):
        """Returns list of all author objects"""
        queryset = Author.objects.prefetch_related('anime', 'manga').all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
