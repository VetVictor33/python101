from time import sleep

def count(begin, end, step):
    current = begin
    step = step if step > 0 else 1
    condition = lambda current, end : current < end + 1
    if begin > end and step > 0:
        condition = lambda current, end : current > end - 1
        step *= -1
    elif begin < end and step < 0:
        step *= -1
    while condition(current, end):
        print(f'{current}', end=', ', flush=True)
        sleep(0.5)
        current += step
    print('FIM!')

print('-='* 30)
print('Contanto de 0 a 5')
count(0, 5, 1)
print('-='* 30)
print('Contanto de 5 a 0')
count(5, 0, 1)
print('-='* 30)

print('-='* 30)
print(f'{"Agora é com você, aprendiz!":^60}')
print('-='* 30)

begin = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

count(begin, end, step)