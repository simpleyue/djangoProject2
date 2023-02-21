
from django.urls import path

#导入views视图
from demo import views

urlpatterns = [
    #path("routerDemo/", views.demo_res),#routerDemo为访问路径，views.demo_res为当前路径想要映射到的函数
    path("recordlist",views.RecordList.as_view())
]
