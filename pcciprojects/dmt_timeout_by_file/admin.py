# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import MainGeneric, Main
from pcciprojects import settings

from datetime import date
import datetime

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from pcciprojects.daterange_filter.filter import DateRangeFilter
from django.db.models import Avg, Count , Sum

class TimeOutListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('decade born')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('Depassement', _('Depassement duree  traitement appel ')),
            ('NoDepassement', _('pas de Depassement duree  traitement appel')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
            
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'Depassement':
            return queryset.filter(main_tempscom__gt =settings.TIMEOUT)
        if self.value() == 'NoDepassement':
           return queryset.filter(main_tempscom__lt=settings.TIMEOUT)

class FileListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('file filter title')
    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'file'

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.


        print "The request "
        if self.value():
            return queryset.filter(main_fichier =self.value())
        
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return ()
        
class UserListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('user filter title')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'user'

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        print "The request "
        if self.value():
            return queryset.filter(main_userid =self.value())
        
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return Main.objects.filter(
            main_dateappel__gt =date.today()).values_list(
                "main_userid", "main_userid").distinct()


class FirstInputDayFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Jour: Debut'

    # Parameter for the filter that will be used in the URL query.
    template = 'first_input_day_filter.html'
    parameter_name = 'first_input_day'

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value():
            return queryset.filter(main_userid =self.value())
        
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """

        return [("first_input_day", "Heure de debut")]

class LastInputDayFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Jour:Fin'

    # Parameter for the filter that will be used in the URL query.
    template = 'last_input_day_filter.html'
    parameter_name = 'last_input_day'

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value():
            return queryset.filter(main_userid =self.value())
        
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [("last_input_day", "Heure de Fin")]

    def choices(self, cl):
        print 'The choices' , self.value()
        return [self.value()]
    
class FirstInputMonthFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Jour: Debut')

    # Parameter for the filter that will be used in the URL query.
    template = 'first_input_month_filter.html'
    parameter_name = 'first_input_month'

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value():
            return queryset.filter(main_userid =self.value())
        
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return Main.objects.filter(
            main_dateappel__gt =date.today()).values_list(
                "main_userid", "main_userid").distinct()


class LastInputMonthFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Jour: Fin'

    # Parameter for the filter that will be used in the URL query.
    template = 'last_input_month_filter.html'
    parameter_name = 'last_input_month'

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value():
            return queryset.filter(main_userid =self.value())
        
    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (("main_userid", "main_userid"),)



class MainAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return [f.name for f in self.model._meta.fields]
        

    def admin_on_timeout(self):
        if self.on_timeout()== True:
            return '<img src= "/static/admin/img/icon_error.gif"/>'
        return  '<img src= "/static/admin/img/icon_success.gif"/>' 

    admin_on_timeout.short_description ="Statut"
    admin_on_timeout.allow_tags        =True    
    
    
    def boot(self):
        print 'generic all ..'
        print MainGeneric.objects.all()
        #MainGeneric.objects.all().delete()
        list = Main.objects.filter(main_dateappel__gt = date.today()).\
            values("main_userid").annotate(
            Count('main_userid'), Avg('main_tempscom')
            )
        for i in list :
            MainGeneric.objects.create(
            main_userid  = i.get("main_userid"),
            main_timeout_count = i.get("main_userid__count"),
            main_tempscom = i.get("main_tempscom__avg")
           )                     
    def queryset(self, request):
        print 'Boot ...............'
        self.boot()
        qs=  super(MainAdmin, self).queryset(request)
        print 'End boot ...........'
        return qs
    
    list_display = ('main_userid','main_timeout_count', 'main_tempscom',
                    admin_on_timeout)
    list_filter   = (
        FirstInputDayFilter ,LastInputDayFilter,
        FirstInputMonthFilter,LastInputMonthFilter,
        TimeOutListFilter,UserListFilter
    )

  
       
admin.site.register(MainGeneric, MainAdmin)

