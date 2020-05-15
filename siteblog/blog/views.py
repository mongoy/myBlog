from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView
from .models import MyPost
from .forms import PostCreatForm


class BlogInfo(TemplateView):
    """Сводная информация на главной странице"""
    template_name = 'base.html'


class PostList(ListView):
    model = MyPost
    queryset = MyPost.objects.all()
    # template_name = 'base.html'
    template_name = 'blog/mypost_list.html'
    paginate_by = 10


class PostCreateView(CreateView):
    """ """
    model = MyPost
    form_class = PostCreatForm
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, '{}'.format(form.instance))
        return result
