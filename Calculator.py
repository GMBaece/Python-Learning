print('='*30,'Python Calculator','='*30)
print('          ','='*15,'Qual operação deseja fazer?','='*15)
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')
op = int(input('Digite o código da operação (1, 2, 3 ou 4): '))     # inserção do código da operação
operadores = (1,2,3,4)      #Restrição de códigos

# condcional para verificar qual operação será feita
if op not in operadores:                                    #reinício caso o usuário digite algo errado
    restart = int(input('Digite um código válido: '))       #inserção de um novo código
    op = restart
    if op not in operadores:
        erro = print('Código inválido')                     # exit se o código for inválido de novo
        exit()
    # continuação caso o código sejá válido
    else:
        x = int(input('Quantos números quer calcular: '))   # definição de quantos números serão inseridos no loop
        x = x - 1                                  # retirando um número da variável pois será usado na variável abaixo
        a = float(input('Digite o primeiro valor: '))   # inserção do primeiro valor registrado em uma variável isolada
        c = []                          # lista para receber os valores da variável b
        while x != 0:                   # loop de inserção dos valores
            b = float(input('Digite o próximo valor: '))            # inserção dos demais valores em uma variável
            x = x - 1                                       # subtrai um número do valor referência até terminar o loop
            c += [b]                               # insere o valor da variável inserida no loop na lista criada acima

# se o código for digitado corretamente no início o programa pula para cá
else:
    x = int(input('Quantos números quer calcular: '))   # definição de quantos números serão inseridos no loop
    x = x - 1                                           #retirando um número da variável pois será usado na variável abaixo
    a = float(input('Digite o primeiro valor: '))       # inserção do primeiro valor registrado em uma variável isolada
    c = []                                              # lista para receber os valores da variável b
    while x != 0:                                       # loop de inserção dos valores
        b = float(input('Digite o próximo valor: '))    # inserção dos demais valores em uma variável
        x = x - 1                                       # subtrai um número do valor referência até terminar o loop
        c += [b]                                        # insere o valor da variável inserida no loop na lista criada acima

float_lst = []                                          # Lista criada para guardar os itens da lista c no tipo str emformato float

for item in c:                                          # formatação de itens de str para float
    float_lst.append(float(item))

# condionais das operações
if op == 1:                             # condicional de soma
        soma = a                        # recebe o valor da primeira variável
        f = 0                           # variável para receber os valores da lista float
        for item in float_lst:          # loop para inserir os valores na variável f e fazer a operação soma
            f += item                   # recebe o valor e soma com o anterior
        soma += f                       # soma o valor inicial com o valor da soma dos demais valores fora do loop
        print('O Resultado da soma dos valores é igual a: ', soma)      # retorna o valor final para o usuário

elif op == 2:                          # condicional subtração
    sub = a
    f = 0
    for item in float_lst:
        f = item                       # recebe os demais valores da operação de modo indiviual
        sub -= f                       # faz a subtração do primeiro valor pelo valor da variável dentro do loop
    print('O Resultado da subtração dos valores é igual a: ', sub)      # retorna o valor final para o usuário

elif op == 3:                          # condicional multiplicação
    multi = a
    f = 0
    for item in float_lst:
        f = item                       # recebe os demais valores da operação de modo individual
        multi *= f                     # faz a multiplicação do valor inicial pelo valor da variável dentro do loop
    print('O Resultado da multiplicação dos valores é igual a: ', multi)      # retorna o valor final p/ o usuário

elif op == 4:                          # condicional divisão
    div = a
    f = 0
    for item in float_lst:
        f = item                    # recebe os demais valores da operação de modo individual
        dl = (div / f)              # faz a divisão do primeiro valor pelo valor da variável e o guarda na nova variável
        div = dl                    # guarda o valor parcial da divisão para retornar ao loop
    print('O Resultado da divisão dos valores é igual a: {:.2f}'.format(div))       #retorna o valor final da divisão


