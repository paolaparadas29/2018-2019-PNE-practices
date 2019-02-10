from Seq import Seq

#Sequence 1
seq1 = Seq('ACTCT')

print('Sequence 1:', seq1.get_sequence())
print('Lenght:', seq1.len())
print('Bases count:', 'A:', seq1.count('A'), 'T:', seq1.count('T'), 'C:', seq1.count('C'), 'G:', seq1.count('G'))
print('Bases percentage:', 'A:', seq1.perc('A'),'%', 'T:', seq1.perc('T'),'%', 'C:', seq1.perc('C'),'%', 'G:',seq1.perc('G'),'%')

#Sequence 2


seq2= Seq('ACTCTTTTT')

print('Sequence 2:', seq2.get_sequence())
print('Lenght:', seq2.len())
print('Bases count:', 'A:', seq2.count('A'), 'T:', seq2.count('T'), 'C:', seq2.count('C'), 'G:', seq2.count('G'))
print('Bases percentage:', 'A:' ,seq2.perc('A'),'%', 'T:',seq2.perc('T'),'%', 'C:',seq2.perc('C'),'%', 'G:',seq2.perc('G'),'%')

#Sequence 3

seq3= seq1.complement()


print('Sequence 3:', seq3)
print('Lenght:', seq3.len())
print('Bases count:', 'A:', seq3.count('A'), 'T:', seq3.count('T'), 'C:', seq3.count('C'), 'G:', seq3.count('G'))
print('Bases percentage:', 'A:', seq3.perc('A'),'%', 'T:', seq3.perc('T'),'%', 'C:', seq3.perc('C'),'%', 'G:', seq3.perc('G'),'%')

#Sequence 4

seq4= seq1.reverse()

print('Sequence 4:', seq4)
print('Lenght:', seq4.len())
print('Bases count:', 'A:', seq4.count('A'), 'T:', seq4.count('T'), 'C:', seq4.count('C'), 'G:', seq4.count('G'))
print('Bases percentage:', 'A:', seq4.perc('A'),'%', 'T:', seq4.perc('T'),'%', 'C:', seq4.perc('C'),'%', 'G:', seq4.perc('G'),'%')
