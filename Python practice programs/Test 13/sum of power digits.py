c=0
n=int(input())
temp=n
while(temp!=0):
    temp//=10
    c+=1
sum,temp=0,n
while(temp!=0):
    sum+=(temp%10)**c
    temp//=10
print(sum)