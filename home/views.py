from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
from .models import Newpatient,Existpatient,AfterPatient,Live
from django.contrib import messages
import os
import time
import csv

from django.utils.datastructures import MultiValueDictKeyError

from django.conf import settings
from django.conf.urls.static import static
from django.core.files.storage import FileSystemStorage

path_location = r"C:\Users\Anuraag\Desktop\eecpdata"
# Create your views here.
def live(request):
    if request.method=="POST":
        date=request.POST.get("date")
        machineid=request.POST.get("machineid")
        patientid=request.POST.get("patientid")
        averageecg=request.POST.get("averageecg")
        averageso=request.POST.get("averageso")
        averagepeakratio=request.POST.get("averagepeakratio")
        averagearearatio=request.POST.get("averagearearatio")
        pressure=request.POST.get("pressure")
       
        live= Live(machineid=machineid,patientid=patientid,averageecg=averageecg,averageso=averageso,averagepeakratio=averagepeakratio,
            averagearearatio=averagearearatio,pressure=pressure
                               )

        parent_dir = path_location
        identered = live.patientid
        date1 = date.split("-")
        date1.reverse()
        date1="_".join(date1)
        timestr=date1
        #timestr = time.strftime("%d_%m_%Y")
        # path = path_location + "\\" + identered + "\\" + timestr
        # dict2 = request.POST
        # with open(path + r"\Live_details.csv", 'a') as csvfile:
        #     wrt = csv.writer(csvfile)
        #     for key, value in dict2.items():
        #         wrt.writerow([key, value])
        try:

            path= path_location+"\\"+identered+"\\"+timestr
            os.mkdir(path)
            print("came to try")
            print(path)
            dict2=request.POST
            with open(path + r"\Live_details.csv", 'a') as csvfile:
                wrt = csv.writer(csvfile)
                for key, value in dict2.items():

                    wrt.writerow([key, value])
        except OSError as error:

            path= path_location+"\\"+identered+"\\"+timestr
            dict2 = request.POST
            print("came to except")
            print(path)
            with open(path + r"\Live_details.csv", 'a') as csvfile:
                wrt = csv.writer(csvfile)
                for key, value in dict2.items():

                    wrt.writerow([key, value])
        live.save()

    return render(request,'live.html')
