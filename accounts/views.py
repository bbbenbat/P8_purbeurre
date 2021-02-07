from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import *


def user_image_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup_user.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


