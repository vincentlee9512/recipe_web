from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('newblog/', views.new_blog, name='new_blog'),
    path('<int:single_blog_id>', views.single_blog, name='single_blog'),
    path('comment', views.comment, name='comment'),
    path('search', views.search, name='search'),
    path('category=<str:cate_type>', views.categorize, name='categorize'),
]