# FULL_NAME = input("Ismingizni kiriting: ")
# YEAR_OF_BIRTH = input("Tug'ulgan kun kiriting: ")
# YEAR_OF_BIRTH = int(YEAR_OF_BIRTH)

# CURRENT_YEAR = 2023

# age = CURRENT_YEAR - YEAR_OF_BIRTH

# natija = f"{FULL_NAME}ning yoshi: {age} " 

# print(natija)



# FULL_NAME = input("Ismingizni kiriting: ")
# SURE_NAME = input("Familiyangizni kiriting: ")
# SINF = input("sinf kiriting: ")
# SINF = int(SINF)

# YOSH = 7

# CURRENT_YEAR = 2023

# age = CURRENT_YEAR - (YOSH + SINF)

# natija = f"{SURE_NAME} {FULL_NAME}ning tugulgan yili: {age} "

# print(natija)



# FULL_NAME = "salom barchaga"

# print(FULL_NAME[::-1])



# FULL_NAME = "salom barchaga"

# soni = len(FULL_NAME)

# yulduzcha = "*"

# print(FULL_NAME)
# print(yulduzcha*soni)




# a = input("Son kiriting: ")
# b = input("Son kiriting: ")
# c = input("Son kiriting: ")

# son = int(a)
# son1 = int(b)
# son2 = int(c)

# if a < b < c:
#     print(f"Katta son {c}")
# elif a > b > c:
#     print(f"Katta son {a}")
# elif a < b > c:
#     print(f"Katta son {b}")
# elif a == b == c:
#     print(f"Uchachalasi teng {a} = {b} = {c}")
# elif a == b < c:
#     print(f"Katta son {c}")
# elif a > b == c:
#     print(f"Katta son {a}")
# elif b > a == c:
#     print(f"Katta son {b}")
# elif a < b == c:
#     print(f"Katta son {b}")
# elif a == c > b :
#     print(f"Katta son {a}")
# elif a == b > c :
#     print(f"Katta son {a}")
# else: 
#     print(f"Sonlarda hatolik bor")




# a = 50
# b = 500

# print(a) if a> b else print(b)



# text = "Salom dunyo men python man"

# for harf in text:
#     print(harf)



# sonlar = "0123456789"

# for raqam in range(0,10):
#     print(harf)




# sonlar = "0123456789"

# for raqam in range(1,10,2):
#     print(raqam)



# tanishlar = ["Sardor","Doniyor","Miraziz","Xabib"]
# ovqatlar = ["Brekfast: Osh", "Lunch: Osh", "Dinner: Osh"]

# for ism in tanishlar:
#     print(f"Salom {ism}")

# for ovqat in ovqatlar:
#     print(f"Eat {ovqat}")




# a = 2
# b = 5

# while a < b:
#     print(b)




# tanishlar = ["Sardor","Doniyor","Miraziz","Xabib"]

# sanagich = 0

# while sanagich < 4:
#     if tanishlar[sanagich] == "Miraziz":
#         print(f"Qanday {tanishlar[sanagich]}")

#     print(f"Salom {tanishlar[sanagich]}")

#     sanagich = sanagich + 1




# counter = 1

# while counter <= 5:
#     print(counter)

#     # counter = counter + 1
#     counter += 1




# if 5 > 2:
#    pass

# for raqam in range(1,10):
#     pass

    
# print("salom")





# for index in range(0, 10):
#     print(index)
#     if index == 3:
#         break




# for index in range(10):
#     if index % 2:
#         continue

#     print(index)





# a = input(f"son kiriting: ")
# b = input(f"son kiriting: ")

# son = int(a)
# son1 = int(b)

# if a > b:
#     print(a > b)
# elif a < b:
#     print(a < b)
# elif a == b:
#     print(a == b) 
# else:
#     print(f"Sonlarda hatolik bor")





# a = input(f"son kiriting: ")
# a = int(a)
# print(a*-1)




