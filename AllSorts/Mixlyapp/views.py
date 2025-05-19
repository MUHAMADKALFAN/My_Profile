from django.shortcuts import render
from . models import *
from AdminApp . models import *
from .models import customerdata
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
 

def Home(request):
    data=Momentodata.objects.all()
    return render(request,'home.html',{'data':data})
 
def customerform(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        Email = request.POST['Email']
        Message = request.POST['Message']

        data1 = customerdata(Name=Name, Email=Email, Message=Message)
        data1.save()

        # Admin Notification Email
        admin_subject = "New Message from Website Contact Form"
        admin_message = f"""
        New message received:

        Name: {Name}
        Email: {Email}
        Message: 
        {Message}
        """
        send_mail(
            admin_subject,
            admin_message,
            settings.EMAIL_HOST_USER,
            ['muhammedkalfan0@gmail.com'],
            fail_silently=False,
        )

        # Auto-reply to user
        user_subject = "Thank You for Contacting Us!"
        user_message = f"""Dear {Name},

Thank you for contacting us!

We have received your message and will get back to you as soon as possible. Our team is reviewing your inquiry and will respond shortly.

If your matter is urgent, feel free to reply to this email or contact us directly at +91 9947883330.

We appreciate your interest and look forward to assisting you.

Best regards,
MUHAMAD KALFAN.K
"""
        send_mail(
            user_subject,
            user_message,
            settings.EMAIL_HOST_USER,
            [Email],
            fail_silently=False,
        )

        messages.success(request, "Message successfully submitted") 

        return redirect("Home")

def singleview(request,id):
    data= Momentodata.objects.filter(id=id)
    return render(request, 'Single_view.html', {'data': data})

