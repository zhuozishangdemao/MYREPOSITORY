class Statistics:
    def __init__(self, data=[]):
        self.data = data

    def count(self):
        # 你自己的实现
        return len(self.data)
        pass
    
    def sum(self):
        # 你自己的实现
        sum = 0
        for i in self.data :
            sum+=i
        self.sum = sum
        return sum
        pass
    
    def min(self):
        # 你自己的实现
        mini = self.data[0]
        for i in self.data :
            mini = min(mini,i)
        self.min = mini
        return mini
        pass
    
    def max(self):
        # 你自己的实现
        pass
    
    def range(self):
        # 你自己的实现
        pass
    
    def mean(self):
        # 你自己的实现
        pass
    
    def median(self):
        # 你自己的实现
        pass
    
    def mode(self):
        # 你自己的实现
        pass
    
    def standard_deviation(self):
        # 你自己的实现
        pass
    
    def variance(self):
        # 你自己的实现
        pass
    
    def frequency_distribution(self):
        # 你自己的实现
        pass
    
    def describe(self):
        # 你自己的实现
        pass
class PersonAcount :
    def __init__(self,firstname,lastname) :
        self.firstname = firstname
        self.lastname  = lastname
        self.remain = 0
    def record_spend(self,income):
        self.remain +=income
        print(f'already record {income} dollars')
    def show_remain(self):
        print(f'you only have {self.remain} now!')
Myaccount = PersonAcount('zhuozi','shangdemao')
Myaccount.record_spend(230)
Myaccount.show_remain()
class product_lsit :
    def __init__(self,*args,**kwargs):
        self.product_list = args
        self.key_list = [i for i in kwargs]
        self.dictionry = kwargs
    def show_prodcut_list (self):
        print(self.product_list)
    def show_dictionary(self):
        print(self.dictionry)
    def show_key_list(self):
        print(self.key_list)
my_products_list = product_lsit("apple", "banana", "orange", vegetable="tomato", juice="orange")
my_products_list.show_key_list()
my_products_list.show_dictionary()
my_products_list.show_prodcut_list()