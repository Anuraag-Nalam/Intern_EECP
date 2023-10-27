from django.db import models
import datetime
# Create your models here.
class Newpatient(models.Model):
    yourid=models.AutoField(primary_key=True)
    name= models.CharField(max_length=122)
    age=models.CharField(max_length=3)
    phone=models.CharField(max_length=12)
    gender=models.CharField(max_length=20)
    height=models.CharField(max_length=4)
    weight=models.CharField(max_length=3)
    diagnosis=models.CharField(max_length=1220)
    address=models.CharField(max_length=12222)
    heartproblem = models.CharField(max_length=100, default="",null=True)
    medication = models.CharField(max_length=100, default="",null=True)
    hospitalization = models.CharField(max_length=100, default="",null=True)
    surgery = models.CharField(max_length=100, default="",null=True)
    allergic = models.CharField(max_length=100, default="",null=True)
    hypertension = models.CharField(max_length=100, default="",null=True)
    diabetes = models.CharField(max_length=100, default="",null=True)
    thyroid = models.CharField(max_length=100, default="",null=True)
    anginapectoris = models.CharField(max_length=100, default="",null=True)
    congesticcardiacfailure = models.CharField(max_length=100, default="",null=True)
    everyday = models.CharField(max_length=100, default="",null=True)
    threetosixdays = models.CharField(max_length=100, default="",null=True)
    onetotwodays = models.CharField(max_length=100, default="",null=True)
    never = models.CharField(max_length=100, default="",null=True)
    everyday1 = models.CharField(max_length=100, default="",null=True)
    threetosixdays1 = models.CharField(max_length=100, default="",null=True)
    onetotwodays1 = models.CharField(max_length=100, default="",null=True)
    never1 = models.CharField(max_length=100, default="",null=True)
    everyday2 = models.CharField(max_length=100, default="",null=True)
    threetosixdays2 = models.CharField(max_length=100, default="",null=True)
    onetotwodays2 = models.CharField(max_length=100, default="",null=True)
    never2 = models.CharField(max_length=100, default="",null=True)
    daily = models.CharField(max_length=100, default="",null=True)
    twotothreetimes = models.CharField(max_length=100, default="",null=True)
    once = models.CharField(max_length=100, default="",null=True)
    never3 = models.CharField(max_length=100, default="",null=True)
    tobacco = models.CharField(max_length=100, default="",null=True)
    almosteveryday = models.CharField(max_length=100, default="",null=True)
    sometimes = models.CharField(max_length=100, default="",null=True)
    rarely = models.CharField(max_length=100, default="",null=True)
    never4 = models.CharField(max_length=100, default="",null=True)




    date=models.DateField()
    def __str__(self):
        return self.name
class Existpatient(models.Model):
    patientid=models.CharField(max_length=10,default="")
    bpsys=models.CharField(max_length=22)
    bpdia = models.CharField(max_length=22)
    visceralfatlevel = models.CharField(max_length=122)
    restingmetabolism = models.CharField(max_length=122)
    bmi = models.CharField(max_length=122)
    bfp = models.CharField(max_length=122)
    bodytemperature = models.CharField(max_length=122)
    glucoselevel=models.CharField(max_length=10,default="")
    skeletalmusclepercentage = models.CharField(max_length=122)
    footbottom = models.ImageField(upload_to='home/images',default="")
    foottop=models.ImageField(upload_to='home/images',default="")
    legs=models.ImageField(upload_to='home/images',default="")
    handsfront=models.ImageField(upload_to='home/images',default="")
    handsback=models.ImageField(upload_to='home/images',default="")
    lefteye=models.ImageField(upload_to='home/images',default="")
    righteye=models.ImageField(upload_to='home/images',default="")
    pulse=models.CharField(max_length=122)
    weight=models.CharField(max_length=122)
    roomhumidity=models.CharField(max_length=122)
    roomtemperature=models.CharField(max_length=122)


    def __str__(self):
         return self.patientid
class AfterPatient(models.Model):
    patientid=models.CharField(max_length=10,default="")
    bpsys=models.CharField(max_length=22)
    bpdia = models.CharField(max_length=22)
    visceralfatlevel = models.CharField(max_length=122)
    restingmetabolism = models.CharField(max_length=122)
    bmi = models.CharField(max_length=122)
    bfp = models.CharField(max_length=122)
    bodytemperature = models.CharField(max_length=122)
    skeletalmusclepercentage = models.CharField(max_length=122)
    footbottom = models.ImageField(upload_to='home/images',default="")
    foottop=models.ImageField(upload_to='home/images',default="")
    legs=models.ImageField(upload_to='home/images',default="")
    handsfront=models.ImageField(upload_to='home/images',default="")
    handsback=models.ImageField(upload_to='home/images',default="")
    lefteye=models.ImageField(upload_to='home/images',default="")
    righteye=models.ImageField(upload_to='home/images',default="")
    pulse=models.CharField(max_length=122)
    weight=models.CharField(max_length=122)
    roomhumidity=models.CharField(max_length=122)
    roomtemperature=models.CharField(max_length=122)


    def __str__(self):
         return self.patientid

class Live(models.Model):
    machineid=models.CharField(max_length=10,default="")
    patientid=models.CharField(max_length=10,default="")
    averageecg=models.CharField(max_length=10,default="")
    averageso=models.CharField(max_length=22)
    averagepeakratio = models.CharField(max_length=22)
    averagearearatio = models.CharField(max_length=122)
    pressure = models.CharField(max_length=122)
    def __str__(self):
        return self.patientid