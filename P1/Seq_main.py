from Seq import Seq

seq1a = Seq('ACTCT' ,'A')
seq1t = Seq('ACTCT','T')
seq1c = Seq('ACTCT','C')
seq1g = Seq('ACTCT','G')

print('Sequence 1:', seq1a.get_sequence())
print('Lenght:', seq1a.len())
print('Bases count:', 'A:', seq1a.count(), 'T:', seq1t.count(), 'C:', seq1c.count(), 'G:', seq1g.count())
print('Bases percentage:', 'A:', seq1a.perc(),'%', 'T:', seq1t.perc(),'%', 'C:', seq1c.perc(),'%', 'G:', seq1g.perc(),'%')

seq2a= Seq('ACTCTTTTT','A')
seq2t= Seq('ACTCTTTTT','T')
seq2c= Seq('ACTCTTTTT','C')
seq2g= Seq('ACTCTTTTT','G')

print('Sequence 2:', seq2a.get_sequence())
print('Lenght:', seq2a.len())
print('Bases count:', 'A:', seq2a.count(), 'T:', seq2t.count(), 'C:', seq2c.count(), 'G:', seq2g.count())
print('Bases percentage:', 'A:',seq2a.perc(),'%', 'T:',seq2t.perc(),'%', 'C:',seq2c.perc(),'%', 'G:',seq2g.perc(),'%')


seqc= seq1g.complement()
seq3a= Seq(seqc,'A')
seq3t= Seq(seqc,'T')
seq3c= Seq(seqc,'C')
seq3g= Seq(seqc,'G')

print('Sequence 3:', seqc)
print('Lenght:', seq3a.len())
print('Bases count:', 'A:', seq3a.count(), 'T:', seq3t.count(), 'C:', seq3c.count(), 'G:', seq3g.count())
print('Bases percentage:', 'A:', seq3a.perc(),'%', 'T:', seq3t.perc(),'%', 'C:', seq3c.perc(),'%', 'G:', seq3g.perc(),'%')

seqr= seq1g.reverse()
seq4a= Seq(seqr,'A')
seq4t= Seq(seqr,'T')
seq4c= Seq(seqr,'C')
seq4g = Seq(seqr,'G')
print('Sequence 4:', seqr)
print('Lenght:', seq4a.len())
print('Bases count:', 'A:', seq4a.count(), 'T:', seq4t.count(), 'C:', seq4c.count(), 'G:', seq4g.count())
print('Bases percentage:', 'A:', seq4a.perc(),'%', 'T:', seq4t.perc(),'%', 'C:', seq4c.perc(),'%', 'G:', seq4g.perc(),'%')
