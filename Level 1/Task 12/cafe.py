# Declare menu items, stock and pricing
menu = ['muffin', 'pie', 'croissant', 'quiche']
stock = {'muffin': 80, 'pie': 140, 'croissant': 90, 'quiche': 50}
price = {'muffin': 70, 'pie': 75, 'croissant': 65, 'quiche': 85}

# Calculate the total stock value
total_stock_value = 0
for item in menu:
    if item in stock and item in price:
        total_stock_value += stock[item] * price[item]

# Output the stock value in Rands
print(f'R {total_stock_value :.2f}')