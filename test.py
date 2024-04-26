count = int(input())

obj = []
for i in range(count):
    for j in input().split():
        obj.append(j)
    
for i in set(obj):
    print(i)
    