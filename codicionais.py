"""
numero=int(input('digite um numero'))

if numero % 2 ==0 :
    print('Esse numero e par')
else :
    print ('esse numero e impar')

idade=int(input('digite sua idade'))

if idade  < 12  :
   print('Criança')
elif idade < 18 :
  print ('Adolescente')
else :
   print('adulto')

usario = str(input('digite seu usuario'))
senha =int(input('digiter sua senha '))

if usario == 'davi'and senha == 1123:
   print("bem vido o")
else:
   print('erro')
"""

x = float(input('digite a cordenada x'))
y =float(input('digite a cordenada y'))

if x > 0 and y > 0:
    print('o ponto está no primeiro quadrante')
elif x < 0 and y> 0:
    print('o ponto está no ssegundo quadrante')
elif x < 0 and y < 0:
    print('o ponto está no terceiro quandrante')
elif x> 0 and y < 0:
    print ('o ponto está no quarto quadrante')
else :
    print('o ponto esta sobre um eixo na origem')