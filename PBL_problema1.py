'''/*******************************************************************************
Autor: Amanda Lima Bezerra
Componente Curricular: MI - Algoritmos I
Concluido em: 23/03/2022
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************/'''

# Declaração das variáveis, algumas outras foram declaradas ao longo do código por motivos de
# um funcionamento correto do programa.

# Booleana
iniciador = True

# Inteira
quantidade_acucar = quantidade_arroz = quantidade_cafe = quantidade_extrato = 0
quantidade_macarrao = quantidade_bolacha = quantidade_oleo = quantidade_farinha_trigo = 0
quantidade_feijao = quantidade_sal = quantidade_extra = 0
soma_quant_PF = soma_quant_PJ = 0
quantidade_cestas = 0
cestas_com_extra = cestas_sem_extra = 0

# Declarando as listas para armazenar os dados do nome e contato dos doadores

lista_nomes = []
lista_contatos = []

# Inicio do programa

print('Bem-vindo(a)\nSistema disponível para cadastro das doações')
print('Observação:\nQuestões com números o funcionário deve digitar o número correspondente a opção desejada')

while iniciador:
    # Entrada dos dados.

    nome_doador = input('Coloque o nome do doador: ')
    lista_nomes.append(nome_doador)

    contado_doador = input('Coloque o contato do doador: ')
    lista_contatos.append(contado_doador)

    tipo_doador = input('1. Pessoa física\n2. Pessoa jurídica\n')

    # Validação da entrada do tipo de doador.
    while not (tipo_doador.isnumeric()) or isinstance(tipo_doador, float) \
            or (int(tipo_doador) != 1 and int(tipo_doador) != 2):
        print('Resposta inválida.')
        tipo_doador = input('1. Pessoa física\n2. Pessoa jurídica\n')

    # Mudando a variável de string para inteiro.
    tipo_doador = int(tipo_doador)

    # A variável iniciador_itens está nesse local e não no inicio, pois é preciso que a cada novo cadastro de uma
    # pessoa ela permita a entrada no while dos itens.
    iniciador_itens = True

    while iniciador_itens:
        item = input('Itens da cesta básica:\n\n'
                     '1. Açúcar\n'
                     '2. Arroz\n'
                     '3. Café\n'
                     '4. Extrato de Tomate\n'
                     '5. Pacote de macarrão\n'
                     '6. Pacote de bolacha\n'
                     '7. Óleo\n'
                     '8. Farinha de trigo\n'
                     '9. Feijão\n'
                     '10. Sal\n'
                     '11. Item extra\n'
                     '12. Sair do cadastro de itens\n\nCódigo: ')
        while not (item.isnumeric()) or isinstance(item, float) or int(item) < 1 or int(item) > 12:
            print('Resposta inválida.\n')
            item = input('Itens da cesta básica:\n\n'
                             '1. Açúcar\n'
                             '2. Arroz\n'
                             '3. Café\n'
                             '4. Extrato de Tomate\n'
                             '5. Pacote de macarrão\n'
                             '6. Pacote de bolacha\n'
                             '7. Óleo\n'
                             '8. Farinha de trigo\n'
                             '9. Feijão\n'
                             '10. Sal\n'
                             '11. Item extra\n'
                             '12. Sair do cadastro de itens\n\nCódigo: ')

        # Mudando a variável de string para inteiro.
        item = int(item)

        # É necessário zerar a variável quantidade para não atrapalhar na contagem das
        # pessoas físicas e pessoas juridicas.
        quantidade = 0

        if item == 1:
            quantidade = input('Quantidade em quilogramas de açúcar: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em quilogramas de açúcar: ')
            quantidade = float(quantidade)
            quantidade_acucar += quantidade
        elif item == 2:
            quantidade = input('Quantidade em quilogramas de arroz: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em quilogramas de arroz: ')
            quantidade = float(quantidade)
            quantidade_arroz += quantidade
        elif item == 3:
            quantidade = input('Quantidade em quilogramas de café: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em quilogramas de café: ')
            quantidade = float(quantidade)
            quantidade_cafe += quantidade
        elif item == 4:
            quantidade = input('Quantidade de unidades de extrato de tomate: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade de unidades de extrato de tomate: ')
            quantidade = float(quantidade)
            quantidade_extrato += quantidade
        elif item == 5:
            quantidade = input('Quantidade de unidades de pacotes de macarrão: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade de inidades de pacotes de macarrão: ')
            quantidade = float(quantidade)
            quantidade_macarrao += quantidade
        elif item == 6:
            quantidade = input('Quantidade de unidades de pacotes de bolacha: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade de unidades de pacotes de bolacha: ')
            quantidade = float(quantidade)
            quantidade_bolacha += quantidade
        elif item == 7:
            quantidade = input('Quantidade em litros de óleo: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em litros de óleo: ')
            quantidade = float(quantidade)
            quantidade_oleo += quantidade
        elif item == 8:
            quantidade = input('Quantidade em quilogramas de farinha de trigo: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em quilogramas de farinha de trigo: ')
            quantidade = float(quantidade)
            quantidade_farinha_trigo += quantidade
        elif item == 9:
            quantidade = input('Quantidade em quilogramas de feijão: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em quilogramas de feijão: ')
            quantidade = float(quantidade)
            quantidade_feijao += quantidade
        elif item == 10:
            quantidade = input('Quantidade em quilogramas de sal: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em quilogramas de sal: ')
            quantidade = float(quantidade)
            quantidade_sal += quantidade
        elif item == 11:
            quantidade = input('Quantidade em unidades do item extra: ')
            while not (quantidade.isnumeric()) or float(quantidade) < 0:
                print('Resposta inválida.\n')
                quantidade = input('Quantidade em unidades do item extra: ')
            quantidade = float(quantidade)
            quantidade_extra += quantidade
        # O último item desse bloco foi usado para sair ou não da repetição do cadastro dos itens.
        else:
            iniciador_itens = False

        # Contando quantos itens cada pessoa física ou pessoa jurídica doaram.
        if tipo_doador == 1:
            soma_quant_PF += quantidade
        else:
            soma_quant_PJ += quantidade

    continuacao = input('Deseja continuar o cadastro?\nPor favor coloque o número correspondente\n'
    '1. SIM\n2. NÃO\n')

    # Validação da entrada que permite a continuação ou não do cadastro.
    while not (continuacao.isnumeric()) or isinstance(continuacao, float) \
            or (int(continuacao) != 1 and int(continuacao) != 2):
        print('Resposta inválida.\n')
        continuacao = input('Deseja continuar o cadastro?\nPor favor coloque o número correspondente\n'
        '1. SIM\n2. NÃO\n')

    # Mudando a variável de string para inteiro.
    continuacao = int(continuacao)

    # O último item desse bloco foi usado para sair ou não da repetição do menu.
    if continuacao == 2:
        iniciador = False

