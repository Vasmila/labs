'задание 1'
def p1():
    N = int(input("Введите количество слов: "))
    a = 0
    s = ""
    while a < N:
        s += (input("Введите слово: ")) + " "
        a += 1
    print(s)

def p2():
 'задание 2'
 s = []
 word = str(input())
 while word != "stop":
  s.append(word)
  word = str(input())

 print(" ".join(s))

def p3():
 'задание 3'
 s = []
 while (word := str(input())) != "stop":
  if "Ф" in word or "ф" in word:
   print("Ого! Это редкое слово!")
  else:
   print("Эх, это не очень редкое слово...")

def p4():
 'задание 4'
 from random import randint
 ko = 0
 k = 0
 while ko < 3:
     a = randint(1, 100)
     b = randint(1, 100)
     print(f"{a} + {b} =", end=" ")
     res = input()
     while not res.isdigit() and res != "stop":
         print("Ошибка. Введите заново.")
         res = input()
     if res == "stop":
         break
     elif int(res) == (a + b):
         print("Правильно!")
         k += 1
     else:
         print("Неправильно!")
         ko += 1

 print("Игра окончена! Правильных ответов: ", k)

p1()
p2()
p3()
p4()
