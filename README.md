# README

## プロジェクトの作成

```sh
django-admin startproject todoproject .

```

.をつけると、今いる階層に、manage.pyとプロジェクトのフォルダが作成される。
付けないと、フォルダが作成されて、その中にmanage.pyとプロジェクトのフォルダが作成される。


## views.py

function based viewとclass based viewがある。


## urls.py

- メソッドで指定。
- クラスで指定。

## models.py

データを扱うファイル。

DBからデータを取ってくるための設計書。
自分でDBのデータを操作しようとすると覚えることも多い。

### DBとは？

図書館のシステム的なもの。

- ルールごとに本が並んでいる。
- 決められた棚に本が並んでいる。
- 本にはISBNが割り振られている

テーブルを作る。
カラムとデータ型を指定する必要がある。
(列の項目と、どのような構造のデータがそこに入るのか。)

## modle

DBの設計

### modelのfieldの種類を調べるには

「django model field　種類」
とかで検索してみる。

- qiita 「model fieldリファレンスの一覧」
- djangoオフィシャルサイトリファレンスで調べる(サイトのurlをen→jaに変えると日本語のリファレンスがすぐ見れる。)


## makemigrations　と　migrate

DBの中にtableを作るには2ステップ必要。

- makemigrations
    - models.pyファイルとDBの中間生成物。
    - コマンドを打つたびに、いちいちファイルが生成される。
    - この時点の状態のDBに戻したいということが、makemigrationsによって生成されるファイルより簡単に実現できる。

- migrate
    - DBに書き込みをしてtableを作成する。

```sh
# 1回目のみ、いろいろなtableが作成される。
#   Applying todo.0001_initial... OK　　のみ今回のmigrationに関係している。
(py36) Air:django_todo hina$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, todo
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
  Applying todo.0001_initial... OK
```


## データの操作をadminでするためには？

admin.pyにコードを書く必要あり。

## DBの考え方

C :作成する<br>
R :読み込む<br>
U :更新する<br>
D :削除する<br>

## templateViewとDB(CRUD)

|tempalteView|DB|
|---|---|
|createView|C|
|ListView,DetailView|R|
|UpdateView|U|
|DeleteView|D|

## tempalte_name

TemplateViewクラスにおいては、template_nameを指定するだけで、template＿nameを指定したクラスを呼び出した時に、template＿nameに代入されたhtmlファイルを呼び出すことができる

```py
# urls.pyでルーティングして、urlを受け取ったら、urls.pyのクラス呼び出しによって、hello.htmlを返すことができる(template_nameに代入されているファイルが返される決まり)
class HelloWorldView(TemplateView):
    template_name= 'hello.html'
```

## htmlとdjango


- html
<>タグで指定

- django

    - {% %}複雑な処理
    - {{ }}データ(DBのデータの取り扱い時)

## detail View 
- CRUDでいうR
- データの詳細を表示するとき向け
- 一個一個のデータを持ってくる


エラー
```
Generic detail view TodoDetail must be called with either an object pk or a slug in the URLconf.

object pkかslugによってどのデータを呼び出すかを指定しなければならない
```

ここのデータのどれを呼び出すかを指定する必要がある。    (pk=プライマリーキー。DBのデータを識別するID。djangoのデフォルトの機能によって　pkは自動的に全てのデータにふられるようになっている。)

<int:pk> = integer型のpk


## Bootstrap

たくさんのコードがかかれたcssファイル

たくさんのクラスが用意されている。クラスをhtmlに指定するだけで綺麗なcssを当てることができる。

<使い方>
- ダウンロード
- タグで使用する。

公式の、https://getbootstrap.com/docs/4.5/getting-started/introduction/
starter templateからbootstrapを使用する準備のタグを貼り付ける。


<使ったやつ>
- https://getbootstrap.com/docs/4.5/components/jumbotron/


### いい感じの幅にするやつ
divのclassにcontainerを指定すると、いい感じの見やすい幅にしてくれる

### ボタンタグ

リンクを貼る際は、
buttonタグではなくaタグを使用した方が、見た目を崩さずに形を構成していくことができる。

