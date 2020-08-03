from django.urls import path
from .views import TodoList, TodoDetail,TodoCreate,TodoDelete,TodoUpdate

urlpatterns = [
    #todoリストを表示させる画面用のurl
    #クラスで呼び出しするので.as_view()メソッドを使用する。(メソッドorクラスで呼び出す。)
    path('list/', TodoList.as_view(), name='list'),
    #djangoがどのデータを持ってきたらいいのかわかるようにpk(プライマリーキーを指定する。)
    #<int:pk> = integer型のpk
    # path('detail/', TodoDetail.as_view()),
    path('detail/<int:pk>', TodoDetail.as_view(),name='detail'),
    #/createというurlがよびだされると、TodoCreateクラスを呼び出す
    path('create/', TodoCreate.as_view(),name='create'),
    #/detele/{プライマリーキー}というurlがよびだされると、TodoDeleteクラスを呼び出す
    path('delete/<int:pk>', TodoDelete.as_view(),name='delete'),
    #/update/{プライマリーキー}というurlがよびだされると、TodoUpdateクラスを呼び出す
    path('update/<int:pk>', TodoUpdate.as_view(),name='update'),

]
