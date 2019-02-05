from Bases import count_bases

# Main program
s = (input('Enter the sequence: ')).upper()
n = count_bases(s)
# Calculate the total sequence lenght
tl= len(s)
print('This sequence is {} bases in lenght'.format(tl))

for key in n:
    # Calculate the percentage of As, Cs, Ts, Gs in the sequence
    if tl > 0:
        perc = round(100.0 * n[key] / tl, 1)
    else:
        perc = 0

    # Results for As, Cs, Ts, Gs bases
    print('Bases {}'.format(key))
    print('  Counter: {}'.format(n[key]))
    print('  Percentage: {}%'.format(perc))