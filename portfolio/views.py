from django.shortcuts import render, redirect  # Combined these at the top
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

    total_portfolio_value = 0 

    for coin in coins:
        if coin.symbol.upper() == 'BTC':
            qty = float(coin.quantity)
            bought_at = float(coin.price_purchased)
            
            coin.current_value = qty * live_price
            coin.profit = coin.current_value - (qty * bought_at)
            total_portfolio_value += coin.current_value 
        else:
            coin.current_value = 0
            coin.profit = 0

    return render(request, 'portfolio/portfolio_list.html', {
        'coins': coins, 
        'live_price': live_price,
        'total_value': total_portfolio_value
    })

# This starts all the way at the left margin
def add_coin(request):
    if request.method == "POST":
        name = request.POST.get('name')
        symbol = request.POST.get('symbol').upper()
        quantity = request.POST.get('quantity')
        price_purchased = request.POST.get('price_purchased')

        Coin.objects.create(
            name=name,
            symbol=symbol,
            quantity=quantity,
            price_purchased=price_purchased
        )
        return redirect('portfolio_list')
    
    return render(request, 'portfolio/add_coin.html')