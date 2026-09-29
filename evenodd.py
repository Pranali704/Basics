n = int(input("Enter the value of n: "))

arr = []

for i in range(n):
    num = int(input("Enter array element:"))
    arr.append(num)

even = 0
odd = 0

for i in range(n):
    if arr[i]%2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even count:",even)
print("odd count:",odd)