- https://getbootstrap.com/docs/4.5/components/buttons/
active stateを使用

class="btn btn-info"のinfoとかwarningとかで色をコントロールしている

### 改行

brタグじゃなくても、pタグで囲えば改行されるらしい

## 重複したコードの取り除き

base.htmlを使ってテンプレートを使い回す。

(一般的に共通する情報を入れているhtmlファイルんことをbase.htmlファイルとすることが多い。)

- base.html
    - block header
    - block content 
    - block sidebar
    - block footer
のように、画面の設計をbase.htmlでしておき、その設計に当てはまるように、その他のdetail.htmlや、list.htmlのコンテンツを当てはめていく。

## base.htmlとその他のファイルの関係

base.html<br>
ここにはレイアウトや、構成をきめる。
```
{% block header %}
{% endblock header %}

```

list.html<br>
実際にデータを入れる。
```
{% extends 'base.html' %}

{% block header %}
ここがheader
{% endblock header %}

```


## css

コンテナというクラスを使うと幅を見やすく整えることができる。
divのタグの中でクラス指定する。

## todolistの重要度によってtodolistのリストの背景色を変える

htmlに{{}}でデータのタグをいれる。
一個一個のitemデータの中に入っているpriorityカラムからデータを撮ってくることにする。

models.pyにpriorityのカラムを作る。

priorityには選択肢を持たせる。(choicesを使用すると選択肢を持たせることができる)


[https://qiita.com/nachashin/items/f768f0d437e0042dd4b3](https://qiita.com/nachashin/items/f768f0d437e0042dd4b3)

### models.py

models.pyを書き換えた後には必ずmakemigrationする！！！

### makemigrations

今現在、データTodoModelテーブルのなかにデータが存在しているが、duedateという新しいカラムが作られたために。
それらのデータに対して、duedateはどうするのか？という質問をされている。
ちなみに、djangoの場合は、デフォルトではなにかしらのデータをいれることを必要とされている。(nullを許容しない)

1)デフォルトの値をプロンプトで設定します。
2)作り直し、出直しします。models.py書き直して、デフォルトの値を設定します。

```
(py36) HinaMaeamanoAir:django_todo hina$ python3 manage.py makemigrations
You are trying to add a non-nullable field 'duedate' to todomodel without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 

```

データベースのデータの項目にnullを入れることを許容する(null=True)

デフォルトでは、データベースの項目には、null許容されておらず、null=Falseとなっている。


デフォルトの値を何で設定するか聞かれている。
例えば、今現在の時間とかどうですか？って聞いてくれているので、それで設定する。(timezone.now)
```
Select an option: 1       
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 

```

timezone.nowを設定する！

duedateと同様に、priorityについても、既存のデータのpriority項目に何も値が入っていないことは許容されないため、
プロンプトで設定をしていく。(2をタイプ)


```
You are trying to add a non-nullable field 'priority' to todomodel without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 

```

```
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> 

```

'danger'をタイプ。

(highじゃなくて、dangerなんだね。。。)
(表示のされ方ではなく、データの中身を指定しなくてはいけないのか。。。)

とりあえずデータに何か入れておく。


makemigrationsが終了すると、todo/migrationsの下にDBに対してどのような操作が行われるか書いてある中間ファイルが作成されているのが確認できる。

### migrate

makemigrationsをした後は、migrateをする！！！

DBに実際に操作が行われて、テーブル再作成、データを入れる

が行われる。


### ここではviews.pyにたいしてコード書くは必要ないのか？

views.pyにどのモデル使うとか、どのhtmlかとか書いてあるから、
もう、modelsのカラムを{{}}を使用して、html内で使用することができる。


## CreateView

DBの操作

c:create
r:read
u:update
d:delete


create=データを新しく作る！

create.htmlを作る

urlの繋ぎ込みをする(urls.py)

views.pyでクラスを作る



### html

    as_p=pタグとして
    データを送るフォームをpタグで囲む
    form.as_p=フォームの内容をpタグで囲む
    {{form.as_p}}

