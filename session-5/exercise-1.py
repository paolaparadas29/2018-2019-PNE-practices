def count_s(seq):
    """Counting the number of As, CS, Ts and Gs in the sequence"""

    # Counter for the As
    resulta = 0
    resultc = 0
    resultt=0
    resultg=0
    for b in seq:

        if b == 'A':
            resulta += 1
        elif b == 'C':
            resultc += 1
        elif b == 'T':
            resultt += 1
        elif b == 'G':
            resultg += 1
    # Return the result
    return results= {'A': resulta, 'C': resultc, 'T': resultt, 'G': resultg}




# Main program
s = input('Enter the sequence: ')
n = count_s(s)
print('The number of As is:  {}'.format(na))

# Calculate the total sequence lenght
tl= len(s)

#Calculate the percentage of As in the sequence
if tl>0:
    perc = round(100.0 * na/ tl,1)
else:
    perc=0

print('This sequence is {} bases in lenght'.format(tl))
print('The percentage of As is: {}%'.format(perc))
