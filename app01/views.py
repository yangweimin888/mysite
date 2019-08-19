from django.shortcuts import render, redirect
from app01.models import User, Press, Book, Author
from django.conf import settings
import os
import time


def login(request):
    # 需要进行判断
    err_msg = ''  # 定义错误信息
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        ret = User.objects.filter(email=email, password=password)
        if ret:
            return redirect('/index/')
        else:
            err_msg = '用户名或者密码不正确，请重新输入'
    return render(request, 'login.html', {'err_msg': err_msg})


def index(request):
    """首页"""
    return render(request, 'index.html')


def press_list(request):
    """出版社列表"""
    # 1、去数据库查所有的出版社
    ret = Press.objects.all()
    # 2、在html页面上展示出来
    return render(request, 'press_list2.html', {'ret': ret})


def edit_press(request):
    """编辑出版社"""
    edit_id = request.GET.get('id')  # 获取需要操作的出版社id
    if request.method == 'POST':
        edit_name = request.POST.get('edit_name')
        edit_press_obj = Press.objects.get(id=edit_id)
        edit_press_obj.name = edit_name  # 更改出版社名称
        edit_press_obj.save()  # 将更改后的名称提交到数据库
        return redirect('/press_list/')
    ret = Press.objects.get(id=edit_id)
    return render(request, 'edit_press2.html', {'press_obj': ret})


def delete_press(request):
    """删除出版社"""
    delete_id = request.GET.get('id')
    Press.objects.get(id=delete_id).delete()  # 根据出版社id删除对应的数据
    return redirect('/press_list/')


def add_press(request):
    """增加出版社"""
    if request.method == 'POST':
        add_name = request.POST.get('add_name')
        Press.objects.create(name=add_name)  # 将新增的出版社名称保存到数据库中
        return redirect('/press_list/')
    return render(request, 'add_press2.html')


def book_list(request):
    """书籍列表"""
    data = Book.objects.all()  # 查询出所有的书籍
    return render(request, 'book_list2.html', {'data': data})


def add_book(request):
    """添加书籍"""
    if request.method == 'POST':
        press_id = request.POST.get('press_id')
        book_title = request.POST.get('book_title')
        Book.objects.create(title=book_title, press_id=press_id)  # 将获取到书名添加至数据库
        return redirect('/book_list/')
    press = Press.objects.all()
    return render(request, 'add_book2.html', {'press_list': press})


def delete_book(request):
    """删除书籍"""
    book_id = request.GET.get('id')
    Book.objects.filter(id=book_id).delete()  # 根据获取的书籍id删除对应的数据
    # return redirect('/book_list/')
    return render(request, 'delete_success.html')


def edit_book(request):
    """编辑书籍"""
    book_id = request.GET.get('id')  # 获取书籍的id
    edit_book_obj = Book.objects.get(id=book_id)
    if request.method == 'POST':
        edit_title = request.POST.get('edit_book')
        edit_press_id = request.POST.get('press_id')
        edit_book_obj.title = edit_title  # 更改书籍名称
        edit_book_obj.press_id = edit_press_id
        edit_book_obj.save()  # 保存书籍
        return redirect('/book_list/')
    press_data = Press.objects.all()
    return render(request, 'edit_book2.html', {'book_obj': edit_book_obj, 'press_list': press_data})


def author_list(request):
    """作者列表"""
    author_data = Author.objects.all()  # 拿到所有的作者信息
    return render(request, 'author_list.html', {'author_list': author_data})


def add_author(request):
    """添加作者"""
    # 查询所有书籍信息
    if request.method == 'POST':
        author_name = request.POST.get('add_author')
        book_ids = request.POST.getlist('book_id')
        # 将获取到的数据存入数据库中
        author = Author.objects.create(name=author_name)  # 创建作者
        author.books.add(*book_ids)  # 参数是一个一个的id值
        # author.books.set(book_ids)  # 参数是id值的列表
        return redirect('/author_list/')
    books = Book.objects.all()
    return render(request, 'add_author.html', {'books': books})


def delete_author(request):
    """删除作者"""
    author_id = request.GET.get('id')
    Author.objects.get(id=author_id).delete()
    return redirect('/author_list/')


def edit_author(request):
    """编辑作者"""
    edit_author_id = request.GET.get('id')  # 获取需要编辑的作者id
    auth_obj = Author.objects.get(id=edit_author_id)
    if request.method == 'POST':
        edit_author_name = request.POST.get('edit_author_name')  # 获取编辑后的作者名称
        edit_book_ids = request.POST.getlist('book_ids')   # 获取需要编辑的书籍id
        auth_obj.name = edit_author_name
        auth_obj.books.set(edit_book_ids)
        auth_obj.save()  # 保存提交数据
        return redirect('/author_list/')
    books = Book.objects.all()
    return render(request, 'edit_author.html', {'author_list': auth_obj, 'books': books})


def upload(request):
    """上传文件"""
    if request.method == 'POST':
        file_obj = request.FILES.get('file_name')
        file_name = file_obj.name
        if os.path.exists(os.path.join(settings.BASE_DIR, file_name)):
            file_name += time.strftime('%Y-%m-%d')  # 如果文件存在重复，则增加时间戳
        with open(file_name, 'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
    return render(request, 'upload.html')
