"""Peça para o usuário digitar uma velocidade 
inicial (em m/s), uma posição inicial (em m) e um instante 
de tempo (em s) e imprima a posição de um projétil nesse 
instante de tempo. 
Use a fórmula matemática: y(t) = y(0) + v(0)*t + (g*(t**2)/2) 
Onde, g é a aceleração da gravidade (10m/s²), y(t) é 
a posição final, y(0) é a posição inicial, v(0) é a 
velocidade inicial e t é o instante de tempo."""

velocidade_i = float(input('Digite a velocidade inicial em metros por segundos: '))
posicao_i = float(input('Digite a posicao inicial em metros: '))
instante_tempo = int(input('Digite o tempo (em segundos) que deseja saber a posicao do projetil: '))
g = 10/(1**2)

posicao_f= posicao_i + (velocidade_i*instante_tempo) + (g*(instante_tempo**2)/2)

print(f'A posicao do projetil em {instante_tempo}s e de: {posicao_f} metros')
