from django.db import models

# Create your models here.
# Create your models here.
class Clas(models.Model):
  num = models.IntegerField(verbose_name='人数',blank=True,null=True)

class Person(models.Model):
  name = models.CharField(max_length=20,verbose_name='姓名',blank=True,null=True)
  age = models.IntegerField(verbose_name='年龄',blank=True,null=True)
  score = models.FloatField(verbose_name='成绩',blank=True,null=True)
  grade = models.IntegerField(verbose_name='年级',blank=True,null=True)
  # 怎么才能灵活的处理已经存在的表?实验知可以直接修改,并进行迁移
  clas = models.ForeignKey(Clas,verbose_name='班级(外键)',blank=True,null=True,on_delete=models.CASCADE)
  # 外键的存储数据类似于对象(就是对象),以Clas外键显示的值为与该对象(外键的记录)的关联
  # 如同js中prototype的构造

# app.Person.grade: (fields.E120) CharFields must define a 'max_length' attribute.
  def __str__(self):
    return "%s-%d-%d-%d-%s"%(self.name,self.age,self.score,self.grade,"班级"+str(self.clas.pk))
# try git init: 无法起到全部清除的作用, 想清除应该直接删除