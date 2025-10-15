s=input()
l=d=sp=o=0
i=0
while i<len(s):
    c=s[i]
    if 'a'<=c<='z' or 'A'<=c<='Z':l+=1
    elif '0'<=c<='9':d+=1
    elif c==' ':sp+=1
    else:o+=1
    i+=1
print("英文字符: "+str(l))
print("数字: "+str(d))
print("空格: "+str(sp))
print("其他字符: "+str(o))

