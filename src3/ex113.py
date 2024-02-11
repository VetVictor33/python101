while True:
    try:
        n = int(input('Digite um número: '))
        print(f'Você digitou {n}, parabéns!')
        break
    except ValueError:
        print('Número inválido')
    except KeyboardInterrupt:
        print('Tchau!')
        break
    except Exception as error:
        print(error.__class__)

print('Obrigado, volte sempre')