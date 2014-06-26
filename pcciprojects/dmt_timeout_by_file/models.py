# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals
from datetime import date
from django.db import models
from django.db.models import Avg, Count
from datetime import date
import datetime
           
class MainGeneric(models.Model):
  main_tempscom = models.IntegerField(db_column='Main_TempsCom', max_length=20, blank=True) # Field name made lowercase.
  main_userid   = models.CharField(db_column='Main_UserID', max_length=4, blank=True) # Field name made lowercase.
  main_timeout_count  = models.CharField(db_column='Main_Timeout_Count', max_length=4, blank=True)


  def on_timeout(self):
    if self.main_tempscom and int(self.main_tempscom)>300:
        return True
    return False

  @classmethod
  def populate(cls, list=None):
    """
    This method fill the MainGeneric table with The given Main list
    before filling , content are removed from database table , and
    and datas are grouped
    """
    print 'generic all ..'
    print cls.objects.all().count()
    #cls.objects.all().delete()
    print 'end generic all ..'
    if not list:
      list = Main.objects.filter(main_dateappel__gt = date.today() - datetime.timedelta(days =30)).\
      values("main_userid").annotate(
        Count('main_userid'), Avg('main_tempscom')
     )
        
    print list
    for i in list :
      cls.objects.create(
        main_userid  = i.get("main_userid"),
        main_timeout_count = i.get("main_userid__count"),
        main_tempscom = i.get("main_tempscom__avg")
      )

  class Meta:
    managed = False
    db_table = 'main_timeout'
    verbose_name = "DMT monitoring global"
        
