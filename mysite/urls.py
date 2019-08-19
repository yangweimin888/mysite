"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index),
    path('press_list/', views.press_list),  # 出版社列表
    path('edit_press/', views.edit_press),  # 编辑出版社
    path('delete_press/', views.delete_press),  # 删除出版社
    path('add_press/', views.add_press),  # 新增出版社
    path('book_list/', views.book_list),  # 书籍列表
    path('add_book/', views.add_book),  # 添加书籍
    path('delete_book/', views.delete_book),  # 删除书籍
    path('edit_book/', views.edit_book),  # 编辑书籍
    path('author_list/', views.author_list),  # 作者列表
    path('add_author/', views.add_author),  # 添加作者
    path('delete_author/', views.delete_author)  # 删除作者
]