### エラー

```
ImproperlyConfigured at /create/
Using ModelFormMixin (base class of TodoCreate) without the 'fields' attribute is prohibited.
```

formで使用するmodel(データ)の項目(カラム)を指定してくださいというエラー

データのカラムの指定は、views.pyでfields変数を使用して指定する。


### エラー2

```
Forbidden (403)
CSRF verification failed. Request aborted.

```

セキュリティ上の脆弱性があるためリクエストは中断されました
という意味

（CSRF＝クロスサイトリクエストフォージェリ）


```
In the template, there is a {% csrf_token %} template tag inside each POST form that targets an internal URL.
```

{% csrf_token %}タグをいれてください、と言われているので、{% csrf_token %}をいれる。

create.htmlにタグを以下のように記入

```
<form action="" method="POST" >{% csrf_token %}


```


duedateの型
2020-08-03

### エラー3

```
NoReverseMatch at /create/
Reverse for '' not found. '' is not a valid view function or pattern name.
```

### reverse_lazy

モジュールはdjango.urlsからインポートする。

なぜ「reverse」 なのか。。。？


- 普通の流れ＝urlを指定してviewを表示する(urls.py→view.py)

- reverseの流れ＝viewで指定されたurlを表示する(views.py→urls.py)


view.pyに画面上からpostが成功して、フォームが送られてきて、成功したらどのurlを返すかは、

success_urlで指定する。

success_urlに指定するのは、

reverse_lazyでとってくるurl.

urlをとってくるために、

urls.pyのルーティングに、nameという項目を新しく作る。

```
    path('list/', TodoList.as_view()),

```
↓

```
    path('list/', TodoList.as_view(),name='list),

```


views.pyのなかのCreateTodoクラスの中で、
    success_url = reverse_lazy('list')
を指定する。

そうするとフォーム投稿成功時にlistと名前をurls.pyでつけた画面にリダイレクトすることができる。


## DeleteView
基本的にCreateViewと同じように、formで実装する。


views.pyの中で、DeleteViewクラスを継承したクラスを作成し、
urls.pyでクラス呼び出しする。

```
class TodoDelete(DeleteView):
```


deleteするデータの番号をdjangoは知っていないとdeleteできないため、
urlの指定は、プライマリーキーが必要になる。

```
    path('delete/<int:pk>', TodoDelete.as_view(),name='delete'),

```

## UpdateView

データを更新する時に適したテンプレート

これもurlの指定にはプライマリーキーが必要。
どのデータの更新をするのかをわかるようにするため。

htmlファイルの{{}} タグの書き方。


全部のデータ表示、
```
{{form.as_p}}
```
でもいけるが、


```
    <p>{{form.title}}</p>
    <p>{{form.memo}}</p>
    <p>{{form.priority}}</p>
    <p>{{form.duedate}}</p>

```
でも同じ！


## urlの繋ぎ込み
listの画面から、
update,delete,detailの画面に行けるように。

この画面の呼び方もリバースの呼びかた。

```
                    <a href="{% url 'update'  %}" class="btn btn-info" role="button" aria-pressed="true">編集</a>
                    <a href="{% url 'delete'  %}" class="btn btn-primary" role="button" aria-pressed="true">削除</a>
                    <a href="{% url 'detail'  %}" class="btn btn-success" role="button" aria-pressed="true">詳細</a>

```



### エラー
```
NoReverseMatch at /list/
Reverse for 'update' with no arguments not found. 1 pattern(s) tried: ['update/(?P<pk>[0-9]+)$']
```

urlで呼び出される個別の指示がされていないためエラー。
何番目のデータ？？ってなっている。


```
                    <a href="{% url 'update' item.pk %}" class="btn btn-info" role="button" aria-pressed="true">編集</a>
                    <a href="{% url 'delete' item.pk %}" class="btn btn-primary" role="button" aria-pressed="true">削除</a>
                    <a href="{% url 'detail' item.pk %}" class="btn btn-success" role="button" aria-pressed="true">詳細</a>

```

プライマリーキーを書いてあげる。