def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')
def newp(request):
    if request.method=="POST":
        name=request.POST.get("name")
        print(type(name))
        date=request.POST.get('date')
        # os.mkdir(os.path.join(os.getcwd(),name))
        age=request.POST.get("age")
        phone=request.POST.get("phone")
        gender=request.POST.get("gender")
        height=request.POST.get("height")
        weight = request.POST.get("weight")
        diagnosis = request.POST.get("diagnosis")
        address = request.POST.get("address")
        heartproblem = request.POST.get("heartproblem")
        medication = request.POST.get("medication")
        hospitalization = request.POST.get("hospitalization")
        surgery = request.POST.get("surgery")
        allergic = request.POST.get("allergic")
        hypertension = request.POST.get("hypertension")
        diabetes = request.POST.get("diabetes")
        thyroid = request.POST.get("thyroid")
        anginapectoris = request.POST.get("anginapectoris")
        congesticcardiacfailure = request.POST.get("congesticcardiacfailure")
        everyday = request.POST.get("everyday")
        threetosixdays = request.POST.get("threetosixdays")
        onetotwodays = request.POST.get("onetotwodays")
        never = request.POST.get("never")
        everyday1 = request.POST.get("everyday1")
        threetosixdays1 = request.POST.get("threetosixdays1")
        onetotwodays1 = request.POST.get("onetotwodays1")
        never1 = request.POST.get("never1")
        everyday2 = request.POST.get("everyday2")
        threetosixdays2 = request.POST.get("threetosixdays2")
        onetotwodays2 = request.POST.get("onetotwodays2")
        never2 = request.POST.get("never2")
        daily = request.POST.get("daily")
        twotothreetimes = request.POST.get("twotothreetimes")
        once = request.POST.get("once")
        never3 = request.POST.get("never3")
        tobacco = request.POST.get("tobacco")
        almosteveryday = request.POST.get("almosteveryday")
        sometimes = request.POST.get("sometimes")
        rarely = request.POST.get("rarely")
        never4 = request.POST.get("never4")
        
        # medicalhistory = request.POST.get("medicalhistory")

        newpatient= Newpatient(name=name,age=age,phone=phone,gender=gender,height=height,
                               weight=weight,diagnosis=diagnosis,address=address,heartproblem=heartproblem,medication=medication,
                               hospitalization=hospitalization,surgery=surgery,allergic=allergic,hypertension=hypertension,diabetes=diabetes,
                               thyroid=thyroid,anginapectoris=anginapectoris,congesticcardiacfailure=congesticcardiacfailure,everyday=everyday,
                               threetosixdays=threetosixdays,onetotwodays=onetotwodays,never=never,everyday1=everyday1,threetosixdays1=threetosixdays1,
                               onetotwodays1=onetotwodays1,never1=never1,everyday2=everyday2,threetosixdays2=threetosixdays2,onetotwodays2=onetotwodays2,
                               never2=never2,daily=daily,twotothreetimes=twotothreetimes,once=once,never3=never3,tobacco=tobacco,
                               almosteveryday=almosteveryday,sometimes=sometimes,rarely=rarely,never4=never4,date= datetime.today()
                               )

        
        newpatient.save()
        # os.mkdir(os.path.join(os.getcwd(), id))
        thank=True
        id=newpatient.yourid
        # CHANGED OVER HERE
        id="LIVO"+str(id)
        directory=id
        parent_dir = path_location
        path = os.path.join(parent_dir, directory)
        parentdir1=path
        print(parentdir1)
        # print(type(parentdir1))
        #timestr = time.strftime("%d_%m_%Y")
        date1 = date.split("-")
        print(date1)
        date1.reverse()
        date1="_".join(date1)
        print(date1)
        timestr=date1
        #print(timestr)
        dir = timestr
        # id = newpatient.yourid
        # directory = id
        try:
            os.makedirs(path, exist_ok=True)
            print("Directory '%s' created successfully" % directory)
        except OSError as error:

            print("Directory '%s' can not be created" % directory)

        # directory of the patient id and date is parentdir2
        parentdir = parentdir1
        pathh = os.path.join(parentdir, dir)
        print(pathh)
        parentdir2=pathh

        try:
            print("Directory '%s' created successfully" % dir)
            os.makedirs(pathh, exist_ok=True)

        except OSError as error:
            print("Directory can not be created")
            print(error)
        dict1 = request.POST
        # with open(r"C:\Users\Anuraag\Desktop\password\oo.csv", 'a') as csvfile:
        with open(parentdir2 + directory+" Registration_details.csv", 'a') as csvfile:
            print(parentdir2)
            print(directory)
            wrt = csv.writer(csvfile)
            for key, value in dict1.items():
                wrt.writerow([key, value])
        messages.success(request, 'Your Details Are Saved')
        return render(request,'newpatient.html', {'thank':thank,'id': id})
    return render(request,'newpatient.html')


def exip(request):
    if request.method=="POST":

        search=request.POST.get('search')
        # search[:3]=="LIVO"
        # listit1[0]['yourid']="LIVO"+str(listit1[0]['yourid'])
        # print(listit1[0]['yourid'])
        # print("LIVO"+str(listit1[0]['yourid']))
        # listit1 = "LIVO" + str(listit1[0]['yourid'])
        print(search[0:4])
        if(search[:4]=="LIVO"):
            
            # listit1 = Newpatient.objects.filter(yourid=search[4:]).values()
            # listit = listit1[0]
            # print(listit)
            # print("came")

            try:
                listit1 = Newpatient.objects.filter(yourid=search[4:]).values()
                listit = listit1[0]
                print(listit)
                print("came")
            except IndexError:

                random={"OK":"okay"}
                return render(request,'exip.html',random)
            return render(request,'exip.html',listit)
        else:
            print("else statement")
            random={"OK":"okay"}
            return render(request,'exip.html',random)
    # values of listit with yourid=2
    # [{'yourid': 2, 'name': 'h', 'age': '6', 'phone': '6', 'gender': 'M', 'height': '6', 'weight': '6', 'diagnosis': '6',
    #   'address': '6', 'medicalhistory': '6', 'date': datetime.date
    #     (2020, 8, 27)}] >

    return render(request,'exip.html')

