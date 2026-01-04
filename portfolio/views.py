from django.shortcuts import render
from .models import Coin

def portfolio_list(request):
    coins = Coin.objects.all()
    return render(request, 'portfolio/portfolio_list.html', {'coins': coins})