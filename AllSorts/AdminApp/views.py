from django.shortcuts import render,redirect
from . models import *
from Mixlyapp . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

def Useradmin(request):
    Certificate=Momentodata.objects.all().count()
    data1 = customerdata.objects.all().count()
    data=Momentodata.objects.all()
    data2=Profiledata.objects.all()
    latest_profile = Profiledata.objects.last()
    return render(request, 'index.html',{'data':data,'Certificate':Certificate,"data1":data1,'latest_profile':latest_profile,'data2':data2})



def addmemento(request):
    return render(request, ('memento.html'))

def Viewachievements(request):
    data=Momentodata.objects.all()
    return render(request,'View_achievements.html',{'data':data})

def Editmementos(request,id):
    data=Momentodata.objects.filter(id=id)
    return render(request, 'edit_mementos.html',{"data":data})

def mementodelete(rwquest,id):
    data=Momentodata.objects.filter(id=id).delete()
    return redirect('Viewachievements')

def Momentofoms(request):
    if request.method=='POST':
        Certificatename=request.POST['Certificatename']
        Position=request.POST['Position']
        image=request.FILES['image']
        Date=request.POST['Date']
        description=request.POST['description']
        data=Momentodata(Certificatename=Certificatename,Position=Position,image=image,Date=Date,description=description)
        data.save()
    return redirect('Viewachievements')


def Momentoupdate(request,id):
    if request.method=='POST':
        Certificatename=request.POST['Certificatename']
        Position=request.POST['Position']
        Date=request.POST['Date']
        description=request.POST['description']
        try:
            image=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=Momentodata.objects.get(id=id).image
        
        data=Momentodata.objects.filter(id=id).update(Certificatename=Certificatename,Position=Position,image=file,Date=Date,description=description)
    return redirect('Viewachievements')

def viewcustomer(request):
    data1 = customerdata.objects.all()
    return render(request, 'customer.html', {"data1": data1})

def customerdelete(request,id):
    data = customerdata.objects.filter(id=id).delete()
    return redirect('viewcustomer')


def profile(request):
    data2=Profiledata.objects.all()
    latest_profile = Profiledata.objects.last()
    return render(request,'My_profile.html',{"data2":data2,'latest_profile':latest_profile})

def profileform(request):
    if request.method=="POST":
        image=request.FILES['image']
        Name=request.POST['Name']
        Email=request.POST['Email']
        data2=Profiledata(image=image,Name=Name,Email=Email)
        data2.save() 
        return redirect('profile')
    

def Profilesettings(request):
    return render(request,('Profile_settings.html'))
