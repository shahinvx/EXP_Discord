from django.db import models

# Create your models here.
class NLP_Models(models.Model):
    NLP_Model = models.CharField(max_length=100, unique=True, null=True, default='Non ML')

    class Meta:
        managed = True
        db_table = 'NLP_Models'


    def __str__(self):
        return self.NLP_Model


class Discord_Apps_List(models.Model):
    App_name = models.CharField(max_length=50, unique=True)
    App_Token = models.CharField(max_length=300, blank=False, unique=True)
    App_ID = models.CharField(max_length=300, blank=False, unique=True)
    App_Pub_Key = models.CharField(max_length=300, blank=False, unique=True)
    App_Invitation_Link = models.CharField(max_length=300, blank=False, unique=True)
    descript = models.CharField(max_length=100, blank=True, null=True, default='nothing')
    #NLP_Model = models.CharField(max_length=100, blank=True, null=True, default='Non ML')
    #NLP_Model = models.ManyToManyField(NLP_Models)
    NLP_Model = models.OneToOneField(NLP_Models, null=True, on_delete=models.DO_NOTHING, default='No Model')

    def __str__(self):
        return self.App_name

    class Meta:
        managed = True
        db_table = 'Discord_Apps_List'

