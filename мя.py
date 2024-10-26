number = int(input('введите чило в десятичной системе счисления:'))
result = ''

d = '0123456789ABCDEF'
while number != 0:
    remainder = number % 16
    result = d[remainder]+ result
    number //= 16

print(result)
