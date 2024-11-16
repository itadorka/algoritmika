import math

a = int(input("Введите число: "))
if a < 2:
    print("Число не является простым")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Число простое")
    else:
        print("Число не является простым")
