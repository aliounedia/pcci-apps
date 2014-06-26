from django.contrib import admin
from models import  Main
from pcciprojects import settings
import util
from datetime import date
import datetime
from django.db.models import Avg, Count
from django.utils.translation import ugettext_lazy as _
from pcciprojects.daterange_filter.filter import DateRangeFilter


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
      ('Depassement', _('DMT Anormale')),
      ('NoDepassement', _('DMT Normale')),
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

class HourStartFilter(admin.SimpleListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = 'Heures Debut'

  # Parameter for the filter that will be used in the URL query.
  template = 'hour_start.html'
  parameter_name ='hour_start'

  def queryset(self, request, queryset):
    """
    Returns the filtered queryset based on the value
    provided in the query string and retrievable via
    `self.value()`.
    """
    # Compare the requested value (either '80s' or '90s')
    # to decide how to filter the queryset.

    pass

  def choices(self, cl):
    if not self.value():
       selected =  date.today().strftime("%d")
    else :selected = self.value()
    return util.hour_list(selected)
  
  def lookups(self, request, model_admin):
    """
    Returns a list of tuples. The first element in each
    tuple is the coded value for the option that will
    appear in the URL query. The second element is the
    human-readable name for the option that will appear
    in the right sidebar.
    """
    return [("first_input_day", "Heure de debut")]



class HourEndFilter(admin.SimpleListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = 'Heures Fin'

  # Parameter for the filter that will be used in the URL query.
  template = 'hour_end.html'
  parameter_name ='hour_end'

  def queryset(self, request, queryset):
    """
    Returns the filtered queryset based on the value
    provided in the query string and retrievable via
    `self.value()`.
    """
    # Compare the requested value (either '80s' or '90s')
    # to decide how to filter the queryset.

    pass
  def choices(self,cl):
    if not self.value():
       selected =  date.today().strftime("%d")
    else :selected = self.value()
    
    return util.hour_list(selected)
  
  def lookups(self, request, model_admin):
    """
    Returns a list of tuples. The first element in each
    tuple is the coded value for the option that will
    appear in the URL query. The second element is the
    human-readable name for the option that will appear
    in the right sidebar.
    """
    return [("first_input_day", "Heure de debut")]

  
class DateStartFilter(admin.SimpleListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = _('Jours Debut')

  # Parameter for the filter that will be used in the URL query.
  template = 'date_start.html'
  parameter_name = 'date_start'


  def queryset(self, request, queryset):
    """
    Returns the filtered queryset based on the value
    provided in the query string and retrievable via
    `self.value()`.
    """
    # Compare the requested value (either '80s' or '90s')
    # to decide how to filter the queryset.
    pass

  def choices(self,cl):
    if not self.value():
       selected =  date.today().strftime("%m/%d/%Y")
    else: selected =self.value()
    return ({"selected": selected}, )
  
      
  def lookups(self, request, model_admin):
    """
    Returns a list of tuples. The first element in each
    tuple is the coded value for the option that will
    appear in the URL query. The second element is the
    human-readable name for the option that will appear
    in the right sidebar.
    """
    return [("first_input_month", "Mois de debut")]



class DateEndFilter(admin.SimpleListFilter):
  # Human-readable title which will be displayed in the
  # right admin sidebar just above the filter options.
  title = _('Jours Fin')

  # Parameter for the filter that will be used in the URL query.
  template = 'date_end.html'
  parameter_name = 'date_end'
  get_params =['date_start', 'date_end']

  def queryset(self, request, queryset):
    """
    Returns the filtered queryset based on the value
    provided in the query string and retrievable via
    `self.value()`.
    """
    # Compare the requested value (either '80s' or '90s')
    # to decide how to filter the queryset.
    print 'get params'
    print request.GET.keys()
    print request.GET

    if set(self.get_params) & set(request.GET.keys()):
      print 'Ok'
      return Main.objects.filter(
            main_dateappel__gt =date.today())
    return  queryset
      
  def lookups(self, request, model_admin):
    """
    Returns a list of tuples. The first element in each
    tuple is the coded value for the option that will
    appear in the URL query. The second element is the
    human-readable name for the option that will appear
    in the right sidebar.
    """
    return [("first_input_month", "Mois de debut")]

  def choices(self,cl):
    if not self.value():
       selected =  date.today().strftime("%m/%d/%Y")
    else : selected = self.value()
    
    return ({"selected" : selected}, )
  
def build_params(get):
  return []
