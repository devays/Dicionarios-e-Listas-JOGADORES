time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(F'    Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    continuar = str(input('Quer continuar? [S/N] '))
    while continuar not in 'SsNn':
        print('Resposta inválida, digite apenas S ou N')
        continuar = str(input('Quer continuar?'))
    if continuar in 'Nn':
        break

print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f'ERRO! Não existe jogador com código {opc}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[opc]["nome"]}')
        for i, g in enumerate(time[opc]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')