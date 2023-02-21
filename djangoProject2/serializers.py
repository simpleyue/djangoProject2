# -*- coding: utf-8 -*-
# @author: chenhaibing
# @contact: chenhaibing@tal.com
# @Time : 2023/1/9 19:41

from demo.models import Person   #导入数据表模型
from rest_framework import serializers

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
