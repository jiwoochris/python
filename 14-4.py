import pyupbit
import time

def get_target_price():
    df = pyupbit.get_ohlcv("KRW-BTC", count = 30)
    volatility = (df.iloc[-2, 1] - df.iloc[-2, 2]) * 0.6
    target_price = df.iloc[-1, 0] + volatility
    return target_price

target_price = get_target_price()
print(target_price)

while True:
    
    price = pyupbit.get_current_price("KRW-BTC")
    if target_price <= price:
        print("매수!!!")
    print(target_price, price)

    time.sleep(1)