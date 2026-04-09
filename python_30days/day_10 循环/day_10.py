for i in range (11) :
    print(f'{i}X{i}={i*i}')
def reverse (list):
    new_list = []
    for item in list[::-1] :
        new_list.append(item)
    return new_list
fruits = ['banana','apple','orange']
fruits = reverse(fruits)
print(fruits)