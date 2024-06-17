
# numero = int(input("Digite um número: "))
# if numero % 2 == 0:
#     print("O número é par")
# else:
#     print("O número é ímpar")

# idade = int(input("Digite sua idade: "))

# if 0 < idade < 12:
#     print("Criança")
# elif 13 < idade <  18:
#     print("Adolescente")
# else:
#     print("Adulto")

# usuario = input("Digite seu usuário: ")
# senha = int(input("Digite sua senha: "))

# usuario_correto = "admin"
# senha_correta = 123

# if usuario == usuario_correto and senha == senha_correta:
#     print("Usuário autenticado")
# else:
#     print("Usuário ou senha inválidos")

x = int(input("Digite as codernadas x: "))
y = int(input("Digite as codernadas y: "))

if x and y > 0:
    print("Primeiro quadrante")
elif x < 0 and y > 0:
    print("Segundo quadrante")
elif x < 0 and y < 0:
    print("Terceiro quadrante")
elif x > 0 and y < 0:
    print("Quarto quadrante")
else:
    print('o ponto está localizado no eixo ou origem.')
