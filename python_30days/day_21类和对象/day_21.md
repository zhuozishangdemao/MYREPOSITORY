## 类和对象
### 类和对象的定义
类是对象构造器，我们实例化一个类来创建一个对象。类定义了对象的属性和行为，而对象代表类
### 类的操作方法
#### 创建类
```py
class 类名：
    代码
```
#### 创建对象
```py
class person:
    pass
p = person()
print(p)
```
#### 类构造函数
python内置__init__构造函数
```py
class Person:
    def __init__(self,firstname,lastname,age,country,city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
p.firstname
```
#### 对象方法
对象可以有方法，方法是对象的函数：要通过对象来调用函数
```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```
#### 对象默认方法
与函数一样，有时候我们可能无参数的调用类生成对象，为了防止生成错误，我们可以为类的定义增加默认值。
```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```
#### 修改对象默认值的方法
可以通过对象函数来修改实例化默认参数
```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []#这些参数在创建的时候默认，除了在调用类方法生成对象输入参数的时候修改，还可以通过修改对象默认值的方法修改

      def person_info(self):
        return f'{self.firstname} {self.lastname}今年{self.age}岁。他住在{self.country}的{self.city}。'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```
#### 继承
允许我们定义一个继承父类所有功能的函数
```py
class 子类名（父类名）：
    代码
class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)
print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)#父类的定义和操作函数都可以使用
```
#### 子类增加定义和操作函数
如果不使用super().__init__(name,..父类的定义)
1. 在子类中定义__init__会完全覆盖父类的定义
2. 在子类中不定义__init__:无影响，直接使用父类定义
如果使用super().__init__方法：  
在子类中定义的__init__会**后**于父类的__init__调用