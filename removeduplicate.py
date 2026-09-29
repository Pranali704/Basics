n = int(input("Enter the value of n:"))

arr = []

for i in range(n):
    arr.append(int(input("Enter the element:")))

unique = []

for i in range(n):
    if arr[i] not in unique:
        unique.append(arr[i])


print("Original array = ",arr)
print("Array after removing duplicates:",unique)


