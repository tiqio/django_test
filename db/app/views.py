from django.shortcuts import render

# Create your views here.
# 视图就是python函数

from django.http import HttpResponse
# 在运用框架时,引用往往必不可少

def index(request):
  return HttpResponse('some words')
# def detail(request,num):
#   return HttpResponse('detail-%s'%num)

from .models import Person, Clas
def persons(request):
  personsList = Person.objects.all()
  # Person应该是个数据表,包含着记录,而不是一个单纯的类
  return render(request, 'app/persons.html', {'persons':personsList})

def clas(request):
  clasList = Clas.objects.all()
  return render(request, 'app/clas.html', {'clases':clasList})

def in_clas(request,num):
  # clasList = Clas.person_set.all() Clas不是对象,没有person_set.all方法
  # clasList = Clas.objects.get(pk = num) 得到的是对象,是无法遍历的
  clas = Clas.objects.get(pk = num)
  personsList = clas.person_set.all()
  return render(request,'app/persons.html',{'persons':personsList})
