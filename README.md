# CryptoTrack Portfolio Manager
**Student:** Chris Thomas  
**Project:** Python Django Web App

## 🚀 Overview
CryptoTrack: web-based cryptocurrency tracker / manager. Users track real-time
holdings by retrieveing up-to-date data from a CoinGecko API.

## ✨ Features
* **Live Price Watch:** auto-gathers up-to-date BTC and ETH prices.
* **Data Diagramming:** Has 7-day Bitcoin trending chart with Chart.js.
* **CRUD Performance:** Add new coins to portfolio and "sell" (delete) them.
* **Automatic Computation:** Processes current value and total profit/loss from purchase price.

## 🛠️ Tech Stack
* **Backend:** Python 3, Django
* **Frontend:** HTML5, CSS3 (Inter Font), JavaScript (Chart.js)
* **API:** CoinGecko Simple Price & Market Chart API

## 🏃 How to Run
1. Install requirements: `pip install django requests`
2. Run migrations: `python manage.py migrate`
3. Start server: `python manage.py runserver`
4. Visit `http://127.0.0.1:8000/` in your browser.