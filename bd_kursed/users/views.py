from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm, UserProfile
from main.models import ShoppingCart
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfile(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfile(instance=request.user)
    total_count = 0
    total_sum = 0
    baskets = ShoppingCart.objects.filter(user=request.user)
    for basket in baskets:
        total_count += basket.count
        total_sum += basket.sum()
    context = {
        'form': form,
        'baskets': ShoppingCart.objects.filter(user=request.user),
        'total_count': total_count,
        'total_sum': total_sum,
    }
    return render(request, 'profile.html', context)