class Main(models.Model):
  main_id = models.BigIntegerField(db_column='Main_ID', primary_key=True ) # Field name made lowercase.
  main_tel = models.CharField(db_column='Main_Tel', max_length=15, blank=True) # Field name made lowercase.
  main_fax = models.CharField(db_column='Main_Fax', max_length=50, blank=True) # Field name made lowercase.
  main_gsm = models.CharField(db_column='Main_GSM', max_length=25, blank=True) # Field name made lowercase.
  main_siret = models.TextField(db_column='Main_Siret', blank=True) # Field name made lowercase.
  main_naf = models.CharField(db_column='Main_NAF', max_length=4, blank=True) # Field name made lowercase.
  main_rs = models.CharField(db_column='Main_RS', max_length=100, blank=True) # Field name made lowercase.
  main_civ = models.CharField(db_column='Main_Civ', max_length=25, blank=True) # Field name made lowercase.
  main_titre = models.CharField(db_column='Main_Titre', max_length=50, blank=True) # Field name made lowercase.
  main_prenom = models.CharField(db_column='Main_Prenom', max_length=100, blank=True) # Field name made lowercase.
  main_nom = models.CharField(db_column='Main_Nom', max_length=50, blank=True) # Field name made lowercase.
  main_adr1 = models.CharField(db_column='Main_Adr1', max_length=100, blank=True) # Field name made lowercase.
  main_adr2 = models.CharField(db_column='Main_Adr2', max_length=100, blank=True) # Field name made lowercase.
  main_adr3 = models.CharField(db_column='Main_Adr3', max_length=100, blank=True) # Field name made lowercase.
  main_cp = models.CharField(db_column='Main_CP', max_length=5, blank=True) # Field name made lowercase.
  main_ville = models.CharField(db_column='Main_Ville', max_length=100, blank=True) # Field name made lowercase.
  main_fonction = models.CharField(db_column='Main_Fonction', max_length=50, blank=True) # Field name made lowercase.
  main_email = models.CharField(db_column='Main_Email', max_length=150, blank=True) # Field name made lowercase.
  main_dateappel = models.DateTimeField(db_column='Main_DateAppel', blank=True, null=True) # Field name made lowercase.
  main_heuredebut = models.CharField(db_column='Main_HeureDebut', max_length=10, blank=True) # Field name made lowercase.
  main_verbatim = models.TextField(db_column='Main_Verbatim', blank=True) # Field name made lowercase.
  main_nouvtel = models.CharField(db_column='Main_NouvTel', max_length=15, blank=True) # Field name made lowercase.
  main_nouvfax = models.CharField(db_column='Main_NouvFax', max_length=15, blank=True) # Field name made lowercase.
  main_nouvgsm = models.CharField(db_column='Main_NouvGSM', max_length=15, blank=True) # Field name made lowercase.
  main_nouvrs = models.CharField(db_column='Main_NouvRS', max_length=100, blank=True) # Field name made lowercase.
  main_nouvciv = models.CharField(db_column='Main_NouvCiv', max_length=5, blank=True) # Field name made lowercase.
  main_nouvtitre = models.CharField(db_column='Main_NouvTitre', max_length=50, blank=True) # Field name made lowercase.
  main_nouvprenom = models.CharField(db_column='Main_NouvPrenom', max_length=50, blank=True) # Field name made lowercase.
  main_nouvnom = models.CharField(db_column='Main_NouvNom', max_length=50, blank=True) # Field name made lowercase.
  main_nouvadr1 = models.CharField(db_column='Main_NouvAdr1', max_length=100, blank=True) # Field name made lowercase.
  main_nouvadr2 = models.CharField(db_column='Main_NouvAdr2', max_length=100, blank=True) # Field name made lowercase.
  main_nouvadr3 = models.CharField(db_column='Main_NouvAdr3', max_length=100, blank=True) # Field name made lowercase.
  main_nouvcp = models.CharField(db_column='Main_NouvCP', max_length=5, blank=True) # Field name made lowercase.
  main_nouvville = models.CharField(db_column='Main_NouvVille', max_length=50, blank=True) # Field name made lowercase.
  main_nouvfonction = models.CharField(db_column='Main_NouvFonction', max_length=50, blank=True) # Field name made lowercase.
  main_nouvemail = models.CharField(db_column='Main_NouvEmail', max_length=150, blank=True) # Field name made lowercase.
  main_called = models.CharField(db_column='Main_Called', max_length=1, blank=True) # Field name made lowercase.
  main_coderefus = models.CharField(db_column='Main_CodeRefus', max_length=100, blank=True) # Field name made lowercase.
  main_codefinappel = models.CharField(db_column='Main_CodeFinAppel', max_length=100, blank=True) # Field name made lowercase.
  main_locked = models.IntegerField(db_column='Main_Locked', blank=True, null=True) # Field name made lowercase.
  main_datefirstcall = models.DateTimeField(db_column='Main_DateFirstCall', blank=True, null=True) # Field name made lowercase.
  main_datelastcall = models.DateTimeField(db_column='Main_DateLastCall', blank=True, null=True) # Field name made lowercase.
  main_nbappels = models.IntegerField(db_column='Main_NBAppels', blank=True, null=True) # Field name made lowercase.
  main_postecdc = models.CharField(db_column='Main_PosteCDC', max_length=50, blank=True) # Field name made lowercase.
  main_nomcdc = models.CharField(db_column='Main_NomCDC', max_length=50, blank=True) # Field name made lowercase.
  main_prenomcdc = models.CharField(db_column='Main_PrenomCDC', max_length=50, blank=True) # Field name made lowercase.
  main_logincdc = models.CharField(db_column='Main_LoginCDC', max_length=50, blank=True) # Field name made lowercase.
  main_userid = models.CharField(db_column='Main_UserID', max_length=4, blank=True) # Field name made lowercase.
  main_extension = models.CharField(db_column='Main_Extension', max_length=4, blank=True) # Field name made lowercase.
  main_heurefin = models.CharField(db_column='Main_HeureFin', max_length=10, blank=True) # Field name made lowercase.

  # change CharField to IntegerField  and max_length to 
  main_tempscom = models.IntegerField(db_column='Main_TempsCom', max_length=20, blank=True) # Field name made lowercase.
  main_datenextrappel = models.DateTimeField(db_column='Main_DateNextRappel', blank=True, null=True) # Field name made lowercase.
  main_dateretour = models.DateTimeField(db_column='Main_DateRetour', blank=True, null=True) # Field name made lowercase.
  main_fichier = models.CharField(db_column='Main_Fichier', max_length=100, blank=True) # Field name made lowercase.
  main_yoon = models.TextField(db_column='Main_Yoon', blank=True) # Field name made lowercase.
  main_operation = models.CharField(db_column='Main_Operation', max_length=100, blank=True) # Field name made lowercase.
  main_typerappel = models.CharField(db_column='Main_TypeRappel', max_length=1, blank=True) # Field name made lowercase.
  main_nomprenomrappel = models.CharField(db_column='MAIN_NomPrenomRappel', max_length=100, blank=True) # Field name made lowercase.
  main_telrappel = models.CharField(db_column='MAIN_TelRappel', max_length=100, blank=True) # Field name made lowercase.
  main_verbatimrappel = models.TextField(db_column='MAIN_VerbatimRappel', blank=True) # Field name made lowercase.
  main_identifiant = models.CharField(db_column='Main_Identifiant', max_length=4, blank=True) # Field name made lowercase.
  main_q2nsp = models.CharField(db_column='Main_Q2NSP', max_length=25, blank=True) # Field name made lowercase.
  main_q4nsp = models.CharField(db_column='Main_Q4NSP', max_length=50, blank=True) # Field name made lowercase.
  main_q6nsp = models.CharField(db_column='Main_Q6NSP', max_length=50, blank=True) # Field name made lowercase.
  main_nomsociete = models.TextField(db_column='Main_NomSociete', blank=True) # Field name made lowercase.
  main_op_code = models.CharField(db_column='Main_Op_Code', max_length=50, blank=True) # Field name made lowercase.
  main_tempscom_reel = models.CharField(db_column='Main_tempscom_reel', max_length=50, blank=True) # Field name made lowercase.
  main_adr4 = models.CharField(db_column='MAIN_Adr4', max_length=50, blank=True) # Field name made lowercase.
  main_pays = models.CharField(db_column='Main_Pays', max_length=50, blank=True) # Field name made lowercase.
  main_q3introduction = models.CharField(db_column='Main_Q3Introduction', max_length=100, blank=True) # Field name made lowercase.
  main_q4avis = models.TextField(db_column='Main_Q4Avis', blank=True) # Field name made lowercase.
  main_q5presentationoffre = models.CharField(db_column='Main_Q5PresentationOffre', max_length=50, blank=True) # Field name made lowercase.
  main_q5promotion = models.CharField(db_column='Main_Q5Promotion', max_length=50, blank=True) # Field name made lowercase.
  main_q6promotionchoisie = models.CharField(db_column='Main_Q6PromotionChoisie', max_length=100, blank=True) # Field name made lowercase.
  main_q6daterv = models.CharField(db_column='Main_Q6DateRV', max_length=50, blank=True) # Field name made lowercase.
  main_q6heurerv = models.CharField(db_column='Main_Q6HeureRV', max_length=10, blank=True) # Field name made lowercase.
  main_q6bouquetabonnement = models.CharField(db_column='Main_Q6BouquetAbonnement', max_length=50, blank=True) # Field name made lowercase.
  main_q6dureeabonnement = models.CharField(db_column='Main_Q6DureeAbonnement', max_length=50, blank=True) # Field name made lowercase.
  main_q6option = models.CharField(db_column='Main_Q6Option', max_length=50, blank=True) # Field name made lowercase.
  main_bp = models.CharField(db_column='Main_BP', max_length=50, blank=True) # Field name made lowercase.
  main_nouvbp = models.CharField(db_column='Main_NouvBP', max_length=100, blank=True) # Field name made lowercase.
  main_numeroabonne = models.CharField(db_column='Main_NumeroAbonne', max_length=50, blank=True) # Field name made lowercase.
  main_numerocontrat = models.CharField(db_column='Main_NumeroContrat', max_length=50, blank=True) # Field name made lowercase.
  main_numerocarte = models.CharField(db_column='Main_NumeroCarte', max_length=50, blank=True) # Field name made lowercase.
  main_teldom = models.CharField(db_column='Main_TelDom', max_length=50, blank=True) # Field name made lowercase.
  main_telbur = models.CharField(db_column='Main_TelBur', max_length=50, blank=True) # Field name made lowercase.
  main_dateabonnement = models.CharField(db_column='Main_DateAbonnement', max_length=50, blank=True) # Field name made lowercase.
  main_datefinabonnement = models.CharField(db_column='Main_DateFinAbonnement', max_length=50, blank=True) # Field name made lowercase.
  main_scoudd = models.CharField(db_column='Main_SCouDD', max_length=100, blank=True) # Field name made lowercase.
  main_formule = models.CharField(db_column='Main_Formule', max_length=150, blank=True) # Field name made lowercase.
  main_duree = models.CharField(db_column='Main_Duree', max_length=100, blank=True) # Field name made lowercase.
  main_options = models.CharField(db_column='Main_Options', max_length=150, blank=True) # Field name made lowercase.
  main_coordonneesdistributeur = models.CharField(db_column='Main_CoordonneesDistributeur', max_length=100, blank=True) # Field name made lowercase.
  main_teldom1 = models.CharField(db_column='Main_TelDom1', max_length=25, blank=True) # Field name made lowercase.
  main_gsm2 = models.CharField(db_column='Main_GSM2', max_length=25, blank=True) # Field name made lowercase.
  main_debutabonnement = models.CharField(db_column='Main_DebutAbonnement', max_length=100, blank=True) # Field name made lowercase.
  main_q6gammeformule = models.CharField(db_column='Main_Q6GammeFormule', max_length=50, blank=True) # Field name made lowercase.
  main_q6motifdowngradeformule = models.TextField(db_column='Main_Q6MotifDowngradeFormule', blank=True) # Field name made lowercase.
  main_q6gammeduree = models.CharField(db_column='Main_Q6GammeDuree', max_length=50, blank=True) # Field name made lowercase.
  main_q6motifdowngradeduree = models.TextField(db_column='Main_Q6MotifDowngradeDuree', blank=True) # Field name made lowercase.
  main_f = models.CharField(db_column='Main_F', max_length=10, blank=True) # Field name made lowercase.
  main_telc = models.CharField(db_column='Main_TelC', max_length=25, blank=True) # Field name made lowercase.
  main_recg = models.CharField(db_column='Main_RecG', max_length=1, blank=True) # Field name made lowercase.
  main_distributeur = models.CharField(db_column='Main_Distributeur', max_length=200, blank=True) # Field name made lowercase.
  main_paiement = models.CharField(db_column='Main_Paiement', max_length=200, blank=True) # Field name made lowercase.
  main_formule1 = models.CharField(db_column='Main_Formule1', max_length=200, blank=True) # Field name made lowercase.
  main_mod = models.CharField(db_column='Main_Mod', max_length=1, blank=True) # Field name made lowercase.
  main_etat = models.CharField(db_column='Main_Etat', max_length=1, blank=True) # Field name made lowercase.
  main_q5presentationpromo = models.CharField(db_column='Main_Q5PresentationPromo', max_length=25, blank=True) # Field name made lowercase.
  main_cformu = models.CharField(db_column='Main_Cformu', max_length=50, blank=True) # Field name made lowercase.
  main_level = models.CharField(db_column='Main_Level', max_length=5, blank=True) # Field name made lowercase.
  main_tel4 = models.CharField(db_column='Main_Tel4', max_length=25, blank=True) # Field name made lowercase.
  main_tel5 = models.CharField(db_column='Main_Tel5', max_length=25, blank=True) # Field name made lowercase.
  main_q1introduction = models.CharField(db_column='Main_Q1Introduction', max_length=50, blank=True) # Field name made lowercase.
  main_q1distributeur = models.CharField(db_column='Main_Q1Distributeur', max_length=10, blank=True) # Field name made lowercase.
  main_q1verbatimdistributeur = models.TextField(db_column='Main_Q1VerbatimDistributeur', blank=True) # Field name made lowercase.
  main_q2etresatisfaitdecanal = models.CharField(db_column='Main_Q2EtreSatisfaitDeCanal', max_length=10, blank=True) # Field name made lowercase.
  main_q2verbatimetresatisfaitdecanal = models.TextField(db_column='Main_Q2VerbatimEtreSatisfaitDeCanal', blank=True) # Field name made lowercase.
  main_q3qualiteservicedistributeuragree = models.CharField(db_column='Main_Q3QualiteServiceDistributeurAgree', max_length=10, blank=True) # Field name made lowercase.
  main_q3formuleabonnement = models.CharField(db_column='Main_Q3FormuleAbonnement', max_length=10, blank=True) # Field name made lowercase.
  main_q3prestationinstallation = models.CharField(db_column='Main_Q3PrestationInstallation', max_length=10, blank=True) # Field name made lowercase.
  main_q3verbatimqualiteservicedistributeuragree = models.CharField(db_column='Main_Q3VerbatimQualiteServiceDistributeurAgree', max_length=200, blank=True) # Field name made lowercase.
  main_q3verbatimformuleabonnement = models.CharField(db_column='Main_Q3VerbatimFormuleAbonnement', max_length=200, blank=True) # Field name made lowercase.
  main_q3verbatimprestationinstallation = models.CharField(db_column='Main_Q3VerbatimPrestationInstallation', max_length=200, blank=True) # Field name made lowercase.
  main_q5programmefidelitecanal = models.CharField(db_column='Main_Q5ProgrammeFideliteCanal', max_length=10, blank=True) # Field name made lowercase.
  main_q7nsp = models.CharField(db_column='Main_Q7NSP', max_length=50, blank=True) # Field name made lowercase.
  main_teldistributeur = models.CharField(db_column='Main_TelDistributeur', max_length=25, blank=True) # Field name made lowercase.
  main_r = models.CharField(db_column='Main_R', max_length=1, blank=True) # Field name made lowercase.
  main_cactiv = models.CharField(db_column='Main_CACTIV', max_length=2, blank=True) # Field name made lowercase.
  main_teladr = models.CharField(db_column='Main_TELADR', max_length=15, blank=True) # Field name made lowercase.
  main_gsm1 = models.CharField(db_column='Main_GSM1', max_length=15, blank=True) # Field name made lowercase.
  main_typerelance = models.CharField(db_column='Main_TypeRelance', max_length=50, blank=True) # Field name made lowercase.
  main_moisrelance = models.CharField(db_column='Main_MoisRelance', max_length=50, blank=True) # Field name made lowercase.
  main_montantfacture = models.CharField(db_column='Main_MontantFacture', max_length=50, blank=True) # Field name made lowercase.
  main_ip = models.CharField(db_column='Main_IP', max_length=5, blank=True) # Field name made lowercase.
  main_account_status = models.CharField(db_column='Main_ACCOUNT_STATUS', max_length=10, blank=True) # Field name made lowercase.
  main_balance = models.CharField(db_column='Main_BALANCE', max_length=10, blank=True) # Field name made lowercase.
  main_accounttype = models.CharField(db_column='Main_ACCOUNTTYPE', max_length=50, blank=True) # Field name made lowercase.
  main_decoder = models.CharField(db_column='Main_DECODER', max_length=10, blank=True) # Field name made lowercase.
  main_dec_model = models.CharField(db_column='Main_DEC_MODEL', max_length=10, blank=True) # Field name made lowercase.
  main_lastevent = models.CharField(db_column='Main_LastEvent', max_length=50, blank=True) # Field name made lowercase.
  main_appeleautretel = models.CharField(db_column='Main_AppeleAutreTel', max_length=1, blank=True) # Field name made lowercase.
  main_autretelappele = models.CharField(db_column='Main_AutreTelAppele', max_length=50, blank=True) # Field name made lowercase.
  main_q3sataisfaitprogramme = models.CharField(db_column='Main_Q3SataisfaitProgramme', max_length=5, blank=True) # Field name made lowercase.
  main_q3modereabonnement = models.TextField(db_column='Main_Q3ModeReabonnement', blank=True) # Field name made lowercase.
  main_q3nsp = models.CharField(db_column='Main_Q3NSP', max_length=10, blank=True) # Field name made lowercase.
  main_q3sataisfaitdistributeur = models.CharField(db_column='Main_Q3SataisfaitDistributeur', max_length=5, blank=True) # Field name made lowercase.
  main_q3solutionpourregardertele = models.TextField(db_column='Main_Q3SolutionPourRegarderTele', blank=True) # Field name made lowercase.
  main_q31nsp = models.CharField(db_column='Main_Q31NSP', max_length=10, blank=True) # Field name made lowercase.
  main_q32nsp = models.CharField(db_column='Main_Q32NSP', max_length=10, blank=True) # Field name made lowercase.
  main_q3contactercanal = models.CharField(db_column='Main_Q3ContacterCanal', max_length=5, blank=True) # Field name made lowercase.
  main_q3biaisdecontact = models.CharField(db_column='Main_Q3BiaisdeContact', max_length=200, blank=True) # Field name made lowercase.
  main_q3solutioncanal = models.TextField(db_column='Main_Q3SolutionCanal', blank=True) # Field name made lowercase.
  main_q33nsp = models.CharField(db_column='Main_Q33NSP', max_length=10, blank=True) # Field name made lowercase.
  main_q3pensersituation = models.TextField(db_column='Main_Q3PenserSituation', blank=True) # Field name made lowercase.
  main_promo = models.CharField(db_column='Main_Promo', max_length=100, blank=True) # Field name made lowercase.
  main_distributor = models.CharField(db_column='Main_Distributor', max_length=100, blank=True) # Field name made lowercase.
  main_traite1 = models.CharField(db_column='Main_Traite1', max_length=5, blank=True) # Field name made lowercase.
  main_traite2 = models.CharField(db_column='Main_Traite2', max_length=5, blank=True) # Field name made lowercase.
  main_traite3 = models.CharField(db_column='Main_Traite3', max_length=5, blank=True) # Field name made lowercase.
  main_traite4 = models.CharField(db_column='Main_Traite4', max_length=5, blank=True) # Field name made lowercase.
  main_traite5 = models.CharField(db_column='Main_Traite5', max_length=5, blank=True) # Field name made lowercase.
  main_q6modepaiement = models.CharField(db_column='Main_Q6ModePaiement', max_length=100, blank=True) # Field name made lowercase.
  main_daterv = models.CharField(db_column='Main_DateRV', max_length=50, blank=True) # Field name made lowercase.
  main_heurerv = models.CharField(db_column='Main_HeureRV', max_length=50, blank=True) # Field name made lowercase.
  main_dureecall1 = models.CharField(db_column='Main_DureeCall1', max_length=50, blank=True) # Field name made lowercase.
  main_formulecall1 = models.CharField(db_column='Main_FormuleCall1', max_length=100, blank=True) # Field name made lowercase.
  main_datecall1 = models.CharField(db_column='Main_DateCall1', max_length=10, blank=True) # Field name made lowercase.
  main_q2daterv = models.CharField(db_column='Main_Q2DateRV', max_length=50, blank=True) # Field name made lowercase.
  main_q2heurerv = models.CharField(db_column='Main_Q2HeureRV', max_length=50, blank=True) # Field name made lowercase.
  main_q2accordrv = models.CharField(db_column='Main_Q2AccordRV', max_length=50, blank=True) # Field name made lowercase.
  main_q4avis1 = models.TextField(db_column='Main_Q4Avis1', blank=True) # Field name made lowercase.
  main_q4nsp1 = models.CharField(db_column='Main_Q4NSP1', max_length=50, blank=True) # Field name made lowercase.
  main_invisible = models.CharField(max_length=1, blank=True)
  main_q5payerdecodeur = models.CharField(db_column='Main_Q5PayerDecodeur', max_length=10, blank=True) # Field name made lowercase.
  main_q5bispayercombien = models.CharField(db_column='Main_Q5BisPayerCombien', max_length=100, blank=True) # Field name made lowercase.
  main_q6installermateriel = models.CharField(db_column='Main_Q6InstallerMateriel', max_length=5, blank=True) # Field name made lowercase.
  main_q6bisbeneficierparabole = models.CharField(db_column='Main_Q6BisBeneficierParabole', max_length=5, blank=True) # Field name made lowercase.
  main_q7indiquerdecodeur = models.CharField(db_column='Main_Q7IndiquerDecodeur', max_length=5, blank=True) # Field name made lowercase.
  main_q8accederimage = models.CharField(db_column='Main_Q8AccederImage', max_length=200, blank=True) # Field name made lowercase.
  main_q5bispayerparabole = models.CharField(db_column='Main_Q5BisPayerParabole', max_length=5, blank=True) # Field name made lowercase.
  main_traiterepondeur = models.CharField(db_column='Main_TraiteRepondeur', max_length=5, blank=True) # Field name made lowercase.
  main_optqcartegold = models.CharField(db_column='Main_OptQCarteGold', max_length=5, blank=True) # Field name made lowercase.
  main_optq1partenaire = models.CharField(db_column='Main_OptQ1Partenaire', max_length=5, blank=True) # Field name made lowercase.
  main_q3partenaire = models.CharField(db_column='Main_Q3Partenaire', max_length=5, blank=True) # Field name made lowercase.
  main_txtq4partenaire = models.CharField(db_column='Main_TxtQ4Partenaire', max_length=100, blank=True) # Field name made lowercase.
  main_optq4partenaire = models.CharField(db_column='Main_OptQ4Partenaire', max_length=5, blank=True) # Field name made lowercase.
  main_optq1magazine = models.CharField(db_column='Main_OptQ1Magazine', max_length=100, blank=True) # Field name made lowercase.
  main_optq2magazine = models.CharField(db_column='Main_OptQ2Magazine', max_length=5, blank=True) # Field name made lowercase.
  main_optq3magazine = models.CharField(db_column='Main_OptQ3Magazine', max_length=5, blank=True) # Field name made lowercase.
  main_txtq3magazine = models.CharField(db_column='Main_TxtQ3Magazine', max_length=100, blank=True) # Field name made lowercase.
  main_optq2partenaire = models.CharField(db_column='Main_OptQ2Partenaire', max_length=5, blank=True) # Field name made lowercase.
  main_optq3partenaire = models.CharField(db_column='Main_OptQ3Partenaire', max_length=5, blank=True) # Field name made lowercase.
  main_nouvgms2 = models.CharField(db_column='Main_NouvGMS2', max_length=100, blank=True) # Field name made lowercase.
  main_nouvtelbureau = models.CharField(db_column='Main_NouvTelBureau', max_length=15, blank=True) # Field name made lowercase.
  main_called_old = models.CharField(db_column='Main_Called_Old', max_length=1, blank=True) # Field name made lowercase.
  main_datechargment = models.CharField(db_column='MAin_DateChargment', max_length=10, blank=True) # Field name made lowercase.
  agesenfants = models.CharField(db_column='AgesEnfants', max_length=50, blank=True) # Field name made lowercase.
  nombreenfants = models.CharField(db_column='NombreEnfants', max_length=10, blank=True) # Field name made lowercase.
  main_stockvaleur = models.TextField(db_column='Main_StockValeur', blank=True) # Field name made lowercase.
  main_fichierclient = models.CharField(db_column='Main_FichierClient', max_length=150, blank=True) # Field name made lowercase.
  main_categorieprof = models.CharField(db_column='Main_CategorieProf', max_length=100, blank=True) # Field name made lowercase.
  main_cbtelc1 = models.CharField(db_column='Main_CBTelC1', max_length=50, blank=True) # Field name made lowercase.
  main_cbtelc2 = models.CharField(db_column='Main_CBTelC2', max_length=50, blank=True) # Field name made lowercase.
  main_cbtelc3 = models.CharField(db_column='Main_CBTelC3', max_length=50, blank=True) # Field name made lowercase.
  main_q6promotionchoisie1 = models.CharField(db_column='Main_Q6PromotionChoisie1', max_length=100, blank=True) # Field name made lowercase.
  main_queue = models.CharField(db_column='Main_Queue', max_length=50, blank=True) # Field name made lowercase.
  main_uniqueid = models.CharField(db_column='Main_UniqueID', max_length=50, blank=True) # Field name made lowercase.
  main_dateflag = models.DateTimeField(db_column='Main_DateFlag', blank=True, null=True) # Field name made lowercase.
  main_nbrappels = models.IntegerField(db_column='Main_NBRappels', blank=True, null=True) # Field name made lowercase.
  main_autretel = models.CharField(db_column='Main_AutreTel', max_length=50, blank=True) # Field name made lowercase.
  main_depersonnaliser = models.CharField(db_column='Main_Depersonnaliser', max_length=2, blank=True) # Field name made lowercase.
  main_flag = models.DateTimeField(blank=True, null=True)
  main_satisfaction = models.CharField(db_column='main_Satisfaction', max_length=50, blank=True) # Field name made lowercase.
  main_reabo = models.CharField(db_column='main_Reabo', max_length=50, blank=True) # Field name made lowercase.
  main_pointvente1 = models.CharField(db_column='main_PointVente1', max_length=50, blank=True) # Field name made lowercase.
  main_pointvente2 = models.CharField(db_column='main_PointVente2', max_length=50, blank=True) # Field name made lowercase.
  main_pointvente3 = models.CharField(db_column='main_PointVente3', max_length=50, blank=True) # Field name made lowercase.
  main_paiementmobile1 = models.CharField(db_column='main_PaiementMobile1', max_length=50, blank=True) # Field name made lowercase.
  main_paiementmobile2 = models.CharField(db_column='main_PaiementMobile2', max_length=50, blank=True) # Field name made lowercase.
  main_paiementmobile3 = models.CharField(db_column='main_PaiementMobile3', max_length=50, blank=True) # Field name made lowercase.
  main_paiementmobile4 = models.CharField(db_column='main_PaiementMobile4', max_length=50, blank=True) # Field name made lowercase.
  main_paiementmobile5 = models.CharField(db_column='main_PaiementMobile5', max_length=50, blank=True) # Field name made lowercase.
  main_tiercepersonne1 = models.CharField(db_column='main_TiercePersonne1', max_length=50, blank=True) # Field name made lowercase.
  main_tiercepersonne2 = models.CharField(db_column='main_TiercePersonne2', max_length=50, blank=True) # Field name made lowercase.
  main_tiercepersonne3 = models.CharField(db_column='main_TiercePersonne3', max_length=50, blank=True) # Field name made lowercase.
  main_telnumcomplement = models.CharField(db_column='main_TelNumComplement', max_length=50, blank=True) # Field name made lowercase.

  
  def on_timeout(self):
    if self.main_tempscom and int(self.main_tempscom)>480:
        return True
    return False
      
  def timeout_count(self):
    return Main.objects.filter(main_userid =self.main_userid).filter(
        main_tempscom__gt =480, main_dateappel__gt =date.today()).count()


 
  class Meta:
    managed = False
    db_table = 'main_dev'
        
