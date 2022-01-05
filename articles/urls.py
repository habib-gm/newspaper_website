from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    CreateArticleView,
)
urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'), # new
    path('', ArticleListView.as_view(), name='article_list'),
    path('create', CreateArticleView.as_view(), name ="create_article")
]