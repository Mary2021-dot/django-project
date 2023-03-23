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
    donations = Donation.objects.order_by('-created_at')[:3]
    
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




def children_list(request):
    children = Child.objects.all()
    context = {'children': children}
    return render(request, 'orphan/children.html', context)





def edit_child(request, id):
    child = Child.objects.get(id=id)
    if request.method == 'POST':
        form = EditChildForm(request.POST, request.FILES, instance=child)
        if form.is_valid():
            form.save()
            return redirect('children')
    else:
        form = EditChildForm(instance=child)
    return render(request, 'orphan/edit_child.html', {'form': form})


from .forms import DeleteChildForm

class DeleteChildView(View):
    def get(self, request, id):
        child = get_object_or_404(Child, id=id)
        form = DeleteChildForm()
        return render(request, 'orphan/delete_child.html', {'child': child, 'form': form})

    def post(self, request, id):
        child = get_object_or_404(Child, id=id)
        form = DeleteChildForm(request.POST)
        if form.is_valid(): # check if form is valid first
            if form.cleaned_data['confirmation']:
                child.delete()
                return redirect('children_list')
        return render(request, 'orphan/delete_child.html', {'child': child, 'form': form})


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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # redirect to home page
                return redirect('/donation_form/')
    else:
        form = AuthenticationForm()
    return render(request, 'orphan/login.html', {'form': form})









from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import DonationForm
from .models import Donation

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required


def donation_form(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save()
            return HttpResponseRedirect(reverse('donation_success'))
    else:
        form = DonationForm()
    return render(request, 'orphan/donation_success.html', {'form': form})


def donation_success(request):
    return render(request, 'orphan/donation_success.html')






