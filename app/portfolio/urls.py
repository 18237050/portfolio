from django.urls import path
from . import views

app_name= 'portfolio'
urlpatterns = [
    # viewsからindexを読み込んで、nameをindexに
    path('', views.index, name='index'),
    path('works',views.works,name='works'),
]
#上記のpathは('url今回はlocalhostなので空',views内のindex関数,nameの設定)を行う