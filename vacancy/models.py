from django.db import models

# Create your models here.
class Vacancies(models.Model):
    id = models.IntegerField(primary_key=True)
    posted = models.IntegerField()
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=30)

# 1 安装pymysql： pip installl pymysql
# python 3.6 中没有MySQLdb ,换成了pymysql
# 2 配置驱动：pymysql.install_as_MySQLdb()
# 在项目的init文件中导入
# import pymysql
# pymysql.install_as_MySQLdb()
# 这一步必须要，不然会报错：找不到mysqldb 包
# 因为django中默认为mysql 驱动包名为MySQLdb ，
# 但是我们安装的是 pymysql 所以有这一步
