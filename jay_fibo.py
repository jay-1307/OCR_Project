startNumber = int(raw_input("Enter the start number here "))
endNumber = int(raw_input("Enter the end number here "))
def fibo(n):
    if n < 2:
        return n
    return fibo(n-1) + fibo(n-2)
for e in range(startNumber, endNumber):
    print fibo(e)
