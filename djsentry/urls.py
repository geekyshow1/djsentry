from django.contrib import admin
from django.urls import path
from blog.views import home, posts
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('posts/', posts, name='posts')
]
