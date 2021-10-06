from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, UpdateView, CreateView, DetailView
from .models import News
from .forms import NewsForm


class NewsListView(ListView):
    model = News
    template_name = 'news_portal/list.html'
    context_object_name = 'news'
    ordering = ['-id']
    paginate_by = 1
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context["form"] = NewsForm()
        return context