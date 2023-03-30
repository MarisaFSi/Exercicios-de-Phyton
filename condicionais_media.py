
#Calcular media de aprovacao - se media maior ou igual a 7 retornar aprovado

nota1= float(input('Digite a sua primeira nota! '))
nota2= float(input('Digite sua segunda nota! ')) 

media = (nota1 + nota2)/ 2

if media >=7:
    print('Sua media foi de ', media, 'Voce foi aprovado!')
elif media >= 5:
    print('Sua media foi de ', media, 'Voce esta na recuperacao!')    
else:
    print('Sua media foi de ', media, 'Voce foi reprovado!')
