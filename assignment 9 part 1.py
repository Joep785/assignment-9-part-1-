sales = { 'cost_price_per_unit': 20, 'sell_price_per_unit': 30, 'inventory': 1000 }
total_profit = (sales['sell_price_per_unit'] - sales['cost_price_per_unit']) * sales['inventory']
total_profit = round(total_profit)
print(f"The total profit made is ${total_profit}.")