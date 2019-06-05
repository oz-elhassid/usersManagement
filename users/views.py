from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import users.forms


@login_required
def welcome(request):
    # return HttpResponse("welcome back %s" % request.user.get_username())
    # return HttpResponse(loader.get_template("registration/welcome.html").render())
    return render(request, 'registration/welcome.html')


def logout(request):
    return render(request, 'registration/logged_out.html')


@login_required
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = users.forms.CustomUserChangeForm(request.POST, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('update_profile_success'))
            return HttpResponseRedirect(reverse(welcome))
    else:
        form = users.forms.CustomUserChangeForm(instance=request.user)

    args['form'] = form
    return render(request, 'registration/user_update.html', args)


def register(request):
    args = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(welcome))
    else:
        form = UserCreationForm()
    args['form'] = form
    return render(request, 'registration/register.html', args)
