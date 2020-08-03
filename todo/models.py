from django.db import models

# Create your models here.

#TodoModelテーブルのpriorityカラムの中で使用する選択肢
# 選択肢(choices)はタプル型のデータでつくる!!!!!
# ("呼び出したデータの中身、データの名前が入る","画面上に表示される文字列")という形式で書く
# danger,info,successはbootstrapのなかのclassの文字列の一部。
# high,normal,lowは選択肢3つ作るやつの、選択肢の項目になる。TodoListの項目の「優先度は、高いか、普通か、低いか」という要件に基づいて作られた。
PRIORITY = (('warning','high'),('info','normal'),('success','low'))



# tableを作る

# TodoModelクラスによって、TodoModelオブジェクトが生成される。
class TodoModel(models.Model):
    # 項目を作る
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        # 選択肢をpriorityに持たせたい
        choices = PRIORITY
    )
    duedate = models.DateField()
    #pythonの文法(特殊メソッド)
    #オブジェクトを文字列型として返す
    #オブジェクトの
    def __str__(self):
        # helloがTodoModelオブジェクトのかわりに返される。
        # return "hello"
        # TodoModelオブジェクトのタイトルが文字列型として、オブジェクトのかわりに返される。
        return self.title