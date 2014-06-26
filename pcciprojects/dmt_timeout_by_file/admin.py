# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import MainGeneric, Main
from filters import *


from django.contrib import admin


class MainAdmin(admin.ModelAdmin):
  def __init__(self, *args, **kwrags):
      MainGeneric.populate()
      super(MainAdmin, self).__init__(*args, **kwrags)
      
  def get_readonly_fields(self, request, obj=None):
      return [f.name for f in self.model._meta.fields]
      
  def admin_on_timeout(self):
      if self.on_timeout()== True:
          return '<img src= "/static/admin/img/icon_error.gif"/>'
      return  '<img src= "/static/admin/img/icon_success.gif"/>' 

  admin_on_timeout.short_description ="Statut"
  admin_on_timeout.allow_tags        =True    
                     
  def queryset(self, request):
    print 'Boot ...............'
    qs =  super(MainAdmin, self).queryset(request)
    print 'End boot ...........'
    return qs

  list_display = ('main_userid','main_timeout_count', 'main_tempscom',
                  admin_on_timeout)
  list_filter   = (
    HourStartFilter, HourEndFilter,
    DateStartFilter, DateEndFilter,
    TimeOutListFilter,UserListFilter
  )
        
admin.site.register(MainGeneric, MainAdmin)

