from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # IsAuthenticatedOrReadOnly: authenticated requests get read-write access, and unauthenticated requests get read-only access.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    # Override perform_create so that extra parameters are passed to the default create() method
    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    
class UserList(generics.ListAPIView): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView): 
    queryset = User.objects.all() 
    serializer_class = UserSerializer
