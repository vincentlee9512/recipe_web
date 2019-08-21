from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('blogs/', include('blogs.urls')),
    path('admin/', admin.site.urls),
]
