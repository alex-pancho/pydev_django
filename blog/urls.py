from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_index, name='index'),
    path('post/<int:post_id>/', views.post_detail, name='detail'),
]