s=input()
for i in range(len(s)):
    if(not(ord(s[i])>47 and ord(s[i])<58)):
        print(s[i],end="")
for i in range(len(s)):
    if(ord(s[i])>47 and ord(s[i])<58):
        print(s[i],end="")