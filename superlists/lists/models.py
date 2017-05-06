from django.db import models

# Create your models here.


class List(models.Model) : 
    text = models.TextField(default = '')


class Item(models.Model) : 
    text = models.TextField(default = '')
    the_list = models.ForeignKey(List, default = None)
    create_datetime = models.DateTimeField(auto_now_add = True)