# son = input(f"Son kiriting: ")

# print(son[0])




# arqon_uzunligi = input(f"arqon uzunligini kiriting: ")
# bolaklar_uzunligi = input(f"bo'laklar uzunligini kiritinng: ")

# arqon_uzunligi = int(arqon_uzunligi)
# bolaklar_uzunligi = int(bolaklar_uzunligi)

# natija = arqon_uzunligi / bolaklar_uzunligi
# natija = int(natija)

# print(natija)

# def sum(a = 50, b = 80):
#     c = a + b
#     return c

# print(sum(140, 80))
# print(sum(100))
# print(sum())

# def salom_berish(ism = "Sardor"):
#     """Ism kiritish va unga salom berish"""
#     return f"Salom {ism}"

# print(salom_berish('Ali'))
# print(salom_berish.__doc__)




# def S(a,b):
#     return a * b

# print(S(10,11))


# def P(a,b):
#     return (a + b) * 2

# print(P(10,11))

# def sum(dev1 = 4, dev2 = 6,dern = 2 ,der1 = 2, der2 = 1.5,narx = 25):
#     return (dev1 * dev2 - dern*(der1*der2))*narx


# print(sum())




# def daraja(a=10,b=3):
#     return a**b

# print(daraja(a=5, b=4))




# def juft_toq(a):
#     if a % 2 == 0 :
#         return "bu son juft"
#     else:
#         return "bu son toq"
    
# print(juft_toq(7))




# for raqam in range(0,100,12):
#     print(raqam)




# for raqam in range(100):
#     if raqam % 6 == 0 and raqam %5 == 0:
#         print(raqam)





# oziq_ovqatlar = ["Non", "Tuxum", "Qazi", "Guruch", "Sabzi", "Go'sht", "Yog'"]

# birinchi_mahsulot = oziq_ovqatlar[0]
# yettinchi_mahsulot = oziq_ovqatlar[6]

# print(yettinchi_mahsulot)






# mevalar = ["2kg Olma","2kg Nok"]

# mevalar[0] = "2 ta Banan"
# mevalar.append("2 ta apelsin")
# mevalar.append("4 ta kivi")
# nimani_chopting = mevalar.pop(3)
# mevalar.remove("2kg Nok")
# mevalar.append(nimani_chopting)
# mevalar.insert(1, "4 ta Nok")

# del mevalar[0]

# print(mevalar)





# mevalar = ["nok", "olma", "banan"]

# miqdori = ["1kg", "2ta", "5ta"]

# result = []

# for i  in range(0, len(mevalar)):
#     result.append(miqdori[i] + " "+mevalar[i])
# print("Result", result)






# harflar = ["B","A","C"]
# sonlar = [10, 5, 20]

# harflar.sort()
# sonlar.sort()

# harflar.sort(reverse=True)
# sonlar.sort(reverse=True)

# saralangan_harflar = sorted(harflar)
# saralangan_sonlar = sorted(sonlar)

# # saralangan_harflar = sorted(harflar, reverse=True)
# # saralangan_sonlar = sorted(sonlar, reverse=True)

# print('Sort list: ', saralangan_harflar)
# print('Sort list: ', saralangan_sonlar)






# harflar = ["B","A","C","D","Z"]
# sonlar = [10, 5, 20, 40, 12, 25]

# print(harflar[2:4]) # ['C', 'D']
# print(sonlar[-5]) # 5

# print(harflar[::-1]) # ['Z', 'D', 'C', 'A', 'B']

# print(harflar[1:4:2]) # ['A', 'D']






# my_list = [1,2,3,100]

# print(my_list[0], end=" ")
# print(my_list[1], end=" ")
# print(my_list[2], end=" ")
# print(my_list[3])

# print(*my_list)






# my_list =[1,2,3]

# def my_sum(a,b,c):
#     return a + b + c


# # print(my_list(1,2,3))

