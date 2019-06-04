from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def welcome(request):
    return HttpResponse("welcome back %s." % request.user.get_username())
