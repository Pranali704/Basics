num = int(input("Enter number:"))

sum = 0
n = num

while(n>0):
    sum = sum*10 + (n%10)
    n=n//10
if(num==sum):
    print("Palindrome")
else:
    print("not palindrome")


