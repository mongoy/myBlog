from django.urls import path
from .views import PostList, PostCreateView


urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
]
