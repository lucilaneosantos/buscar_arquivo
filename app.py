import os
# entrada de dados para pesquisa
caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo de pesquisa: ')

# formata oarquivo com sua nomeclatura de acordo com tamanho


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    # ajuste de duas casas decimais
    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'


# guardar os arquivos encontrados com sucesso
conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:

                conta += 1
                # caminho completo do arquivo
                caminho_completo = os.path.join(raiz, arquivo)
                # filtra nome e tipo de arquivo percorrido na pasta
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                # verifica o tamanho do arquivo
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão do arquivo: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado: ', formata_tamanho(tamanho))
                # sem permissão de acesso
            except PermissionError as e:
                print('Sem permissão neste arquivo')
                # arquivo não encontrado
            except FileExistsError as e:
                print('Arquivo não encontrado')
                # erro desconhecido
            except Exception as e:
                print('Erro desconhecido:', e)
print()
print(f"{conta}(s) encontrado(s)")
