num = list(input("enter a binary number: " ))
num.reverse()
sum = 0
for i in range(len(num)):
    if num[i] == '1':
        sum = sum + pow(2,i)
print (sum)        
