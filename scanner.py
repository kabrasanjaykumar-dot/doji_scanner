
import yfinance as yf
import pandas as pd
import requests
import os

BOT = os.getenv("BOT_TOKEN")
CHAT = os.getenv("CHAT_ID")

def send(msg):
    requests.post(f"https://api.telegram.org/bot{BOT}/sendMessage",
                  data={"chat_id": CHAT, "text": msg})

def is_doji(o,h,l,c):
    body = abs(c-o)
    rng = h-l
    return body/rng <= 0.2 if rng else False

def run():
    stocks = ["RELIANCE","TCS","INFY","HDFCBANK","ICICIBANK","ITC"]

    for s in stocks:
        try:
            df = yf.download(s+".NS", interval="1mo", period="3mo")
            last = df.iloc[-1]

            if is_doji(last['Open'],last['High'],last['Low'],last['Close']):
                msg = f"{s} Doji\nHigh:{round(last['High'],2)}\nLow:{round(last['Low'],2)}"
                send(msg)
        except:
            pass

if __name__ == "__main__":
    run()
import time

while True:
    print("Bot running...")
    time.sleep(60)
