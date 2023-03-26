# views.py

from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Child
from .forms import EditChildForm
from django.views import View
from .models import Donor,Event
from django.http import HttpResponseRedirect



def home(request):
    # Retrieve the latest 3 children added to the database
    children = Child.objects.order_by('-created_at')[:3]
    
    # Retrieve the latest 3 donations made to the orphanage
    donations = Donation.objects.order_by('-id')[:3]

    
    context = {
        'children': children,
        'donations': donations,
    }
    
    return render(request, 'orphan/home.html', context)

def base(request):
    return render(request, 'orphan/base.html')

def navbar(request):
    return render(request, 'orphan/navbar.html')

def footer(request):
    return render(request, 'orphan/footer.html')

def about(request):
    return render(request, 'orphan/about.html')




from .forms import DonorForm

from .forms import DonorForm

def donate_view(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'orphan/donation_success.html')
    else:
        form = DonorForm()
    return render(request, 'orphan/donate.html', {'form': form})



from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .forms import ContactForm
from .models import ContactMessage

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
            )

            messages.success(request, 'Your message was sent successfully!')
            return redirect(reverse('contact_us'))
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'orphan/contact_us.html', context)

def event_list(request):
    events = Event.objects.all()
    return render(request, 'orphan/event_list.html', {'events': events})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

from .forms import SignUpForm

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            # log in the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # redirect to success page
        return HttpResponseRedirect('/login/')        
    else:
        form = UserCreationForm()
    return render(request, 'orphan/signup.html', {'form': form})






from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # login(request, user)
                return HttpResponseRedirect('/donation_form/') 
            else:
                messages.error(request, "invalid details")

    form = AuthenticationForm()

    return render(request, 'orphan/login.html', context={"form": form})









from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import DonationForm
from .models import Donation

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import DonationForm

def donation_form(request):
    form = DonationForm()
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your donation!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
    context = {'form': form}
    return render(request, 'orphan/donation_form.html', context)




def afterlogin_view(request):
    if is_donor(request.user):
        return redirect('donation_form')
    else:
        return redirect('error-page')






