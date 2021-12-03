from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.serializers import UserSerializer
from rest_framework import renderers
from snippets.views import SnippetViewSet, UserViewSet  

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})



urlpatterns = [
    path('', views.api_root),
    path('snippets/', snippet_list, name='snippet-list'),    # When we use class-based view, we need to call as_view() to get the view form class
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
    path('users/', user_list, name='user-list'), 
    path('users/<int:pk>/', user_detail, name='user-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)