class Statistiques(models.Model):
  stat_id = models.BigIntegerField(db_column='STAT_id', blank=True, null=True) # Field name made lowercase.
  stat_tel = models.CharField(db_column='STAT_Tel', max_length=50, blank=True) # Field name made lowercase.
  stat_dateappel = models.DateTimeField(db_column='STAT_DateAppel', blank=True, null=True) # Field name made lowercase.
  stat_codefinappel = models.CharField(db_column='STAT_CodeFinAppel', max_length=100, blank=True) # Field name made lowercase.
  stat_coderefus = models.CharField(db_column='STAT_CodeRefus', max_length=200, blank=True) # Field name made lowercase.
  stat_modedenvoi = models.TextField(db_column='STAT_ModeDenvoi', blank=True) # Field name made lowercase.
  stat_userid = models.CharField(db_column='STAT_UserId', max_length=4, blank=True) # Field name made lowercase.
  stat_logincdc = models.CharField(db_column='STAT_LoginCDC', max_length=50, blank=True) # Field name made lowercase.
  stat_nbappels = models.IntegerField(db_column='STAT_NbAppels', blank=True, null=True) # Field name made lowercase.
  stat_tempscom = models.CharField(db_column='STAT_TempsCom', max_length=50, blank=True) # Field name made lowercase.
  stat_fichier = models.CharField(db_column='STAT_Fichier', max_length=100, blank=True) # Field name made lowercase.
  stat_operation = models.CharField(db_column='Stat_Operation', max_length=100, blank=True) # Field name made lowercase.
  stat_identifiant = models.CharField(db_column='Stat_Identifiant', max_length=10, blank=True) # Field name made lowercase.
  stat_op_code = models.CharField(db_column='Stat_Op_Code', max_length=50, blank=True) # Field name made lowercase.
  stat_tempscom_reel = models.CharField(db_column='STAT_TempsCom_Reel', max_length=50, blank=True) # Field name made lowercase.
  stat_queue = models.CharField(db_column='Stat_Queue', max_length=50, blank=True) # Field name made lowercase.
  class Meta:
      managed = False
      db_table = 'statistiques_dev'

