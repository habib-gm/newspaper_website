from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 
from .models import Article
from django.core.exceptions import PermissionDenied
    
class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    
class ArticleDetailView(DetailView): 
    model = Article
    template_name = 'article_detail.html'
    
class ArticleUpdateView(LoginRequiredMixin, UpdateView): 
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    
class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

class CreateArticleView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = "__all__"    
    success_url = reverse_lazy('article_list')
    login_url = 'login'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs): # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    