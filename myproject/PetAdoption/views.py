from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render, redirect
from .models import shelter,article,contact,pet,category,order,address
from .forms import contactview, RegisterForm, checkoutform

def homepage(request):
    dogs=pet.objects.filter(category='1')[:3]
    cats=pet.objects.filter(category='2')[:3]
    return render(request, 'PetAdoption/home.html', {'dogs':dogs, 'cats':cats})

def registerview(request):
    if request.method == "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
        messages.error(request,"invalid form")
    form=RegisterForm()
    return render(request,'PetAdoption/register.html',{'form':form})

def loginview(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            messages.error(request,"invalid username or password")
        messages.error(request,"invalid username or password")
    form=AuthenticationForm()
    return render(request,'PetAdoption/login.html',{'form':form})
def logoutview(request):
    logout(request)
    return redirect('home')
def alldogs(request):
    dogs=pet.objects.filter(category='1')
    return render(request, 'PetAdoption/alldog.html', {'dogs': dogs})

def allcats(request):
    cats=pet.objects.filter(category='2')
    return render(request, 'PetAdoption/allcat.html', {'cats': cats})


def petbreed(request):
    pets=pet.objects.all()
    return render(request, 'PetAdoption/petbreed.html',{ 'pets' : pets} )

def shelters(request):
    shelters = shelter.objects.all()
    return render(request, 'PetAdoption/shelter.html',{'shelters' : shelters} )

def articles(request):
    articles = article.objects.all()
    return render(request, 'PetAdoption/article.html',{'articles' : articles} )

class petdetails(DetailView):
    model= pet
    template_name = "PetAdoption/petdetail.html"

def search(request):
    if request.method == "POST" and 'btn1' in request.POST:
        searched= request.POST.get('searched')
        pets=pet.objects.filter(breed__contains=searched, category='1')
        return render(request,'PetAdoption/search.html',{'searched':searched, 'pets':pets})
       
    if request.method == "POST" and 'btn2' in request.POST:
        searched= request.POST.get('searched')
        pets=pet.objects.filter(breed__contains=searched, category='1')
        return render(request,'PetAdoption/search.html',{'searched':searched, 'pets':pets})

def checkoutview(request,id):
    if request.method== 'POST':
        form=checkoutform(request.POST)
        if form.is_valid():
            street=form.cleaned_data['street_address']
            state=form.cleaned_data['state']
            zip=form.cleaned_data['zip']
            country=form.cleaned_data['country']
            phone=form.cleaned_data['phone']
            add=address(
                user=request.user,
                street_address=street,
                state=state,
                zip=zip,
                country=country,
                phone=phone
            )
            add.save()
            pets=pet.objects.get(id=id)
            orders=order(
                user=request.user,
                pet=pets,
                address=add
            )
            orders.save()
            return redirect('home')
        messages.error(request, "invalid checkout")
    form=checkoutform()
    return render(request, "PetAdoption/checkout.html",{'form':form})

class contactus(FormView):
    def get(self, request, *args, **kwargs):
        return render(request,'PetAdoption/contact.html')
    def post(self, request, *args, **kwargs):
        form=contactview(request.POST)
        if form.is_valid():
            cnt=contact()
            cnt.name=request.POST.get('name')
            cnt.email=request.POST.get('email')
            cnt.subject=request.POST.get('subject')
            cnt.description=request.POST.get('message')
            cnt.save()

            return render(request,'PetAdoption/contact.html')

