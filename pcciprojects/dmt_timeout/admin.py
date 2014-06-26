# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import Main

from datetime import date

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from pcciprojects.daterange_filter.filter import DateRangeFilter
from filters import *

class MainAdmin(admin.ModelAdmin):
  def get_readonly_fields(self, request, obj=None):
    return [f.name for f in self.model._meta.fields]
      
  def admin_main_dateappel(self):
    return self.main_dateappel.hour
  admin_main_dateappel.short_description ="Heure Appel"

  def admin_main_fichier(self):
    return self.main_fichier
  admin_main_fichier.short_description ="Fichier"

  def admin_main_tempscom(self):
    return self.main_tempscom
  admin_main_tempscom.short_description ="DMT"

  def admin_timeout_count(self):
    return self.timeout_count()
  admin_timeout_count.short_description ="Nombre"

  def admin_on_timeout(self):
    if self.on_timeout()== True:
      return '<img src= "/static/admin/img/icon_error.gif"/>'
    return  '<img src= "/static/admin/img/icon_success.gif"/>' 

  admin_on_timeout.short_description ="Statut"
  admin_on_timeout.allow_tags        =True    

  #list_display_links = (None,)
  def queryset(self, request):
    return super(MainAdmin, self).queryset(request).filter(
      main_dateappel__gt =date.today()).\
      exclude(main_tempscom__isnull=True).\
          order_by("-main_dateappel")


  search_fields = ['main_userid', 'main_fichier', 'on_timeout']
  list_display = ('main_userid',admin_main_fichier,
    admin_main_dateappel,
    admin_main_tempscom,
    admin_timeout_count,
    admin_on_timeout
  )
  # No link 
  list_filter   = (
   HourStartFilter, HourEndFilter,
   DateStartFilter, DateEndFilter,
   TimeOutListFilter,UserListFilter,
   FileListFilter
)


     
admin.site.register(Main, MainAdmin)

