numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_list = [_ for _ in numbers if _>0]
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_flattened = [_ for lists in list_of_lists for _ in lists[0] ]
print(list_flattened)
exp_list = [(x**1,x**0,x**1,x**2,x**3,x**4) for x in range(0,9)]
print(exp_list)
countries = [[('芬兰', '赫尔辛基')], [('瑞典', '斯德哥尔摩')], [('挪威', '奥斯陆')]]
countries_dictionary = [{'国家': lists[0][0],'城市':lists[0][1]}for lists in countries ]
print(countries_dictionary)