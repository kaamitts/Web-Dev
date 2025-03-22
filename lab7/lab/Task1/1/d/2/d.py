n, m = map(int, input().split())
max_value = -1
row_index = -1 
col_index = -1 

for i in range(n):
    row = list(map(int, input().split()))[:m]
    for j in range(m):
        if row[j] > max_value:
            max_value = row[j]
            row_index, col_index = i, j
        elif row[j] == max_value and i < row_index:
            row_index, col_index = i, j
        elif row[j] == max_value and i == row_index and j < col_index:
            col_index = j

print(max_value)
print(row_index, col_index)
