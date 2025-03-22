n = int(input())
arr = list(map(int, input().split()))[:n]
count = 0
for i in range(1, n - 1):
    if arr[i-1]<arr[i] and arr[i + 1] < arr[i]:
        count += 1
print(count)
