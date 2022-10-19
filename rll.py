print('Input string')
strok = input()
a = [*strok]
b = []
i = 0
c = 0
while i<len(strok)-1:
    if a[i+1]==a[i]:
        c+=1
        if a[i+1]!=a[i] and c!=0:
            b.append(c)
            b.append(a[i])
            c=0
    else:
        b.append(a[i])
    i+=1
print(b)