a = input('Enter A Number:')
b = input('Now Enter another Number:')

sum = a + b
print('\ndata Type sum:', sum, type(sum))

sum = int(a) + int(b)
print('Data Type Sum:', sum, type(sum))

sum = float(sum)
print('Data Type sum:', sum, type(sum))

sum = chr(int(sum))
print('Data Type sum:', sum, type(sum))