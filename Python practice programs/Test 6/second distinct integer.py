n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
for i in range(1,len(a)):
    if(a[i]!=a[i-1]):
        print(a[i])
        break