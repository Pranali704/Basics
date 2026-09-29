
n = int(input("Enter the value of n:"))

arr = []

for i in range(n):
    num = int(input("Enter the array elements:"))
    arr.append(num)

arr.sort()

print("Smallest=",arr[0])
print("Second smallest = ",arr[1])
print("Largest = ",arr[n-1])
print("Second largest = ",arr[n-2])


