sum=0
s=input()
for i in range(len(s)):
    if(ord(s[i])>47 and ord(s[i])<58):
        sum+=int(s[i])
print(sum)