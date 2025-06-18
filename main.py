def ler_lista_arquivo(nome_arquivo):
    with open(nome_arquivo, encoding='utf-8') as f:
        return set(linha.strip() for linha in f if linha.strip())

base = ler_lista_arquivo('base.txt')
nova_lista = ler_lista_arquivo('nova.txt')

novas_oracoes = nova_lista - base
oracoes_que_sumiram = base - nova_lista

with open('diferencas.txt', 'w', encoding='utf-8') as f:
    f.write('Novas orações encontradas:\n')
    for oracao in sorted(novas_oracoes):
        f.write(f'- {oracao}\n')

    f.write('\nOrações que sumiram:\n')
    for oracao in sorted(oracoes_que_sumiram):
        f.write(f'- {oracao}\n')

print('Diferenças salvas em diferencas.txt')