def exipu(request):
    if request.method=="POST":
        date=request.POST.get("date")
        patientid=request.POST.get('patientid')
        bpsys=request.POST.get('bpsys')
        bpdia = request.POST.get('bpdia')
        visceralfatlevel = request.POST.get('visceralfatlevel')
        restingmetabolism = request.POST.get('restingmetabolism')
        bmi = request.POST.get('bmi')
        bfp = request.POST.get('bfp')
        bodytemperature = request.POST.get('bodytemperature')
        glucoselevel=request.POST.get('glucoselevel')
        skeletalmusclepercentage = request.POST.get('skeletalmusclepercentage')
        try:
            footbottom = request.FILES['footbottom']
            fs = FileSystemStorage()
            fs.save(footbottom.name, footbottom)
        except MultiValueDictKeyError:
            footbottom = request.POST.get('footbottom')

        try:
            foottop = request.FILES['foottop']
            fs1 = FileSystemStorage()
            fs1.save(foottop.name, foottop)
        except MultiValueDictKeyError:
            foottop = request.POST.get('foottop')
        try:
            legs = request.FILES['legs']
            fs2 = FileSystemStorage()
            fs2.save(legs.name, legs)
        except MultiValueDictKeyError:
            legs = request.POST.get('legs')

        try:
            handsfront = request.FILES['handsfront']
            fs3 = FileSystemStorage()
            fs3.save(handsfront.name, handsfront)
        except MultiValueDictKeyError:
            handsfront = request.POST.get('handsfront')

        try:
            handsback = request.FILES['handsback']
            fs4 = FileSystemStorage()
            fs4.save(handsback.name, handsback)
        except MultiValueDictKeyError:
            handsback = request.POST.get('handsback')

        try:
            lefteye = request.FILES['lefteye']
            fs5 = FileSystemStorage()
            fs5.save(lefteye.name, lefteye)
        except MultiValueDictKeyError:
            lefteye = request.POST.get('lefteye')


        try:
            righteye = request.FILES['righteye']
            fs6 = FileSystemStorage()
            fs6.save(righteye.name, righteye)
        except MultiValueDictKeyError:
            righteye = request.POST.get('righteye')



        pulse = request.POST.get('pulse')
        weight = request.POST.get('weight')
        roomhumidity = request.POST.get('roomhumidity')
        roomtemperature = request.POST.get('roomtemperature')
        existpatient=Existpatient(patientid=patientid,bpsys=bpsys,bpdia=bpdia,visceralfatlevel=visceralfatlevel,
            restingmetabolism=restingmetabolism,bmi=bmi,bfp=bfp,bodytemperature=bodytemperature,glucoselevel=glucoselevel,
                                  skeletalmusclepercentage=skeletalmusclepercentage,footbottom=footbottom,foottop=foottop,
                                  legs=legs,handsfront=handsfront,handsback=handsback,
                                  lefteye=lefteye,righteye=righteye,pulse=pulse,weight=weight,
                                  roomhumidity=roomhumidity,roomtemperature=roomtemperature)

        parent_dir = path_location
        identered =existpatient.patientid
        #timestr = time.strftime("%d_%m_%Y")
        date1 = date.split("-")
        print(date1)
        date1.reverse()
        date1="_".join(date1)
        print(date1)
        timestr=date1
        # path= r"C:\Users\Anuraag\Desktop\eecpdata"+"\\"+identered+"\\"+timestr
         # except (FileNotFoundError, IOError):
            #     os.mkdir(path)
            # try:
            #     path= r"C:\Users\Anuraag\Desktop\eecpdata"+"\\"+identered+"\\"+timestr
            # except OSError as error:
            #     path= r"C:\Users\Anuraag\Desktop\eecpdata"+"\\"+identered+"\\"+timestr
            #     os.mkdir(path)
            # except FileNotFoundError:
            #     path= r"C:\Users\Anuraag\Desktop\eecpdata"+"\\"+identered+"\\"+timestr
            #     os.mkdir(path)
        #path= r"C:\Users\Anuraag\Desktop\eecpdata"+"\\"+identered+"\\"+timestr
        try:
            path= path_location+"\\"+identered+"\\"+timestr
            os.mkdir(path)
            print("came to try")
            print(path)
            dict2=request.POST
            with open(path + r"\Before_details.csv", 'a') as csvfile:
                wrt = csv.writer(csvfile)
                for key, value in dict2.items():

                    wrt.writerow([key, value])
        except OSError as error:

            path= path_location+"\\"+identered+"\\"+timestr
            dict2 = request.POST
            print("came to except")
            print(path)
            with open(path + r"\Before_details.csv", 'a') as csvfile:
                wrt = csv.writer(csvfile)
                for key, value in dict2.items():

                    wrt.writerow([key, value])

        existpatient.save()
        return render(request,'exipu.html')



    return render(request,'exipu.html')
