print("Bem-vindo ao MyCalculator\n")
print("[MENU] -> Selecione uma das operações abaixo:")
print("[1] Adição")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
print("[5] Potência")
print("[6] Raiz Quadrada")
print("[7] Porcentagem")
print("[8] Fatorial")
print("[9] Ajuda")
print("[0] Sair\n")

opcao = ""
while(opcao != 0): # Condição de parada do loop
    opcao = int(input("OPERAÇÃO: "))
    if(opcao == 1): # Calcula a adição
        print("\n[ADIÇÃO]")
        numeros = str(input("Digite os números que deseja somar: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        soma = 0 # inicia a variável de soma com o elemento neutro
        for numero in lista_valores: # realiza iteração para cada número presenta na lista
            soma += int(numero) # realiza a adição com os números, convertendo cada um para inteiro
        print(f"Resultado: {soma}\n")
        
    if(opcao == 2):
        print("\n[SUBTRAÇÃO]") # Calcula a subtração
        numeros = str(input("Digite os números que deseja subtrair: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        subtracao = int(lista_valores[0]) # inicia a variável de subtração com o primeiro valor que foi digitado
        for i in range(1, len(lista_valores)): # realiza a iteração a partir do segundo valor presente na lista
            subtracao -= int(lista_valores[i]) # realiza a subtração com os números, convertendo cada um para inteiro
        print(f"Resultado: {subtracao}\n")
        
    if(opcao == 3): # Calcula a multiplicação
        print("\n[MULTIPLICAÇÃO]")
        numeros = str(input("Digite os números que deseja multiplicar: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        multiplicacao = 1 # inicia a variável de multiplicação com o elemento neutro
        for numero in lista_valores: # realiza iteração para cada número presenta na lista
            multiplicacao *= int(numero) # realiza a multiplicação com os números, convertendo cada um para inteiro
        print(f"Resultado: {multiplicacao}\n")

    if(opcao == 4): # Calcula a divisão
        print("\n[DIVISÃO]")
        numeros = str(input("Digite os dois valores que deseja calcular a divisão: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        if(int(lista_valores[1]) == 0): # verifica se o segundo valor passado é zero
           print("Impossível realizar divisão por zero. Tente novamente.") # se sim, exibe a mensagem e encerra a operação
        else: # se não...
            divisao = int(lista_valores[0]) // int(lista_valores[1]) # realiza a divisão
            resto = int(lista_valores[0]) % int(lista_valores[1]) # calcula o resto da divisão
            print(f"Resultado: {divisao} | Resto: {resto}\n")

    if(opcao == 5): # Calcula a potência
        print("\n[POTÊNCIA]")
        numeros = str(input("Digite a base e o expoente que deseja utilizar para o cálculo: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        potencia = int(lista_valores[0]) ** int(lista_valores[1]) # realiza a potenciação
        print(f"Resultado: {potencia}\n")

    if(opcao == 6): # Calcula a raiz quadrada
        print("\n[RAIZ QUADRADA]")
        numeros = str(input("Digite os valores que deseja calcular a raiz quadrada: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        lista_raizes = [] # cria uma lista vazia para armazenar os valores das raízes
        for numero in lista_valores: # realiza iteração para cada número presenta na lista
            lista_raizes.append(int(numero) ** (1/2)) # calcula a raíz quadrada de cada número e armazena na lista criada anteriormente
        for i in range (len(lista_valores)): # realiza iteração sobre a lista que contém as raízes
            print(f"A raiz quadrada de {lista_valores[i]} é {lista_raizes[i]}.") # exibe a raíz quadrada de cada valor inicial
        print("\n")

    if(opcao == 7): # Calcula porcentagem
        print("\n[PORCENTAGEM")
        numeros = str(input("Digite o percentual e o valor a ser calculado: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        resultado = (int(lista_valores[0])/100) * int(lista_valores[1]) # calcula a porcentagem
        print(f"Resultado: {lista_valores[0]}% de {lista_valores[1]} é igual a {resultado}.\n") # exibe o resultado

    if(opcao == 8): # Calcula fatorial
        print("\n[FATORIAL]")
        numeros = str(input("Digite os fatoriais que deseja calcular: ")) # Pede informações via teclado
        lista_valores = list(numeros.split(" ")) # Cria uma lista com os valores excluindo os espaços entre eles
        lista_fatoriais = [] # cria uma lista vazia para armazenar o resultado fatorial de cada número passado
        for numero in lista_valores: # realiza iteração para cada número passado
            fatorial = 1 # inicial a variável com o elemento neutro
            for i in range(int(numero), 1, -1): # loop que se inicia do número passado e vai decrescendo até chegar a 1
                fatorial *= i # calcula o fatorial
            lista_fatoriais.append(fatorial) # guarda o cálculo realizado
        for i in range (len(lista_valores)): # realiza iteração sobre a lista que contém as raízes
            print(f"O fatorial de {lista_valores[i]} é {lista_fatoriais[i]}.") # exibe o fatorial de cada valor inicial
        print("\n")
        
    if(opcao == 9): # Exibe as informações de ajuda
        print("\n[AJUDA]")
        print("1 - Para as operações que recebem mais de um valor, estes valores precisam ser digitados de maneira separada por espaço.")
        print("2 - Para encerracar o MyCalculator, digite 0 (zero) quando for pedida a operação a ser realizada.")
        print("3 - Uma vez selecionada a operação que deseja realizar, digite os valores pedidos e aguarde o resultado. Após isto, você poderá selecionar uma nova operação.")
        print("\n")

    if(opcao == 0): # Exibe a mensagem de despedida
        print("\nAté logo (: ")
