def count_bases(seq):
    """Counting the number of As, CS, Ts and Gs in the sequence"""

    # Counter for the As
    resulta = 0
    # Counter for the Cs
    resultc = 0
    # Counter for te Ts
    resultt=0
    # Counter for the Gs
    resultg=0

    for base in seq:

        if base == 'A':
            resulta += 1
        elif base == 'C':
            resultc += 1
        elif base == 'T':
            resultt += 1
        elif base == 'G':
            resultg += 1
          # Return the results
    results= {'A': resulta, 'C': resultc, 'T': resultt, 'G': resultg}
    return results