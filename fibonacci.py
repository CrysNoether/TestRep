def fibonacci(n):
    cajaA = 1
    cajaB = 0
    count = n - 1
    fibList = [1]
    while count > 0:
        cajaB = cajaA + cajaB
        cajaA = cajaB
        count = count - 1
        fibList.append(cajaB)
        continue
    print(cajaA)
    print(fibList)

n = int(input("Number? "))
fibonacci(n)
