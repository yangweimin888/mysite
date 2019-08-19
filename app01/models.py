from django.db import models


class User(models.Model):
    """新建用户信息表"""
    id = models.AutoField(primary_key=True)
    email = models.CharField('邮箱', max_length=32)
    password = models.CharField('密码', max_length=32)

    def __str__(self):
        return self.email


class Press(models.Model):
    """出版社表"""
    id = models.AutoField(primary_key=True)
    name = models.CharField('出版社名称', max_length=24)

    def __str__(self):
        return self.name


class Book(models.Model):
    """书籍"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)  # 书名
    price = models.IntegerField(default=12)  # 价格
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    """作者"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)  # 作者姓名
    books = models.ManyToManyField(to='Book')  # 创建作者和书籍多对多的关系

    def __str__(self):
        return self.name
