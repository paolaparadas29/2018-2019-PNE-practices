from Bases import count_bases
# Main program
s = (input('Enter the sequence 1: ')).upper()
t = (input('Enter the sequence 2: ')).upper()

# Combining both sequences
listbases=[s,t]

# Working with each one

# The first sequence
s = listbases[0]
n = count_bases(s)
# Calculate the total sequence lenght
tl= len(s)
print('The sequence 1 is {} bases in lenght'.format(tl))

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

# The second sequence

s = listbases[1]
n = count_bases(s)
# Calculate the total sequence lenght
tl= len(s)
print('The sequence 2 is {} bases in lenght'.format(tl))

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