from django.shortcuts import redirect, render
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry , Please wait for our response')
                return redirect('/car/'+car_id)
        
        contact = Contacts(car_id=car_id, car_title=car_title, user_id=user_id,
                       first_name=first_name, last_name=last_name, city=city, 
                       customer_need=customer_need, state=state, email=email,
                       phone=phone, message=message)
    
        admin_info = User.objects.get(is_superuser= True)
        admin_email = admin_info.email
        
        send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
    
        contact.save()
        messages.success(request, 'You request has been submitted, We will cotact you soon')
        return redirect('/cars/'+car_id)