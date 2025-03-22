n, m = map(int, input().split())
max_value = -1
winners = []

for i in range(n):
    row = list(map(int, input().split()))[:m]
    best_attempt = max(row)
    
    if best_attempt > max_value:
        max_value = best_attempt
        winners = [i] 
    elif best_attempt == max_value:
        winners.append(i)

print(len(winners))
print(*winners)