def after(request):
    if request.method=="POST":
        date=request.POST.get("date")
        patientid=request.POST.get('patientid')
        bpsys=request.POST.get('bpsys')
        bpdia = request.POST.get('bpdia')
        visceralfatlevel = request.POST.get('visceralfatlevel')
        restingmetabolism = request.POST.get('restingmetabolism')
        bmi = request.POST.get('bmi')
        bfp = request.POST.get('bfp')
        bodytemperature = request.POST.get('bodytemperature')
        skeletalmusclepercentage = request.POST.get('skeletalmusclepercentage')


        try:
            footbottom = request.FILES['footbottom']
            fs = FileSystemStorage()
            fs.save(footbottom.name, footbottom)
        except MultiValueDictKeyError:
            footbottom = request.POST.get('footbottom')

            

        try:
            foottop = request.FILES['foottop']
            fs1 = FileSystemStorage()
            fs1.save(foottop.name, foottop)
        except MultiValueDictKeyError:
            foottop = request.POST.get('foottop')


        try:
            legs = request.FILES['legs']
            fs2 = FileSystemStorage()
            fs2.save(legs.name, legs)
        except MultiValueDictKeyError:
            legs = request.POST.get('legs')

            
        try:
            handsfront = request.FILES['handsfront']
            fs3 = FileSystemStorage()
            fs3.save(handsfront.name, handsfront)
        except MultiValueDictKeyError:
            handsfront = request.POST.get('handsfront')

           

        try:
            handsback = request.FILES['handsback']
            fs4 = FileSystemStorage()
            fs4.save(handsback.name, handsback)
        except MultiValueDictKeyError:
            handsback = request.POST.get('handsback')

           

        try:
            lefteye = request.FILES['lefteye']
            fs5 = FileSystemStorage()
            fs5.save(lefteye.name, lefteye)
        except MultiValueDictKeyError:
            lefteye = request.POST.get('lefteye')

           

        try:
            righteye = request.FILES['righteye']
            fs6 = FileSystemStorage()
            fs6.save(righteye.name, righteye)
        except MultiValueDictKeyError:
            righteye = request.POST.get('righteye')

        pulse = request.POST.get('pulse')
        weight = request.POST.get('weight')
        roomhumidity = request.POST.get('roomhumidity')
        roomtemperature = request.POST.get('roomtemperature')
        afterpatient=AfterPatient(patientid=patientid,bpsys=bpsys,bpdia=bpdia,visceralfatlevel=visceralfatlevel,restingmetabolism=restingmetabolism,bmi=bmi,bfp=bfp,bodytemperature=bodytemperature,
                                  skeletalmusclepercentage=skeletalmusclepercentage,footbottom=footbottom,foottop=foottop,legs=legs,handsfront=handsfront,handsback=handsback,
                                  lefteye=lefteye,righteye=righteye,pulse=pulse,weight=weight,roomhumidity=roomhumidity,roomtemperature=roomtemperature)

        parent_dir = path_location
        identered = afterpatient.patientid
        date1 = date.split("-")
        print(date1)
        date1.reverse()
        date1="_".join(date1)
        print(date1)
        timestr=date1
        timestr = date1
        # path = r"C:\Users\Anuraag\Desktop\eecpdata" + "\\" + identered + "\\" + timestr
        # os.mkdir(path)
        try:
           path= path_location+"\\"+identered+"\\"+timestr
           os.mkdir(path)
           dict4 = request.POST
           with open(path + r"\After_details.csv", 'a') as csvfile:

               wrt = csv.writer(csvfile)
               for key, value in dict4.items():

                   wrt.writerow([key, value])
        except OSError as error:


            path= path_location+"\\"+identered+"\\"+timestr
            dict4 = request.POST
            with open(path + r"\After_details.csv", 'a') as csvfile:

                wrt = csv.writer(csvfile)
                for key, value in dict4.items():

                    wrt.writerow([key, value])
            

        afterpatient.save()
        return render(request,'after.html')
    return render(request, 'after.html')
def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
