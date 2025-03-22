n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

symmetric = True
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break 
    if not symmetric:
        break

print("yes" if symmetric else "no")
