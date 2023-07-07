# ism = input("Ismingiz nima: ")

# familiya = input("familiyangiz nima: ")

# # nateja = "Salom"+ " " + familiya + " " + ism
# nateja = f"Salom {familiya} {ism}"

# print(nateja)

# foo = "Laa"
# baz = "Bla"
# look = 2.2

# turi = type(look)
# type funksiyasi malumotni turini aniqlaydi


# print(turi)






# text = "Salom"







# print("Men keldim")










# def salomlash_kim_bilandir(ismi):
#     return(f"Salom {ismi}")


# def sum(a,b):
#     return a + b








# print(__name__)







# def sum(a,b):
#     return a + b






# with open('./demo.txt', 'wt') as f:
#     f.write("Hello world 2!")






# ismi = input("Ismingiz nima: ")
# familiyasi = input("familiyangiz nima: ")

# with open('./demo.txt', 'at') as f:
#     f.write(f"{ismi} {familiyasi}")






# login = input("Login: ")
# password = input("Password: ")

# with open("./demo.txt", "rt") as f:
#     # user_data = (f.readline()[:-1], f.readline())
#     user_data = []
#     user_data.append(f.readline()[:-1])
#     user_data.append(f.readline())
    
#     if login == user_data[0] and password == user_data[1]:
#         print("Welcome!")
#     else:
#         print("UYGA BOR!")
#     # print(user_data)





# words_count = int(input("Words count: "))

# count = 1
# while count <= words_count :
#     word = input(f"{count} Word: ")

#     with open("./emo.txt", "at") as f:
#         f.write(word)
#         f.write("\n")

#     count += 1


# with open("./emo.txt", "rt") as f:
#     result = f.read()
#     print(result)




# import os

# print(os.getcwd())

# Summary
# Use the os.getcwd() function to get the current working directory.
# Use the os.chdir() function to change the current working directory to a new one.
# Use the os.mkdir() function to make a new directory.
# Use the os.rename() function to rename a directory.
# Use the os.rmdir() function to remove a directory.
# Use the os.walk() function to list the contents of a directory.


# img = image.open("python.jpg")

# print(img.format, img.size,img.mode)
# new_100_100 = img.resize((100,100))
# new_100_100.save("100_100.mp4")








# class Inson:
#     pass

# print(Inson) # <class '__main__.Inson'>
# print(__name__) # __main_







# class Inson:
#     x = 12

# print(Inson.x) # 12
# print(Inson.__name__) # <class '__main__.Inson'>
# print(type(Inson)) # <class 'type'>







# class Inson:
#     inson_nomi = "Sardor"
#     inson_yoshi = 14

# print(Inson.inson_nomi)
# print(Inson.inson_yoshi)

#--------------------

# class Inson:
#     inson_nomi = ""
#     inson_yoshi = 0

# print(Inson.inson_nomi)
# print(Inson.inson_yoshi)








# class Inson:
#     def __init__(self,nomi,yoshi):
#         self.nomi = nomi
#         self.yoshi = yoshi
    
#     def salomlash(self):
#         return f"Salom {self.nomi}"
    
#     def yoshini_oshir(self):
#         return self.yoshi + 1
    
#     def yoshini_aniqla(self):
#         if self.yoshi < 18:
#             return f"{self.nomi} siz hali yoshsiz!"
#         else:
#             return f"{self.nomi} siz ro'yxatdan o'tdingiz!"
    
#     def nomini_alishtir(self, yangi_nomi):
#         self.nomi = yangi_nomi
#         return yangi_nomi
    


# Sardor = Inson("Sardor", 19)
# Umid = Inson("Umid", 22)

# print(Sardor.nomini_alishtir("Sarik"))
# print(Sardor.salomlash())


# print(Sardor.salomlash())
# print(Sardor.yoshini_oshir())
# print(Sardor.yoshini_aniqla())

# print(Umid.salomlash())
# print(Umid.yoshini_oshir())




# a = input("Son kiriting: ")
# b = input("Son kiriting: ")
# a = int(a)
# b = int(b)


# class Calc:
#     def __init__(self, a,b) -> None:
#         self.a = a
#         self.b = b

#     def yigindi(self):
#         return self.a + self.b

#     def ayerish(self):
#         return self.a - self.b

#     def kupaytma(self):
#         return self.a * self.b

#     def bulish(self):
#         return self.a / self.b
    
