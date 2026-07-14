from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(),  name='blog-home'), # name can be referenced in templates instead of hardcoding path
    path('post/<int:pk>/', PostDetailView.as_view(),  name='post-detail'),
    path('about/', views.about, name='blog-about'),
]