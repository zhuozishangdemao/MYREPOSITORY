age = int (input())
if age > 30:
    print ('old guys ')
else :
    print(f'you are only {age},way too young')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruits = str(input())
if str in fruits:
    print(f'already in {fruits}')
else:
    fruits.append(new_fruits)
    print(f'I ve already add it to the {fruits}')