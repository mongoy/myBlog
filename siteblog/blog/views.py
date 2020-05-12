from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import MyPost


class BlogInfo(TemplateView):
    """Сводная информация на главной странице"""
    template_name = 'base.html'


class PostList(ListView):
    model = MyPost
    queryset = MyPost.objects.all()
    # template_name = 'base.html'
    template_name = 'blog/mypost_list.html'
    paginate_by = 10

