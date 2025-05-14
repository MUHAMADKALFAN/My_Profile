from django.shortcuts import render,redirect
from . models import *
from AdminApp . models import *

# Create your views here.
 

def Home(request):
    data=Momentodata.objects.all()
    return render(request,'home.html',{'data':data})
 
def customerform(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Message=request.POST['Message']
        data1=customerdata(Name=Name,Email=Email,Message=Message)
        data1.save()
    return redirect("Home")


def singleview(request,id):
    data= Momentodata.objects.filter(id=id)
    return render(request, 'single_view.html', {'data': data})

