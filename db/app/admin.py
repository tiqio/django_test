from django.contrib import admin
from .models import Person

# Register your models here.
class GradesAdmin(admin.ModelAdmin):
  # list_display = ['name','age','score','grade'] 
  # list_filter = ['name']
  # search_fields = ['name'] 没list_filter好用
  # list_per_page = 5
  # 增加,修改页属性
  # fields = ['age','name','score','grade']
  # fieldsets = [
  #   ("num",{"fields":['score','age','grade']}),
  #   ("others",{"fields":['name']})
  # ] 是一种fields扩展与fields冲突

admin.site.register(Person,GradesAdmin)

