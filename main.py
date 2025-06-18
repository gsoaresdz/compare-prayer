def ler_lista_arquivo(nome_arquivo):
    with open(nome_arquivo, encoding='utf-8') as f:
        return set(linha.strip() for linha in f if linha.strip())

base = ler_lista_arquivo('base.txt')
nova_lista = ler_lista_arquivo('nova.txt')

novas_oracoes = nova_lista - base
oracoes_que_sumiram = base - nova_lista

print("Novas orações encontradas:", novas_oracoes)
print("Orações que sumiram:", oracoes_que_sumiram)
