from django.shortcuts import render

# Create your views here.

def index(request):
  objs=Person.objects.all()
  return render(request,'index.html',locals())
  