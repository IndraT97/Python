prices = [7,6,4,3,1]

if prices.index(min(prices)) == len(prices) - 1:
    print("0")
else:
    x = prices[prices.index(min(prices))]
    y = max(prices[prices.index(min(prices)):])
    print(y - x)