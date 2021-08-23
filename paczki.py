import sys
liczba_elementow = int(sys.argv[1])

numer_paczki = 1
waga_paczki = 0
wyslane_kilogramy = 0
waga_najlzejszej_paczki = 20
numer_najlzejszej_paczki = 0
koniec = 0

for numer_elementu in range(liczba_elementow):
    waga_elementu = int(input('Podaj wagę elementu w kilogramach: '))
    if numer_elementu == 0 and waga_elementu == 0:
        numer_paczki = 0
        break
    elif waga_elementu == 0:
        break
    elif waga_elementu < 1 or waga_elementu > 10:
        print('Błąd: Waga paczki musi mieścić się w zakresie 1-10 kg.')
        koniec = 1
        break
    else:
        wyslane_kilogramy += waga_elementu
        if waga_paczki + waga_elementu <= 20:
            waga_paczki += waga_elementu
        else:
            if waga_paczki < waga_najlzejszej_paczki:
                waga_najlzejszej_paczki = waga_paczki
                numer_najlzejszej_paczki = numer_paczki
            numer_paczki += 1
            waga_paczki = waga_elementu  
if waga_paczki < waga_najlzejszej_paczki:
                waga_najlzejszej_paczki = waga_paczki
                numer_najlzejszej_paczki = numer_paczki
puste_kilogramy = numer_paczki * 20 - wyslane_kilogramy

if koniec != 1:
    print(f'\nSuma "pustych" kilogramów: {puste_kilogramy}')
    print(f'Numer najlżejszej paczki: {numer_najlzejszej_paczki}, Waga najlżejszej paczki: {waga_najlzejszej_paczki}')
    print(f'Liczba paczek wysłanych: {numer_paczki}')
    print(f'Kilogramy wysłane: {wyslane_kilogramy}')