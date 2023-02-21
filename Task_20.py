# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. Напишите программу, которая вычисляет стоимость
# введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

def convert_and_check_word(wd):
    up_word = wd.upper()
    rus_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф",
                   "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
    eng_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z']
    rul_rus = all([i in rus_letters for i in up_word.lower()])
    rul_eng = all([i in eng_letters for i in up_word.lower()])
    rul = True if rul_rus or rul_eng else False
    return up_word, rul_rus, rul_eng, rul


def count_points(dic_en, dic_ru, tup):
    s = 0
    if not tup[3]:
        print("Слово должно состоять только из букв одного алфавита!")
        exit()
    elif tup[1]:
        for i in tup[0]:
            if i in dic_ru.keys():
                s += dic_ru[i]
    else:
        for i in tup[0]:
            if i in dic_en.keys():
                s += dic_en[i]
    return s


dict1 = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
         'D': 2, 'G': 2,
         'B': 3, 'C': 3, 'M': 3, 'P': 3,
         'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
         'K': 5,
         'J': 8, 'X': 8,
         'Q': 10, 'Z': 10}

dict2 = {'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
         'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
         'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 2,
         'Й': 4, 'Ы': 4,
         'Ж': 5, 'З': 2, 'Х': 2, 'Ц': 2, 'Ч': 2,
         'Ш': 8, 'Э': 8, 'Ю': 2,
         'Ф': 10, 'Щ': 10, 'Ъ': 2, }

word = input("Введите слово, только на русском или английскоям языке: ")

collect = convert_and_check_word(word)

print(f"Загадав слово \"{word}\" вы набрали {count_points(dict1, dict2, collect)} очков")