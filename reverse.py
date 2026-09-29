n = int(input("Enter n:"))

arr = []

for i in range(n):
    arr.append(int(input("Enter array elements:")))

print("Original array = ",arr)

print("Reverse array = ",end=" ")

for i in range(n-1,-1,-1):
    print(arr[i],end=" ")



