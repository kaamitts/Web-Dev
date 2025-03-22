n, m = map(int, input().split())
best_sum = -1
best_index = -1

for i in range(n):
    row = list(map(int, input().split()))[:m]
    total = sum(row)
    
    if total > best_sum:
        best_sum = total
        best_index = i
print(best_sum)
print(best_index)