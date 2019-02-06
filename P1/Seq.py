class Seq:

    def __init__(self, strbases, base):

        self.base = base

        self.strbases = strbases

    def len(self):

        return len(self.strbases)

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
        return trbases

    def reverse(self):

        s = self.complement()
        print(s)
        reverseseq = s[::-1]
        print(reverseseq)
        return reverseseq

    def count(self):

        # Counter for the base
        result = 0
        for base in self.strbases:
            if base == self.base:
                result += 1
        # Return the result
        return result


    def perc(self):

        if len(self.strbases)>0:
            v=self.count()
            r=self.len()
            perc = round(100.0 * v / r, 1)
            return perc
        else:
            perc = 0
            return perc
