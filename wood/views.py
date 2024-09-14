from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.shortcuts import render, get_object_or_404
from .models import Wood

def home(request):
    woods = Wood.objects.all()
    testimonies = Testimony.objects.all().order_by('-date_added')
    return render(request,'home.html', {'woods': woods, 'testimonies':testimonies})


def wood_list(request):
    woods = Wood.objects.all()
    return render(request, 'property-halfmap-grid.html', {'woods': woods})

def wood_detail(request, pk):
    wood = get_object_or_404(Wood, pk=pk)
    return render(request, 'wood-details-v1.html', {'wood': wood})

def contact(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to the database
        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()
        
        # Redirect after successful submission
        return redirect('home')  # Redirect to a thank you page or another URL
    
    return render(request, 'contact.html')  # Render the contact.html template for GET requests



def about(request):
    woods = Wood.objects.all()
    testimonies = Testimony.objects.all().order_by('-date_added')
    return render(request,'about-us.html', {'woods': woods, 'testimonies':testimonies})
