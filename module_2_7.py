def print_params(a=1, b='погода', c=True):
    print(a, b, c)


print_params()
print_params(a=1, b = 25, c = [1,2,3])
values_list = [3, 'слово', 2.5]
values_dict = {'a': True, 'b': 4, 'c': 'sun'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [2.5, 'lite']
print_params(*values_list_2, 42)
