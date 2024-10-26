number = int(input('введите чило в десятичной системе счисления:'))
result = ''

while number != 0:
    remainder = number % 16
    if remainder < 10:
        result = str(remainder) + result
    else:
        result = chr(remainder - 10 + ord('A')) + result
    number //= 16

print(result.upper())
