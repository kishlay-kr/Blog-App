"""bolg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import BlogListView , BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name='bolg'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',BlogListView.as_view(), name='homepage'),
    path('<int:pk>',BlogDetailView.as_view(), name='detail_url'),
    path('create/',BlogCreateView.as_view(), name='create_url'),
    path('<int:pk>/update/',BlogUpdateView.as_view(), name='update_url'),
    path('<int:pk>/delete',BlogDeleteView, name='delete_url'),
]