# print(Calc.yigindi())
# print(Calc.ayerish())
# print(Calc.kupaytma())
# print(Calc.bulish())






# class Inson:
#     nomi = "Ali"
#     yoshi = 22

# # print(Inson.nomi)
# # print(Inson.yoshi)

# print(getattr(Inson, 'nomi'))
# print(getattr(Inson, "yoshi"))








# class Inson:
#     nomi = "Ali"
#     yoshi = 22

# # Inson.nomi = "Sardor"
# # setattr(Inson, 'nomi', 'Umid')
# # delattr(Inson,"nomi")
# del Inson.nomi


# print(Inson.nomi)







# class Request:
#     def send():
#         print('Sent')

# # Request.send()
# http_request = Request()
# # print(http_request.send)
# print(type(Request.send) is type(http_request.send)) # False








# class Request:
#     def send(self):
#         print(self)


# Request.send("SALOM")






# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def get_name(self):
#         return self.name

# if __name__ == '__main__':
#     person = Person('John', 25)
#     print(f"I'm {person.get_name()}. I'm {person.age} years old.")
#     print(f"I'm {person.name}. I'm {person.age} years old.")









# from my import Calc
# a = input("Birinchi soni kiriting: ")
# b = input("Ikkinchi son kiriting: ")
# a = int(a)
# b = int(b) 

# if __name__ == '__main__':
#     my_calc = Calc(a,b)

#     print(f"a + b = {my_calc.sum()}")
#     print(f"a - b = {my_calc.divergence()}")
#     print(f"a * b = {my_calc.multiplication()}")
#     print(f"a / b = {my_calc.division()}")
#     print(f"a % b = {my_calc.residual_blanking()}")
#     print(f"a ** b = {my_calc.upgrade()}")
#     print(f"a ** (1/b) = {my_calc.ildiz()}")







# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def get_name(self):
#         return self.name

# if __name__ == '__main__':
#     person = Person('John', 25)
#     print(f"I'm {person.get_name()}. I'm {person.age} years old.")
#     print(f"I'm {person.name}. I'm {person.age} years old.")









# class Inson:
#     def __init__(self, nomi,yoshi) -> None:
#         self.nomi = nomi
#         self.yoshi = yoshi
#         self._laqabi = 'Sarik'


# insoncha = Inson("Sardor",15)

# insoncha.yoshi = 17 # ✅
# insoncha._laqabi = "Sancho" # ❌w

# print(insoncha.nomi)
# print(insoncha.yoshi)
# print(insoncha._laqabi)









# class Sum:
#     x = 12

#     def __init__(self, y) -> None:
#         self.y = y

#     def result(self):
#         return self.x + self.y
    
# sum = Sum(12)

# print(sum.result())









# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     # def __str__(self):
#     #     return f'Person({self.first_name},{self.last_name},{self.age})'

#     def __repr__(self):
#         return f'Person({self.first_name},{self.last_name},{self.age})'
    
# personcha = Person("Ali","Valiyev",25)

# print(personcha) # Person(Ali,Valiyev,25)








# class Inson:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):
#         return isinstance(other,Inson)  and self.age == other.age
    

# jhone = Person("Jhone",25)
# jane = Person("Jane",25)

# print(jhone == jane) # False









# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self._age = age

#     @property
#     def age(self):
#         return self._age

#     def __eq__(self, other):
#         return isinstance(other, Person) and self.age == other.age

#     def __hash__(self):
#         return hash(self.age)
    
# jhone = Person("Jhone",25)
# jane = Person("Jane",25)

# # print(hash(Person))

# print(hash(jhone))
# print(hash(jane))











# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __bool__(self):
#         if self.age < 18 or self.age > 65:
#             return False
#         return True


# if __name__ == '__main__':
#     person = Person('Jane', 16)
#     print(bool(person))  # False








# class Payroll:
#     def __init__(self, length):
#         self.length = length

#     def __len__(self):
#         print('len was called...')
#         return self.length


# if __name__ == '__main__':
#     payroll = Payroll(0)
#     print(bool(payroll))  # False
#     print(payroll.__len__())

#     payroll.length = 10
#     print(bool(payroll))  # True
#     print(payroll.__len__())









# def base_func(lst):
#     new_list = []
#     for i in lst:
#         new_list.append(i+1)
#     return new_list

    
    
    
# print(base_func([1,2,3]))










