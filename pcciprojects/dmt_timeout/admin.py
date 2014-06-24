# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from models import Main

from datetime import date

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from pcciprojects.daterange_filter.filter import DateRangeFilter

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

        print 'query'
        print self.value()
            
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'Depassement':
            return queryset.filter(main_tempscom__gt =480)
        if self.value() == 'NoDepassement':
           return queryset.filter(main_tempscom__lt=480)

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
        return Main.objects.filter(
            main_dateappel__gt =date.today()).values_list(
                "main_fichier", "main_fichier").distinct()


        
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


        print "The get  "
        print request.GET
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


        print "The get  "
        print request.GET
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


        print "The get  "
        print request.GET
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


        print "The get  "
        print request.GET
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
            main_dateappel__gt =date.today(),
            main_tempscom__isnull=False).order_by("-main_dateappel")
    
    
    search_fields = ['main_userid', 'main_fichier', 'on_timeout']
    list_display = ('main_userid',admin_main_fichier, admin_main_dateappel,
                    admin_main_tempscom, admin_timeout_count, admin_on_timeout)
    # No link 
    list_filter   = (
                     FirstInputDayFilter  ,LastInputDayFilter,
                     FirstInputMonthFilter,LastInputMonthFilter,
                     TimeOutListFilter,UserListFilter,FileListFilter
                     )

  
       
admin.site.register(Main, MainAdmin)

