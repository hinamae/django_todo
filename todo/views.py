from django.shortcuts import render

#ListView(CRUDのRにあたる)をインポート
from django.views.generic import ListView
#ListView(CRUDのRにあたる)をインポート
from django.views.generic import DetailView
#CreateView(CRUDのCにあたる)をインポート
from django.views.generic import CreateView
#DeleteView(CRUDのDにあたる)をインポート
from django.views.generic import DeleteView
#UpdateView(CRUDのUにあたる)をインポート
from django.views.generic import UpdateView




#modelsファイルで定義したモデルをインポート!!!!!!!!
from .models import TodoModel



#reverse_lazy関数をインポート
from django.urls import reverse_lazy


# ListViewを継承して便利な機能をたくさん使用する！
class TodoList(ListView):
    #TodoListが呼び出された際list.htmlが返される。
    template_name = 'list.html'
    #list.htmlで使用している、modelを指定する
    model = TodoModel

# DetailViewを継承して便利な機能をたくさん使用する！
class TodoDetail(DetailView):
    template_name= 'detail.html'
    model = TodoModel


# CreateViewを継承して便利な機能をたくさん使用する！

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')

    #データの作成が成功した時に、どういう画面を返すか指定する
    #sucess_url=どの画面を返すか指定する
    #reverse_lazy=クラスで使用する場合はreverse_lazyを使用する。
    #defで作成している場合は、画面を返す際はreverseを使用する。(ちなみに。)
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')


class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    success_url = reverse_lazy('list')
    #filedsに指定することによって、どのカラムを更新するのかを指定することができる。(例えば更新されたくないカラムがある場合には便利)
    #ここでは全てweb上でデータを更新する権限を与えることにする
    fields = ('title','memo','priority','duedate')
