# llueve = input('¿Está lloviendo? ')
# haceFrio = input('¿Hace mucho frío? ')

# if llueve == 'si' and haceFrio == 'si':
#     print ('Entonces ponte abtigo y lleva paraguas')
# elif llueve == 'si' and haceFrio == 'no':
#     print ('Entonces lleva el paraguas')
# elif llueve == 'no' and haceFrio == 'si':
#     print ('Entonces ponte el abrigo y no lleves paraguas.')
# else:
#     print ('Anda asi nomas, si no está lloviendo ni hace frío.')

# print ('Andate luego y apurate que es tarde.')
a = 4
b = 3
r = b
while a > 1:
    a = a - 1
    b2 = b
    r2 = 0
    while b2 > 0:
        r2 = r2 + r
        b2 = b2 - 1
    r = r2
print(r)