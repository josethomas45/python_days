def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


n = int(input("Enter n: "))
r = int(input("Enter r: "))


print(f"{n}C{r} = {nCr(n, r)}")
