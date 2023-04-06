from django.shortcuts import render
from .models import Team

# Create your views here.

def home(request):
    team_members = Team.objects.all()
    context = {
        'team_members': team_members,
    }
    return render(request, 'home.html', context)


def about(request):
    team_members = Team.objects.all()
    context = {
        'team_members': team_members,
    }
    return render(request, 'pages/about.html', context)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')