n = int(input('Введите число: '))
z = int(input('Введите в какую систему исчисления нужно перевести: '))
eng_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def desyat_v_chislo(chislo, stepen):
    final = ''
    while chislo >= stepen:
        if chislo % stepen > 9:
            final += eng_big[chislo % stepen - 10]
        else:
            final += str(chislo % stepen)
        chislo = chislo // stepen
    final += str(chislo)
    return final[::-1]

print(f'Число {n} в {z}-ичной системе исчисления будет: {desyat_v_chislo(n, z)}')
