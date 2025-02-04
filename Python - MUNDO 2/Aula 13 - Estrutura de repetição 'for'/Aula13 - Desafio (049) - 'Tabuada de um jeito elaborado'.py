esc = int(input('Digite qual tabuada você quer: '))
print('')

for c in range(1, 11):
    tab = esc * c
    print('{} x {} = {}'.format(esc, c, tab))
