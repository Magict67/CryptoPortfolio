from django.shortcuts import render, redirect
from .models import Coin
import requests

def portfolio_list(request):
    coins = Coin.objects.all()
    
    # API URLs for current prices and 7-day history
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    chart_url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=7&interval=daily"
    
    try:
        # 1. Fetch Current Prices
        response = requests.get(url)
        data = response.json()
        prices = {
            'BTC': data.get('bitcoin', {}).get('usd', 0),
            'ETH': data.get('ethereum', {}).get('usd', 0)
        }
        
        # 2. Fetch Historical Data for the Chart
        chart_response = requests.get(chart_url)
        chart_data = chart_response.json()
        # Extracting the price values into a simple list of numbers
        prices_list = [item[1] for item in chart_data.get('prices', [])]
    except:
        prices = {'BTC': 0, 'ETH': 0}
        prices_list = []

    total_portfolio_value = 0 
    for coin in coins:
        live_price = prices.get(coin.symbol.upper(), 0)
        qty = float(coin.quantity)
        bought_at = float(coin.price_purchased)
        coin.current_value = qty * live_price
        coin.profit = coin.current_value - (qty * bought_at)
        total_portfolio_value += coin.current_value 

    # We are now sending 'prices_list' to the HTML
    return render(request, 'portfolio/portfolio_list.html', {
        'coins': coins, 
        'total_value': total_portfolio_value,
        'prices_list': prices_list 
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