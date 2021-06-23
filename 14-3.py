import pyupbit
import time
from pandas import DataFrame

def williams(ticker, k):
    df = pyupbit.get_ohlcv(ticker)

    range = (df['high'] - df['low']) * k
    target = df['open'] + range.shift(1)

    cond = df['high'] > target
    buy = target[cond]
    sell = df['close'][cond]

    rate = sell / buy

    return rate.cumprod().iloc[-1]

williams("KRW-BTC", 0.5)
williams("KRW-MLK", 0.5)

data = []
for k in range(1, 21):
    data.append([k/10, williams("KRW-BTC", k/10)])
    time.sleep(0.5)

df = DataFrame(data)
df.columns = ["k", "return rate"]
df.sort_values('return rate')
print(df)