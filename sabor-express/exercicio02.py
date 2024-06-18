# pessoa = {'nome': 'Felipe', 'idade': 30, 'cidade': 'São Paulo'}
# # Atualização de Idade
# pessoa['idade'] = 31

# # Adicionando Profissão
# pessoa['profissao'] = 'Engenheiro'

# # Remoção de Elemento
# del pessoa['cidade']

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print('O nome da pessoa é:', pessoa['nome'])
else:
    print('O nome da pessoa não foi encontrado')