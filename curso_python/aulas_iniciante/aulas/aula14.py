# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print('Seja bem vindo!')
elif entrada == 'sair':
    print('Você saiu do sistema')
    print('Até logo!')
else:
    print('Você não digitou nem entrar e nem sair.')
    print('Escolha a opção correta!')