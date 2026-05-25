import requests
import pandas as pd
from cbonds_api_test import CBondsAPI

api = CBondsAPI()

# 1. Получаем общую информацию об облигации
bond = api.get_bond_info("RU000A10DQA8")
print(bond['document_rus'])   # Название выпуска
print(bond['maturity_date'])  # Дата погашения

# 2. Получаем историю торгов (котировки) за период
trades = api.get_market_trades("RU000A10DQA8", date_from="2024-01-01", date_to="2024-05-01")

# 3. Получаем купоны (денежные потоки)
coupons = api.get_bond_cashflows("RU000A10DQA8")
for coupon in coupons[:10]: # Выводим только первые 10 выплат для компактности
    print(f"Дата: {coupon.get('date')}, Купон: {coupon.get('cupon_sum')}, Амортизация: {coupon.get('redemtion')}")
