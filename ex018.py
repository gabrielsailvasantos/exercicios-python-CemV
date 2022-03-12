from math import radians, sin, cos, tan
ang = float(input('Digite o angulo: '))
seno = sin(radians(ang))
print('O angulo de {} tem o seno de {:.2f}'.format(ang, seno))
cosseno = cos(radians(ang))
print('O angulo de {} tem o cosseno de {:.2f}'.format(ang, cosseno))
tangente = tan(radians(ang))
print('O angulo de {} tem a tangente de {:.2f}'.format(ang, tangente))