class StatistiquesAppeles(models.Model):
  stat_id = models.BigIntegerField(db_column='STAT_id', blank=True, null=True) # Field name made lowercase.
  stat_tel = models.CharField(db_column='STAT_Tel', max_length=50, blank=True) # Field name made lowercase.
  stat_dateappel = models.DateTimeField(db_column='STAT_DateAppel', blank=True, null=True) # Field name made lowercase.
  stat_codefinappel = models.CharField(db_column='STAT_CodeFinAppel', max_length=100, blank=True) # Field name made lowercase.
  stat_coderefus = models.CharField(db_column='STAT_CodeRefus', max_length=200, blank=True) # Field name made lowercase.
  stat_modedenvoi = models.TextField(db_column='STAT_ModeDenvoi', blank=True) # Field name made lowercase.
  stat_userid = models.CharField(db_column='STAT_UserId', max_length=4, blank=True) # Field name made lowercase.
  stat_logincdc = models.CharField(db_column='STAT_LoginCDC', max_length=50, blank=True) # Field name made lowercase.
  stat_nbappels = models.IntegerField(db_column='STAT_NbAppels', blank=True, null=True) # Field name made lowercase.
  stat_tempscom = models.CharField(db_column='STAT_TempsCom', max_length=50, blank=True) # Field name made lowercase.
  stat_fichier = models.CharField(db_column='STAT_Fichier', max_length=100, blank=True) # Field name made lowercase.
  stat_operation = models.CharField(db_column='Stat_Operation', max_length=100, blank=True) # Field name made lowercase.
  stat_identifiant = models.CharField(db_column='Stat_Identifiant', max_length=10, blank=True) # Field name made lowercase.
  stat_op_code = models.CharField(db_column='Stat_Op_Code', max_length=50, blank=True) # Field name made lowercase.
  stat_tempscom_reel = models.CharField(db_column='STAT_TempsCom_Reel', max_length=50, blank=True) # Field name made lowercase.
  stat_queue = models.CharField(db_column='Stat_Queue', max_length=50, blank=True) # Field name made lowercase.
  class Meta:
      managed = False
      db_table = 'statistiques_appeles_dev'
