from django.db import models


class Group(models.Model):
    name = models.CharField(verbose_name='Name', unique=True, max_length=64)
    course = models.CharField(verbose_name='Course', max_length=64)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


class Student(models.Model):
    first_name = models.CharField(verbose_name='First_Name', max_length=64)
    last_name = models.CharField(verbose_name='Surname', max_length=64)
    patronymic = models.CharField(verbose_name='Patronymic', max_length=64)
    email = models.EmailField(verbose_name='Email', unique=True, max_length=64)
    phone = models.CharField(verbose_name='Phone', unique=True, max_length=64)
    group_id = models.ForeignKey(Group, verbose_name='Group', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
