#13

n=int(input())
warehouse=list(map(int, input().split()))
d=[0]*1000

for i in range(len(warehouse)):
    sum=0
    for j in range(i, len(warehouse), 2):
        sum+=warehouse[j]
    d[i]=sum

print(max(d))