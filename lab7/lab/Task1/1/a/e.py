v = int(input())
t = int(input()) 

distance = v * t

position = (distance % 109)  

print(position if position >= 0 else 109 + position)
