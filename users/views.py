from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.template import loader, RequestContext
from django.urls import reverse
from django.views.generic import UpdateView
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
            return HttpResponseRedirect(reverse('update_profile_success'))

    else:
        form = users.forms.CustomUserChangeForm(instance=request.user)

    args['form'] = form
    return render(request, 'registration/user_update.html', args)
    # return render_to_response('registration/user_update.html', context=RequestContext(request))
