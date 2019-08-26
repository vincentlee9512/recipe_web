from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('newblog/', views.new_blog, name='new_blog'),
    path('modifyblog/<int:blog_id>', views.modify_blog, name='modify_blog'),
    path('<int:single_blog_id>', views.single_blog, name='single_blog'),
    path('comment', views.comment, name='comment'),
    path('like', views.like, name='like'),
    path('unlike', views.unlike, name='unlike'),
    path('search', views.search, name='search'),
    path('category=<str:cate_type>', views.categorize, name='categorize'),
    path('personal_likes', views.personal_likes, name='personal_likes'),
]
