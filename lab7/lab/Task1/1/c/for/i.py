x = int(input())
count = 0
for d in range(1, x + 1):
    if x % d == 0:
        count+=1

print(count)