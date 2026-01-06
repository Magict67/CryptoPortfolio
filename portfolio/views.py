from django.shortcuts import render
from .models import Coin
import requests

def portfolio_list(request):
    coins = Coin.objects.all()
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        live_price = data['bitcoin']['usd']
    except:
        live_price = 0

    for coin in coins:
        if coin.symbol.upper() == 'BTC':
            # Make floats for math
            qty = float(coin.quantity)
            bought_at = float(coin.price_purchased)
            
            coin.current_value = qty * live_price
            coin.profit = coin.current_value - (qty * bought_at)
        else:
            coin.current_value = 0
            coin.profit = 0

    return render(request, 'portfolio/portfolio_list.html', {
        'coins': coins, 
        'live_price': live_price
    })