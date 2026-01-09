from django.shortcuts import render, redirect
from .models import Coin
import requests

def portfolio_list(request):
    coins = Coin.objects.all()
    
    # We ask for BOTH bitcoin and ethereum prices in one go
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        prices = {
            'BTC': data.get('bitcoin', {}).get('usd', 0),
            'ETH': data.get('ethereum', {}).get('usd', 0)
        }
    except:
        prices = {'BTC': 0, 'ETH': 0}

    total_portfolio_value = 0 

    for coin in coins:
        # Look up the price based on the symbol (BTC or ETH)
        live_price = prices.get(coin.symbol.upper(), 0)
        
        qty = float(coin.quantity)
        bought_at = float(coin.price_purchased)
        
        coin.current_value = qty * live_price
        coin.profit = coin.current_value - (qty * bought_at)
        total_portfolio_value += coin.current_value 

    return render(request, 'portfolio/portfolio_list.html', {
        'coins': coins, 
        'total_value': total_portfolio_value
    })

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

def delete_coin(request, pk):
    coin = Coin.objects.get(pk=pk)
    coin.delete()
    return redirect('portfolio_list')