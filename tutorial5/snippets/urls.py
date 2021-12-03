from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from snippets.serializers import UserSerializer

urlpatterns = [
    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),    # When we use class-based view, we need to call as_view() to get the view form class
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'), 
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]


urlpatterns = format_suffix_patterns(urlpatterns)