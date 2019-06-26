
def isPrime(n):
    if (n <= 1):
        return False
    for y in range(2, n):
        if (n % y ==0):
            return False
    else:
        return True
def list_prime():
    for i in range(100):
        if isPrime(i):
            print(i, end=" ", flush=True)
    print()
list_prime()