# print(my_sum(my_list[0],my_list[1],my_list[2]))

# print(my_sum(*my_list))





# my_list = [1,2,3]

# def my_sum(*value):
#     return value

# print(my_sum(*my_list))






# my_list = [1,2,3,10,100]

# def my_sum(*value):
#     sum = 0
#     for ilemint in value:
#         # ilemint = ilemint + ilemint
#         sum += ilemint

#     return sum

# print(my_sum(*my_list))






# my_list = [1,2,3,4,5,6,7]

# index_raqami = my_list.index(5)

# print(index_raqami) # 4







# my_list = [1,2,3,4,5,6,7]

# # for i in my_list:
# #     print(i)

# birinchi_eliment = iter(my_list)
# ikkinchi_eliment = iter(my_list)


# print(next(birinchi_eliment)) # 1
# print(next(ikkinchi_eliment)) # 1






# my_list = [1,2,3,4,5,6,7]

# # for i in my_list:
# #     print(i)

# eliment = iter(my_list)



# print(next(eliment)) # 1
# print(next(eliment)) # 2
# print(next(eliment)) # 3







# my_list = [1,2,3,4,5,6,7,8,9]

# new_list = []

# for i in my_list:
#     new_list.append(i*2)

# print(new_list)





# my_list = [1,2,3,4,5,6,7,8,9]

# new_list = map(lambda i : i*2, my_list)

# print(list(new_list))


# print(list(map(lambda i : i*2, my_list)))






# my_list = [1,2,3,4,5,6,7,8,9]

# new_list = []

# for i in my_list:
#     if i > 5:
#         new_list.append(i)

# print(new_list)





# my_list = [1,2,3,4,5,6,7,8,9]

# new_list= filter(lambda i: i > 5, my_list)

# print(list(new_list))





# my_list = [1,2,3,4,5,6,7,8,9]

# print(list(filter(lambda i: i > 5, my_list)))







# from functools import reduce

# def sum(a, b):
#     print(f"a={a}, b={b}, {a} * {b} ={a*b}")
#     return a * b

# scores = [75, 65, 80, 95, 50]
# total = reduce(sum, scores)
# print(total)

# print(reduce(lambda a,b: a*b, scores))







# from functools import reduce

# scores = [75, 75]

# print(reduce(lambda a,b: a >= b, scores))







# numbers = [1, 2, 3, 4, 5]

# print([number**2 for number in numbers])

# #-----------------

# print(list(number**2 for number in numbers))








# for i in range(10):
#     for a in range(i + 1):
#         print("*", end="")
#     print()



# my_dict = {'foo': 'Yes', 'bazz': 'No','foo': 'Yeah', 'bazz': 'Nop',}

# # print(type(my_dict)) # <class 'dict'>


# # print(my_dict['foo']) # Yes
# # print(my_dict.get('foo')) # Yes 

# # del my_dict['bazz']
# # my_dict['foo'] = 'Nop'
# # my_dict.pop('foo')

# print(my_dict)








# person ={
#     "name":"sardor" ,
#     "age": 14,
#     "hobby" :"programming",
#     "job" :"programming"
# }

# for e in person:
#     lis = e
#     i = person.get(e)
#     print(list(lis,i))









# my_dict = {}

# my_set = set()

# print(type(my_dict)) # <class 'dict'>
# print(type(my_set))  # <class 'set'>






# a = 10
# b = 15

# if not a < b:
#     print("Ishladi")
# else:
#     print("Ishlamadi")





# a = 10
# b = 15

# if not a < b:
#     print("Ishladi")
# else:
#     print("Ishlamadi")

# if a != b:
#     print("Ishladi")
# else:
#     print("Ishlamadi")





# kasblar = {'Dasturchi','Dezayner','Loyiha menejeri'}

# print(type(kasblar)) # <class 'set'>
# print(len(kasblar)) # 3
# print('Dezayner' in kasblar) # True

