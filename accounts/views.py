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
    success_signup = 'Bravo, tu fais partie de l\'équipe!'
    success_signup1 = 'Connectes-toi pour voir ton profil et sauvegarder ' \
                      'tes produits favoris!'
    return render(request, 'home.html', {'success_signup': success_signup,
                                         'success_signup1': success_signup1})
