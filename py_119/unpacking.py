# Collection unpacking
stocks = ['TSM', 'NVDA', 'META', 'GOOG', 'AMZN', 'MSFT', 'TSLA', 'AAPL']
price = [123, 2342, 3425, 3245, 345, 3425, 34523, 3454]
stock_price = {k: v for k, v in zip(stocks, price)}

cryptos = ['BTC', 'ETH', 'XRP', 'assrocket']
p = [123, 2342, 3425, 3245]
crypto_price = {k: v for k, v in zip(cryptos, p)}

{**stock_price, **crypto_price}
stock_price | crypto_price