# for i in kasblar:
#     print(i)







# kasblar = ('Dasturchi','Dezayner','Loyiha menejeri')

# # print(type(kasblar)) # <class 'tuple'>
# kasblar[1] = "O'quvchi"
# print(kasblar[1])






# kasblar = {'Dasturchi','Dezayner','Loyiha menejeri'}

# # kasblar.add('Testlovchi')
# # kasblar.remove('DevOps') # KeyError: 'DevOps'
# # kasblar.discard('DevOps') # Error not found!
# # kasblar.discard('Loyiha menejeri')

# # chopilgan_kasb = kasblar.pop()

# # kasblar.clear()


# print(kasblar)
# # print(chopilgan_kasb)






# kasblar = {'Dasturchi','Dezayner','Loyiha menejeri'}

# # kasblar.add('Testlovchi')
# # kasblar.remove('DevOps') # KeyError: 'DevOps'
# # kasblar.discard('DevOps') # Error not found!
# # kasblar.discard('Loyiha menejeri')

# # chopilgan_kasb = kasblar.pop()

# # kasblar.clear()


# print(kasblar)
# # print(chopilgan_kasb)







# skills = {'Problem solving', 'Software design', 'Python programming'}

# for index, skill in enumerate(skills, 1):
#     print(f"{index}.{skill}")


# # print(enumerate(skills)) # <enumerate object at 0x00000239AA6A5350>








# skills = {'Problem solving', 'Software design', 'Python programming'}

# for index, skill in enumerate(skills):
#     print(f"{index}.{skill}")


# # print(enumerate(skills)) # <enumerate object at 0x00000239AA6A5350>






# skills = {'Problem solving', 'Software design', 'Python programming'}

# skills = frozenset(skills)

# skills.add('DevOps') # AttributeError: 'frozenset' object has no attribute 'add'









# tags = {'Django', 'Pandas', 'Numpy'}
# new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}

# print(new_tags)








# people = [{'name': 'John', 'age': 25},
#         {'name': 'Jane', 'age': 22},
#         {'name': 'Peter', 'age': 30},
#         {'name': 'Jenifer', 'age': 28}]

# name = input('Enter a name:')

# found = False
# for person in people:
#     if person['name'] == name:
#         found = True
#         print(person)
#         break

# if not found:
#     print(f'{name} not found!')








# people = [{'name': 'John', 'age': 25},
#         {'name': 'Jane', 'age': 22},
#         {'name': 'Peter', 'age': 30},
#         {'name': 'Jenifer', 'age': 28}]

# name = input('Enter a name:')

# for person in people:
#     if person['name'] == name:
#         print(person)
#         break
# else:
#     print(f'{name} not found!')







# from functools import partial

# def multiply(a, b):
#     return a*b


# double = partial(multiply, b=2)

# result = double(10)

# print(result)








# from functools import partial

# def multiply(a, b):
#     return a*b


# double = partial(multiply, b=2)

# result = double(10, b=3)

# print(result)








# def say_hi(name: str) -> str:
#     return f'Hi {name}'


# greeting = say_hi('John')

# print(greeting)







# def sum(a:int,b:int)->int:
#     return a + b

# print(sum(1.2,2))








# def sum(a,b):
#     return a+b

# print(sum(1,))



# import app

# print(app.text)



    


# print("Men avvaldan borman")
# import app






# import app

# print(app.salomlash("Sardor")) 
# print(app.sum(10,15))







# import app

# from app import salomlash, sum

# print(salomlash("Sardor")) 
# print(sum(10,15))








# import app

# from app import salomlash_kim_bilandir as salomlash

# print(salomlash("Sardor")) 
# print(sum(10,15))







# import sys

# for path in sys.path:
#     print(path)







# import app

# print(__name__)







# import app


# def main():
#     print(app.sum(15,20))

# if __name__ == app.__name__:
#     main()
# else:
#     print(app.__name__)






