def countingDNA(n):
    f = open(n,"r")
    f=f.readlines()
    f=''.join(f)
    sequence = f.replace('\n','')
    sequence= sequence.upper()
    lenght= len(sequence)
    a=sequence.count('A')
    c=sequence.count('C')
    t=sequence.count('T')
    g=sequence.count('G')


    print('Total lenght:', lenght)
    print('A:'+str(a)+'\n'+'C:'+str(c)+'\n'+'T:'+str(t)+'\n'+'G:'+str(g))
    return



sequence= countingDNA('DNA.txt')
