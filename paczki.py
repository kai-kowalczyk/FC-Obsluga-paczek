import sys
liczba_elementow = int(sys.argv[1])

numer_paczki = 0
waga_paczki = 0
wyslane_kilogramy = 0
puste_kilogramy = numer_paczki * 20 - wyslane_kilogramy

for numer_elementu in range(liczba_elementow):
    waga_elementu = int(input('Podaj wagę elementu w kilogramach: '))
    if waga_elementu == 0:
        print ('Błąd: Waga elementu nie może wynosić 0.')
        break
    elif waga_elementu < 1 or waga_elementu > 10:
        print('Błąd: Waga paczki musi mieścić się w zakresie 1-10 kg.')
        break