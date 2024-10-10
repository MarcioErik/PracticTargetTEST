entrada = str(input("Digite uma palavra: "))   ##Recebe a string
# A variável string_invertida recebe a variável entrada, que é tratada
# como lista e tem acesso a todos os caracteres, com -1 para percorrer de trás pra frente.
palavra_invertida = entrada[::-1]  
print(f"Palavra invertida: {palavra_invertida}")