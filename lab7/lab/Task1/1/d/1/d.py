n = int(input())
arr = list(map(int, input().split()))[:n]

print(sum(arr[i]>arr[i-1] for i in range(1,n)))