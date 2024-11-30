
max = int(input("Please enter max number: "))
result = max
while max > 1:
    result = result * (max-1)
    max -= 1
print(result)