#Crie um programa que calcule o fatorial de um número inteiro positivo digitado pelo usuário.

#Passos:

#Peça ao usuário para digitar um número inteiro positivo.
#Utilize um loop for para calcular o fatorial desse número.
#Imprima o resultado.

# Solicita ao usuário que digite um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))

# Inicializa a variável fatorial com 1
fatorial = 1

# Utilize um loop for para calcular o fatorial
for i in range(1, numero + 1):  # Itera de 1 até o número fornecido pelo usuário
    fatorial *= i  # Multiplica a variável fatorial pelo número atual i

# Imprime o resultado final
print(f"O fatorial de {numero} é {fatorial}.")

