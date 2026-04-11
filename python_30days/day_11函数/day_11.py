def add_all_numbers (*args):
    sum = 0
    for i in args :
        if i is int or i is float :
            sum += i
        else :
            print('something wrong with your datatype')
            return
    return sum
def captilize_list_items (list):
    for i in range(0,len(list)):
            list[i]=list[i].upper()
def is_solemn (list):
     new_set = set(list)
     if len(new_set)==len(list):
          return True
     else :
          return False
    