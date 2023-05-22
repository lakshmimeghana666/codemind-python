n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
sum=0
for i in range(a,b+1):
    l.append(i)
for i in s:
    if i not in l:
        sum=sum+i;
print(sum)