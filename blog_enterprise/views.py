from django.shortcuts import redirect, render

from .forms import RegistrationForm
from blogs.models import Blog
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import Group


def home(request):
    posts = Blog.objects.filter(is_featured=True).order_by(
        '-updated_at')  # -: ordenado de manera descendente
    context = {
        'featured_posts': posts
    }
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='blog_group')
            group.user_set.add(user)
            return redirect('login')
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')

    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')
