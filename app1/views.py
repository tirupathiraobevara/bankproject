from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
def Home_page(request):
    return render(request,'app1/home.html')
@login_required
def Customer(request):
    return render(request,'app1/customer.html')
def Logout(request):
    return render(request,'app1/logout.html')
def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserCreationForm()
    return render(request,'app1/registration.html',{'form':form})

# Create your views here.
