class Seq:
    #function to initialize variables
    def __init__(self, strbases, base):

        self.base = base
        self.strbases = strbases

    #function to return a variable
    def get_sequence(self):
        return self.strbases

    #function to get the lenght of the sequence
    def len(self):
        return len(self.strbases)

    #function to give the complement of a function
    def complement(self):

        D = {'A':'T','T':'A','C':'G','G':'C'}
        seq=[]

        for b in self.strbases:
            if b =='A':
                b=D[b]
                seq.append(b)
            elif b =='C':
                b=D[b]
                seq.append(b)
            elif b =='T':
                b=D[b]
                seq.append(b)
            elif b =='G':
                b=D[b]
                seq.append(b)
        trbases=''.join(seq)
        self.strbases=trbases
        return trbases

    #function to take the reverse of a complement sequence
    def reverse(self):
        t=self.strbases
        reverseseq = self.strbases[::-1]
        return reverseseq

    #function to count the bases
    def count(self):

        # Counter for the base
        result = 0
        for base in self.strbases:
            if base == self.base:
                result += 1
        # Return the result
        return result

    #function to get the perc
    def perc(self):

        if len(self.strbases)>0:
            v=self.count()
            r=self.len()
            perc = round(100.0*v/r, 1)
            return perc
        else:
            perc = 0
            return perc