#вагоны
a=int(input())
lst = ['w','m','a','a','m','w','w','m','a','a','m','w']
count = list(range(11,0,-2))
print(count)
b = lst[(a-1)%12]
if a % 12 <= 6:
    another_seat = a + count[(a%6)-1]
if a % 12 > 6:
    count.reverse()
    another_seat = a - count[(a%6)-1]
print(f'{another_seat}{b}')
