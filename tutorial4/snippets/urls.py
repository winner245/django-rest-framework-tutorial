from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),    # When we use class-based view, we need to call as_view() to get the view form class
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)