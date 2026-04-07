# 集合
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
it_companies_lst = ['deepseek','Grok']
it_companies.update(it_companies)
print(it_companies)
it_companies.discard('Grok')
C = A.union(B)
D = A.intersection(B)
A.issubset(B)
print(A.issubset(B) or A.issupperset(B))
print(A.symmetric_difference(B))
del A 
del B
sentence ='I am a teacher,I like to inspire and instruct people.'
claeaned = sentence.replace(',','').replace(',',' ').split()
set_sentence = set(claeaned)
print(set_sentence)