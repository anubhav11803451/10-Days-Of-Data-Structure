stocks = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]


def buy_and_sell_stock_once(prices):

    buying_price = prices[0]
    max_profit = 0

    for selling_price in prices:
        buying_price = min(buying_price, selling_price)
        profit = selling_price - buying_price
        max_profit = max(max_profit, profit)

    return max_profit


print("Max_Profit:", buy_and_sell_stock_once(stocks))
