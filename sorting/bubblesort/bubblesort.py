"""
  This code is the solution for bubble sort algorithm
"""
elements = list(map(int, input("Enter Elements:").split()))
count = len(elements)

# For multiple passes
for i in range(0, count-1):
    flag = 0
    # For swapping the elements placed adjusant
    for j in range(0, count-1-i):
        if (elements[j] > elements[j+1]):
            temp = elements[j]
            elements[j] = elements[j+1]
            elements[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(elements)