# Total de doações recolhidas.
print('Quantidade de itens doados:\n\nAçúcar em Kg: %.2f\nArroz em Kg: %.2f\nCafé em Kg: %.2f\n'
      'Extrato de tomate unidades: %d\nPacote de macarrão unidades: %d\nPacote de bolacha unidades: %d\n'
      'Óleo em litros: %.2f\nFarinha de trigo em Kg: %.2f\nFeijão em Kg: %.2f\nSal: %.2f\n'
      'Itens extras unidades: %d\n' % (quantidade_acucar, quantidade_arroz, quantidade_cafe,
       quantidade_extrato, quantidade_macarrao, quantidade_bolacha, quantidade_oleo, quantidade_farinha_trigo,
       quantidade_feijao, quantidade_sal, quantidade_extra))

# Total de itens doados por pessoas físicas e juridicas.
print('Total de itens doados por pessoas físicas: %.2f' % (soma_quant_PF))
print('Total de itens doados por pessoas jurídicas: %.2f\n' % (soma_quant_PJ))

# Contagem das cestas básicas.
while quantidade_acucar >= 1 and quantidade_arroz >= 4 and quantidade_cafe >= 2 and quantidade_extrato >= 2 \
        and quantidade_macarrao >= 3 and quantidade_bolacha >= 1 and quantidade_oleo >= 1 \
        and quantidade_farinha_trigo >= 1 and quantidade_feijao >= 4 and quantidade_sal >= 1:
    quantidade_acucar -= 1
    quantidade_arroz -= 4
    quantidade_cafe -= 2
    quantidade_extrato -= 2
    quantidade_macarrao -= 3
    quantidade_bolacha -= 1
    quantidade_oleo -= 1
    quantidade_farinha_trigo -= 1
    quantidade_feijao -= 4
    quantidade_sal -= 1
    quantidade_cestas += 1

