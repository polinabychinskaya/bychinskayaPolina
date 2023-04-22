#Exercise 1
a = "Не знаю, как там в Лондоне, я не была. Может, там собака — друг человека. А у нас управдом — друг человека!"
characters = len(a)
print ("Количество символов: " + str(characters))


#Exercise 2
b = "Python yes"
print ("Развернуть строку: " + b [::-1])


#Exercise 3
c = a.title()
print ("Сделать каждое слово с большой буквы: " + c)


#Exercise 4
d = a.upper()
print ("Сделать весь текст прописными буквами: " + d)


#Exercise 5
value_count_1 = a.count('нд')
value_count_2 = a.count('ам')
value_count_3 = a.count('о')
answer = "Найти число вхождений 'нд', 'ам', 'о' в строку: \n"\
    "a) Количество 'нд': "\
    + str(value_count_1)\
    + "\nb) Количество 'ам': "\
    + str(value_count_2)\
    + "\nc) Количество 'о': "\
    + str(value_count_3)
print (answer)


#My exercises
j = "SpongeBob SquarePants lives in Bikini Bottom"
print ("--------------------------------------------------------")
print (j.casefold())
print (j.endswith("tom"))
print (j.find("B"))
print (j.islower())
h = j.maketrans("B", "M")
print (j.translate(h))
print (j.swapcase())
print ("--------------------------------------------------------")


#Exercise 6
e = "Я Денис"
f = e[2:7] + " " + e[0]
print ("Развернуть предложение: " + f)


#Exercise 7
print("Вывести в консоль исходную строку: " + a)
