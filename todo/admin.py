## 管理画面の操作をするために使う

from django.contrib import admin
from .models import TodoModel

# Register your models here.


# admin.site.register(作ったモデル名)

admin.site.register(TodoModel)