from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.AutoField(primary_key = True)  #设置自增主键
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "CHBperson"  #设置表名
