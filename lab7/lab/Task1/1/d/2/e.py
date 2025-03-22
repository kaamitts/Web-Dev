n, m = map(int, input().split()) 
best_athlete = -1
best_throw = -1
best_sum = -1

for i in range(n):
    throws = list(map(int, input().split()))[:m]
    max_throw = max(throws)
    total_score = sum(throws)

    if max_throw > best_throw:
        best_throw = max_throw
        best_sum = total_score
        best_athlete = i
        
    elif max_throw == best_throw:
        if total_score > best_sum:
            best_sum = total_score
            best_athlete = i

        
print(best_athlete)
