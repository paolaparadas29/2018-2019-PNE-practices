f= open('CPLX2.txt','r')
f=f.readlines()

i=[]
for line in f:
    if line.startswith('>'):
        line=''
    else:
        i.append(line)

f=''.join(i)
f=f.replace('\n','')

contA=0
contC=0
contT=0
contG=0
for i in f:
    if i=='A':
        contA+=1
    elif i=='C':
        contC+=1
    elif i=='G':
        contG+=1
    elif i=='T':
        contT+=1

print('The number of A\'s bases', contA)
print('The number of C\'s bases', contC)
print('The number of T\'s bases', contT)
print('The number of G\'s bases', contG)


