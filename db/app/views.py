from django.shortcuts import render

# Create your views here.
# 视图就是python函数

from django.http import HttpResponse

def index(request):
  return HttpResponse('some words')
def detail(request,num):
  return HttpResponse('detail-%s'%num)
