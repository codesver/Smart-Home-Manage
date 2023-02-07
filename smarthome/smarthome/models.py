from django.db import models

# Create your models here.
class Home(models.Model) :
    hsn = models.CharField(max_length = 20, primary_key = True)
    aptn = models.IntegerField()
    floor = models.IntegerField()
    lrv = models.CharField(max_length = 20)

class Resident(models.Model) :
    rsn = models.CharField(max_length = 20, primary_key = True)
    hsn = models.ForeignKey('Home', on_delete = models.CASCADE, db_column = 'hsn', null = True)
    rname = models.CharField(max_length = 20)
    age = models.IntegerField()
    pw = models.CharField(max_length = 20, default = '000000')
    authority = models.BooleanField(default = False)

class Space(models.Model) :
    ssn = models.CharField(max_length = 20, primary_key = True)
    hsn = models.ForeignKey('Home', on_delete = models.CASCADE, db_column = 'hsn', null = True) 
    skind = models.CharField(max_length = 20)
    sno = models.CharField(max_length = 20, null = True)

class Power(models.Model) :
    psn = models.CharField(max_length = 20, primary_key = True)
    ssn = models.ForeignKey('Space', on_delete = models.CASCADE, db_column = 'ssn', null = True)  
    pkind = models.CharField(max_length = 20)
    pno = models.IntegerField(null = True)
    pstate = models.BooleanField(default = False)

class IOT(models.Model) :
    isn = models.CharField(max_length = 20, primary_key = True)
    ssn = models.ForeignKey('Space', on_delete = models.CASCADE, db_column = 'ssn', null = True) 
    ikind = models.CharField(max_length = 20)
    ino = models.IntegerField(null = True)
    istate = models.BooleanField(default = False)


    