from django.urls import path
from .views import PostList, BlogInfo


urlpatterns = [
    path('', PostList.as_view()),

]