# Quantidade de cestas que podem ser formadas.
print('A quantidade de cestas que podem ser formadas é %d\n' % (quantidade_cestas))

if quantidade_cestas >= quantidade_extra:
    # Nesse caso a quantidade limitadora é a quantidade de itens extras, então a quantidade de cestas
    # com itens extra é a quantidade de itens extra.
    cestas_com_extra = quantidade_extra
    print('A quantidade de cesta com itens extras são %d' % (cestas_com_extra))

    # Como já se sabe a quantidade de cestas com itens extras, coloquei nesse bloco a quantidade de
    # cestas sem itens extras.
    cestas_sem_extra = quantidade_cestas - cestas_com_extra
    print('A quantidade de cesta sem itens extras são %d\n' % (cestas_sem_extra))


    # Como numericamente itens usados e cestas com itens extras são iguais usei a variável cestas_com_extra para
    # contabilizar quantos itens extras estão sobrando.
    quantidade_extra -= cestas_com_extra

else:
    # Nesse caso a quantidade limitadora é a quantidade de cestas, então a quantidade de cestas
    # com itens extra é a quantidade de cestas formadas.
    cestas_com_extra = quantidade_cestas
    print('A quantidade de cesta com itens extras são %d' % (cestas_com_extra))

    # Como o número de itens extras superam o valor das cestas formadas, todas as cestas irão receber um
    # item extra. Então o valor das cestas sem itens extras será o valor que foi declarado no inicio do programa.
    print('A quantidade de cesta sem itens extras são %d\n' % (cestas_sem_extra))

    # Como numericamente itens usados e quantidade de cestas são iguais usei a variável quantidade_cestas para
    # contabilizar quantos itens extras estão sobrando.
    quantidade_extra -= quantidade_cestas

# Atualizando para o usuário a quantidade de itens restantes depois que formou as cestas.
print('Quantidade de itens restantes:\n\nAçúcar em Kg: %.2f\nArroz em Kg: %.2f\nCafé em Kg: %.2f\n'
      'Extrato de tomate unidades: %d\nPacote de macarrão unidades: %d\nPacote de bolacha unidades: %d\n'
      'Óleo em litros: %.2f\nFarinha de trigo em Kg: %.2f\nFeijão em Kg: %.2f\nSal: %.2f\n'
      'Itens extras unidades: %d\n' % (quantidade_acucar, quantidade_arroz, quantidade_cafe,
       quantidade_extrato, quantidade_macarrao, quantidade_bolacha, quantidade_oleo, quantidade_farinha_trigo,
       quantidade_feijao, quantidade_sal, quantidade_extra))

# Não foi obrigatório mas como sei o básico de listas resolvi colocar esse item extra.
print('Deseja ver a lista dos nomes e contatos dos doadores?')

visualizador_listas = input('1. Sim\n2. Não\n')
while not (visualizador_listas.isnumeric()) or isinstance(visualizador_listas, float) \
    or (int(visualizador_listas) != 1 and int(visualizador_listas) != 2):
    print('Resposta inválida.')
    visualizador_listas = input('1. Sim\n2. Não\n')

# Mudando a variável de string para inteiro.
visualizador_listas = int(visualizador_listas)


if visualizador_listas == 1:
    print('Lista de doadores', lista_nomes)
    print('Lista de contatos', lista_contatos)
    print('Programa finalizado, obrigada pela preferência!\nAutora: Amanda Lima Bezerra')
else:
    print('Programa finalizado, obrigada pela preferência!\nAutora: Amanda Lima Bezerra')