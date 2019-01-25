def countingDNA(n):
    f = open(n,"r")
    f=f.readlines()

    print(f)#how to convert a list into a string
    f=''.join(f)
    print(f)
    sequence = f.replace('\n','')
    print(f)
    sequence= sequence.upper()
    lenght= len(sequence)
    a=sequence.count('A')
    c=sequence.count('C')
    t=sequence.count('T')
    g=sequence.count('G')

    print('Total lenght:', lenght)
    print('A:', a,'\n','C:',c,'\n','T:', t,'\n','G:', g)
    return

    f.close()

sequence= countingDNA('/home/alumno/Pycharmfirstprojects')

