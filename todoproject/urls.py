from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 入力：http://localhost:8000
    # 出力：そのurlをtodoアプリに渡す
    # ''でurlを指定している時、アプリの画面を呼び出す、ができる
    path('',include('todo.urls'))
]
