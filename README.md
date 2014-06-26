pcci-apps
=========

apps run at PCCI

![Alt text](https://raw.githubusercontent.com/aliounedia/pcci-apps/master/docs/dmt_timeout_screen.JPG "Optional title")



* this app run on django Django-1.6.5 , The latest version when 
I wrote it with python 27. It monitor The DMC (Maximal call 
duration ) and DMT (Maximal call handling) to each outband call
to alert timemout. 90 percent of code is into admin.py and
models.py


* installing app dmt_timeout 

**install django :
  see https://www.djangoproject.com

**create app
  manage.py startapp dmt_timeout

**install models.py for existing mysql pcci database
python manage.py inspectdb > dmt_timeout/models.py

** remove not using models into models.py
 For me I use only Main , Statistiques

** change some type field to take adventage of the powefull django 
 ORM .For me only one change Type I done Here :

# change CharField to IntegerField  
main_tempscom = models.CharField(db_column='Main_TempsCom',
     max_length=20, blank=True) # Field name made lowercase.
to 
main_tempscom = models.IntegerField(db_column='Main_TempsCom', 
    max_length=20, blank=True) # Field name made lowercase.

  

* Hack on The django admin site
To enabble calendar filter work , I add some lines hack to The
django admin base.html , so add Theses following lines into <head> . 
If you fine a more proper way to do that you are welcome
   

<!-- Hack pcci - admin  -->
<link rel="stylesheet" href="//code.jquery.com/ui/1.10.4/themes/
	smoothness/jquery-ui.css">
<script src="//code.jquery.com/jquery-1.10.2.js"></script>
<script src="//code.jquery.com/ui/1.10.4/jquery-ui.js"></script>
<link rel="stylesheet" href="/resources/demos/style.css">
<script>
$(function() {
$( "#datepicker1" ).datepicker();
$( "#datepicker2" ).datepicker();

});
</script>

<!--End hack --> 
  
* Sync db 
manage.py syncdb 

  
* Run server
manage.py runserver HOST:PORT

 
