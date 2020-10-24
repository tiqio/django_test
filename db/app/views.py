from django.shortcuts import render

# Create your views here.
# 视图就是python函数

from django.http import HttpResponse
# 在运用框架时,引用往往必不可少

def index(request):
  return HttpResponse('some words')
def detail(request,num):
  return HttpResponse('detail-%s'%num)

from .models import Person
def persons(request):
  personsList = Person.objects.all()
  # Person应该是个数据表,包含着记录,而不是一个单纯的类
  return render(request, 'app/persons.html',{'persons':personsList})