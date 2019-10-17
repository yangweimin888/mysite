# -*- coding: utf-8 -*-
# @Time    : 2019/10/17 17:13
# @Author  : YangWeiMin
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login),
    path('index/', views.index),
    path('press/', views.press_list, name='press_list'),  # 出版社列表
    path('edit_press/<int:edit_id>/', views.edit_press),  # 编辑出版社
    path('delete_press/<int:delete_id>/', views.delete_press),  # 删除出版社
    path('add_press/', views.AddPress.as_view()),  # 新增出版社
    path('book_list/', views.book_list),  # 书籍列表
    path('add_book/', views.add_book),  # 添加书籍
    path('delete_book/', views.delete_book),  # 删除书籍
    path('edit_book/', views.edit_book),  # 编辑书籍
    path('author_list/', views.author_list),  # 作者列表
    path('add_author/', views.add_author),  # 添加作者
    path('delete_author/', views.delete_author),  # 删除作者
    path('edit_author/', views.edit_author),  # 编辑作者
    path('upload/', views.upload),  # 上传文件
    path('get_book/', views.get_book),  # 获取书籍信息
    path('custom_filter/', views.test_custom_filter),  # 测试自定义filter
    path('test/', views.test),
    path('home/<int:year>/10/', views.home),
]