num = 0.00298
i = 1
arr = []
print("{:<15} {:<15} {:<5}".format("Номер біта", "Мантиса", "Біти"))
while i <= 35:
    num *= 2
    if num > 1:
        num -= 1
        arr.append(1)
        print("{:<15} {:<15} {:<5}".format(i, round(num, 5), 1))
    else:
        arr.append(0)
        print("{:<15} {:<15} {:<5}".format(i, round(num, 5), 0))
    i += 1
print(arr[9:])

