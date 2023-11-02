from django.shortcuts import render
from listinha.models import Listinha

# Create your views here.
def home(request):
    listinha = Listinha.objects.all()
    return render(request, "home.html", context={
        'listinha': listinha,
    })
def pokemon(request):
    return render(request, 'pokemon.html')