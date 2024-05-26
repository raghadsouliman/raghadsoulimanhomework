def fac(n):
    if n==0:
        return 1
    else:
        return n* fac (n-1)
num= int(input("enter a number:"))
result= fac(num)
print(f"the fac of{num} is{result}")
