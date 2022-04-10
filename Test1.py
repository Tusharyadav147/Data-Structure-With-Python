arr = [14,33,27,10,35,19,42,44]
"""
num = 0
a = arr[num]
print(a)
for i in range(len(arr)):
    for j in range(len(arr)):
        if a > arr[j]:
            arr[num] = arr[j]
            arr[j] = a
            num = num+1
            print(arr)"""
"""space = ""
for i in range(10):
    space += "  "

print(space, "print")"""

str = "Tushar"
print(str[::-1])