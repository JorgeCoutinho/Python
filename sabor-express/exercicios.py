# num = [0,1,2,3,4,5,6,7,8,9,10]
# nomes = ['mikael', 'jorge', 'couto', 'alves']
# data = [1999, 2024]
# print(num)
# print(nomes)
# print(data)
# - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
# lista_numero = [0,1,2,3,4,5,6,7,8,9,10]
# for numeros in lista_numero:
#     print(numeros)

# Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
# soma_impares = 0
# for i in range(1, 11, 2): # 
#     soma_impares += i
# print(soma_impares)

# Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
# for i in range(10, 0, -1):
#     print(i)

# Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# num = int(input('Digite um número: '))
# for i in range(1, 11):
#     print(f'{num} x {i} = {num * i}')

# Crie uma lista de números e utilize um loop for para calcular a soma de 
# todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# lista_numero = [0,1,2,3,4,5,6,7,8,9,10]
# soma = 0

# try:
#     for numero in lista_numero:
#         soma += numero
#     print(soma)
# except Exception as e:
#     print('Erro:', e)


# lista_valores = [15, 20, 25, 30]
# soma_valores = 0

# try:
#     for valor in lista_valores:
#         soma_valores += valor
#     media = soma_valores / len(lista_valores)
#     print(f"Média dos valores: {media}")
# except ZeroDivisionError:
#     print("A lista está vazia, não é possível calcular a média.")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")