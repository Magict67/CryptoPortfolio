from django.shortcuts import render
from .models import Coin
import requests

def portfolio_list(request):
    #  get  saved coins from  database
    coins = Coin.objects.all()
    
    # Working test code to get price
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        # Pull price same as test
        live_price = data['bitcoin']['usd']
    except:
        # Show this if down
        live_price = "Network Error"

    # Deliver coin and price
    return render(request, 'portfolio/portfolio_list.html', {
        'coins': coins, 
        'live_price': live_price
    })