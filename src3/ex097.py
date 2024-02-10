def print_nice_title(content):
    length = len(content) * 2
    print('-'*length)
    print(f'{content:^{length}}')
    print('-'*length)

print_nice_title(input('O que você quer digitar? '))