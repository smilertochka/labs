words = []
while (word := str(input())) != "stop":
    words.append(word)
print(" ".join(words))


def p2():
    words = []
while (word := str(input())) != "stop":
    if "ф" in word or "Ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

def p3():
    from random import randint
    lose = 0
    win = 0
    while True:
        a = randint(1, 100)
        b = randint(1, 100)
        print(f"{a} + {b} = ", end="")
        res = input()
        while not res.isdigit() and res != "stop":
            print("что то пошло fне так, повторите ввод: ", end="")
            res = input()
        if res == "stop":
            break
        res = int(res)
        if a + b == res:
            win += 1
            print("правильно!")
            print(win)
        else:
            lose += 1
            print("Ответ неверный")
            print(lose)
        if lose == 3:
            print(f"Игра окончена правильных ответов:  {win}")
            break


p3()






