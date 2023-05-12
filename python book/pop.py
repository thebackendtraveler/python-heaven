#!python3

basket = ['apple', 'bun', 'cola']
crate = ['egg', 'fig', 'grape']

print('Basket List:', basket)
print('Basket Elements:', len(basket))

basket.append('Damson')

print('Appended:', basket)
print('Last Item removed:', basket.pop())
print('BasketList:', basket)

basket.extend(crate)
print('Extended:', basket)
del basket[1]
print('Item Removed:', basket)
del basket[1:3]
print('Slice removed:', basket)