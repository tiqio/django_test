from django.urls import path,re_path
from . import views

urlpatterns = [
  path('', views.index),
  # re_path(r'(^\d+$)',views.detail),

  path('persons',views.persons),
  path('clas',views.clas),
  re_path(r'(^\d+$)',views.in_clas)
]