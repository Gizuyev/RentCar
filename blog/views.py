from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .models import Blog, FeedBacks
from .forms import CallbackForm
from .forms import CustomUserCreationForm
from .models import CustomUser, Car




# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    feedbacks = FeedBacks.objects.all()

    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CallbackForm()

    context = {
        'blogs': blogs,
        'feedbacks': feedbacks,
        'form': form,
    }

    return render(request, 'blog/index.html', context)


def about(request):
    return render(request, 'blog/about.html')

def blog(request):
    blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)

def car(request):
    return render(request, 'blog/car.html')



def contact(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = CallbackForm()

    context = {
        'form': form,
    }
    return render(request, 'blog/contact.html', context)



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'blog/login.html')
    


def logout_view(request):
    logout(request)
    return redirect('/')




def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

from django.shortcuts import render
from .models import Car  # Импортируем модель Car

def car_list(request):
    cars = Car.objects.all()  # Получаем список всех автомобилей из базы данных
    context = {'cars': cars}  # Создаем контекст с данными, которые будут доступны в шаблоне
    return render(request, 'blog/car.html', context) 