company = 'Coding For All'
print(company)
print(company.upper())
print(company.lower(),company.capitalize(),company.title(),company.swapcase())
print(company[0])
print(company.index('Coding'),company.find('Coding'))
company = company.replace('Coding','Python')
print(company.split(' '))
companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(","))
print(''.join([i.capitalize()[0] for i in company.split(" ")]))
company = 'Coding For All'
print(company.index('C'))
print(company.rfind('l'))
sentence ='You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
print(' '.join(sentence.replace('because','').split()))
print (company.startswith('Coding'))
print(company.endswith('coding'))
print(' Coding For All '.strip(' '))
print(' '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFInland\tHelisinki')
