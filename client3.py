import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

# Initialize the dictionary to store prices
prices = {'ABC': 0, 'DEF': 0}

def getDataPoint(quote):
    """Produce all the needed values to generate a datapoint"""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    avg_price = (bid_price + ask_price) / 2  # Calculate the average price
    return stock, bid_price, ask_price, avg_price


def getRatio(price_a, price_b):
    """Calculate the ratio between two prices"""
    if price_b == 0:
        return  # Avoid ZeroDivisionError by not dividing by zero
    return price_a / price_b


# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        for quote in quotes:
            stock, bid_price, ask_price, avg_price = getDataPoint(quote)
            prices[stock] = avg_price  # Store the average price in the 'prices' dictionary
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, avg_price))

        ratio = getRatio(prices['ABC'], prices['DEF'])
        print("Ratio %s" % ratio)
