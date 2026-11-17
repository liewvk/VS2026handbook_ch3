prices = [19.9, 12.5, 8.0]
subtotal = 0.0
for position, price in enumerate(prices, start=1):
    subtotal += price
    print(f'After item {position}: {subtotal:.2f}')
print(f'Final total: {subtotal:.2f}')

