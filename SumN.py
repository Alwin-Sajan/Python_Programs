n = int(input("Enter the numbers : "));
if n <= 0:
    print("Positive natural number")
else:
    sum = 0 
    t = 0
    while t != n+1:
        sum += t
        t += 1
print("Sum is : ",sum)
