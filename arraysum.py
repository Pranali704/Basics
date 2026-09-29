n = int(input("Enter n:"))

arr = []

for i in range(n):
    num = int(input("Enter elements:"))
    arr.append(num)

sum = 0

for i in range(n):
    sum = sum + arr[i]

print(sum)

