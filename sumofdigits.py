

#ma'am logic

n = int(input("Enter the value of n"))
sum = 0
while(n>0):
    sum = sum + (n%10)
    n = n//10
print(sum)