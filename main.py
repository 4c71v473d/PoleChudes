alph = 'А Б В Г Д Е Ё Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я'
words = {"ЖУПА": "Как у западных и южных славян назывались селение, деревня, курень?",
         "ПРАВДА": "Польский ученый-математик Гуго Дионисий Штейнгауз, прославившийся также своими афоризмами, говорил:"
                   "«Комплимент женщине должен быть правдивее, чем…",
         "ТЕЩА": "Если скорость ветра тропического шторма превышает 60 км/ч, ему присваивают личное имя."
                 "Во времена Второй мировой войны американские синоптики начали давать ураганам имена кого?",
         "ВОЙНА": "Какого слова нет в языке народов Арктики?",
         }
import random
import os

key = random.choice(list(words.keys()))
bukva = list(alph)
length = "-" * len(key)
wrong = 0
used = []
while length != key:
    print('╔══╦══╗╔══╦═══╗ ╔╗╔╦╗╔╗╔══╗╔═══╦══╗', )
    print('║╔╗║╔╗║║╔╗║╔══╝ ║║║║║║║║╔╗║║╔══╣╔═╝', )
    print('║║║║║║║║║║║╚══╗ ║╚╝║╚╝║║║║║║╚══╣║', )
    print('║║║║║║║║║║║╔══╝ ╚═╗╠═╗║║║║║║╔══╣║', )
    print('║║║║╚╝╠╝║║║╚══╗ ──║║╔╝╠╝╚╝╚╣╚══╣╚═╗', )
    print('╚╝╚╩══╩═╝╚╩═══╝ ──╚╝╚═╩════╩═══╩══╝')
    print("\nВопрос:\n\t", words[key])
    print("Вы уже предлагали следующие буквы: ", used)
    print("Отгаданное вами в слове сейчас выглядит так: ", length, "\n")
    guess = input("Введите букву: ")
    result = ''.join([a if (a.lower() not in guess) else '' for a in alph])
    print('Попробуйте буквы:', result)
    guess = guess.upper()
    while guess in used:
        print("Вы уже вводили букву ", guess)
        guess = input("Введите другую букву: ")
        guess = guess.upper()
    used.append(guess)

    if guess in key:
        print("Откройте букву ", guess, "!")
        new = ""
        for i in range(len(key)):
            if guess == key[i]:
                new += guess
            else:
                new += length[i]
        length = new
    else:
        print("К сожалению буквы ", guess, " нет в слове.")
        guess = input("Введите другую букву: ")
        guess = guess.upper()
    used.append(guess)
    os.system('cls')

print("Вы предлагали следующие буквы: ", used)
print("Отгаданное вами в слове выглядит так: ", length, "\n")
print("Было загадано слово ", key)
input("Нажмите Enter, чтобы выйти ;)")