from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView  #视图
from rest_framework.response import Response  #响应
from demo.models import Person   #数据表模型
from djangoProject2.serializers import PersonModelSerializer   #序列化器
from rest_framework import status   #接口状态码
import json
import logging
from utils import g
from django_redis import get_redis_connection
conn = get_redis_connection()
conn.set('chenhaibing3','233333',ex=3600)

#设置logger对象
log = logging.getLogger('log')
#访问接口的时候，直接"hello Django API"。实际应用中，可以添加复杂的逻辑，最后给出返回值即可
# def demo_res(request):
#     return HttpResponse("hello Django API")

class RecordList(APIView):
    res = {
        'code': status.HTTP_200_OK,
        'data':None,
        'msg': 'success',
    }

    """通过post请求时，实现插入数据的功能"""
    def post(self,request):
        #获取前端传入的请求体数据
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        data = {
            'first_name':first_name,
            'last_name': last_name,
        }
        print("data>>>>>>",data)
        #update_or_create需要提供一个查询参数，先查询，如果不存在，则插入，如果存在，则更新。这里设置id为None,可以达到直接插入的效果
        obj,iscreated= Person.objects.update_or_create(defaults=data,id=9)
        print("插入结果>>>>>>>",obj,iscreated)
        return Response(self.res)

    """通过get请求时，实现查询数据库并返回给接口的功能 """
    def get(self,request):
        #获取接口传入的数据
        first_name = request.GET.get('first_name')

        b = conn.get('chenhaibing3')

        #根据first_name查询数据库，根据id降序排序
        data_obj = Person.objects.filter(first_name=first_name).order_by('id').reverse()

        #data_obj>>>>>> <class 'django.db.models.query.QuerySet'> <QuerySet [<Person: Person object (5)>]>
        #print('data_obj>>>>>>',type(data_obj),data_obj)

        #实例化序列器
        ser = PersonModelSerializer(instance=data_obj,many = True)

        g.set_value('gh', 'shide')
        print(f'刚才设置的全局变量是：{g.get_value("gh")}')

        if ser.data:
            #获取序列化后的数据，只返回第一条
            self.res['data'] = ser.data[0]
            self.res['redis'] = b

        log.info(f'查询结果是: {self.res}')
        # 将数据返给接口
        return Response(self.res)

    #删除数据
    def delete(self, request):
        first_name = request.GET.get('first_name')
        obj = Person.objects.filter(first_name = first_name).delete()
        self.res['data'] = obj
        return Response(self.res)

