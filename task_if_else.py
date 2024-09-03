first, second, third = int(input()), int(input()), int(input())

if first == second == third: # Если все числа равны между собой, то вывести 3
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)