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
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': '芬兰',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': '太空街',
        'zipcode': '02210'
    }
}
if person.get('skills') :
    print(person['skills'])
    if 'Python' in person['skills'] :
        print ('talented')
    