from django.db import models

# Create your models here.
# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length=20,verbose_name='姓名',blank=True,null=True)
  age = models.IntegerField(verbose_name='年龄',blank=True,null=True)
  score = models.FloatField(verbose_name='成绩',blank=True,null=True)
  grade = models.IntegerField(verbose_name='年级',blank=True,null=True)
# app.Person.grade: (fields.E120) CharFields must define a 'max_length' attribute.
  def __str__(self):
    return "%s-%d-%d-%d"%(self.name,self.age,self.score,self.grade)
# ValueError: Field 'grade' expected a number but got ''.
# This is a master section
# This is nogood 
# try git init: 无法起到全部清除的作用, 想清除应该直接删除