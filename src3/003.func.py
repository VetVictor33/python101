def print_nice_title(content, length):
    print('-'*length)
    print(f'{content:^{length}}')
    print('-'*length)

print_nice_title('Vamo que vamo', 30)

##packing params
def python_is_packing(*n):
    print(n)

python_is_packing(1, 2, 3, 4, 5)

python_is_packing('então', 'vc', 'cria', 'uma', 'tupla', '?')

def double_my_list(my_list):
    for index, item in enumerate(my_list):
        my_list[index] *= 2
    return my_list

my_list = [1, 2, 3]
print(my_list)
print(double_my_list(my_list))
print(my_list)