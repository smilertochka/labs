def p1():
    from random import randint
    a = [randint(0, 50) for i in range(5)]
    b = int(input())
    if b in a:
        print(b, "Поздравляю, вы угадали число")
    else:
        print(b, "Нет такого числа")


def p2():
    from random import randint
    a = [randint(0, 10) for i in range(5)]
    b = [c for c in a if a.count(c) > 1]
    if len(b) < 1:
        print("Все числа уникальны")
    else:
        c = int(b[0])
        print(c, "Повторяющееся число", a.count(c), "Повторений")

def p3():
    a = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение")
    b = int(input("кол-во выходных"))
    for i in a:
        print("Рабочие", *a[:-b])
        print("Выходные", *a[-b:])
        break

def p4():
    group1 = ["Дюбарев", "Аленик", "Ковалев", "Дубовец", "Абадовский ", "Нуримов"]
    group2 = ["Бобков", "Русецкий", "Попов", "Иванов", "Самыгин ", "Поляков"]
    team = tuple(group1[:5] + group2[:5])
    print("Группа 1:", *group1)
    print("Группа 2:", *group2)
    print("Команда:", *team)
    print("Длина кортежа:", len(team))
    sorted_team = sorted(team)
    print("Команда (отсортирована по алфавиту):", *sorted_team)
    k = team.count("Иванов")
    if k > 0:
        print("Фамилия Иванов входит в команду. Встречается:", k, "раз(а)")
    else:
        print("Фамилия Иванов не входит в команду")
p4()



