# Створіть функцію def popularity(text) яка приймає текст text і повертає унікальний массив строк відсортований за популярністью.
#
# Уявіть що вам надсилають текст роману чи вірша і хочуть побачити найбільш популярні слова які зустрічаються у цьому тексті.
#
# Для початку ви повинні розбити текст на слова. Слова розділені звичайними пробілами.
# В тексті не будуть використовуватись точки або коми.
# Регістр слів не повинен мати значення. Тобто 'Apple' і 'aPPle' - одне слово.
# При формуванні результуючого массива слово повинно бути конвертовано в нижній регістр (lovercase).
# Сортування повинно бути виконано від найпопулярніших слів до найменш популярних.
# Якщо слова мають однакову популярність, сортування повинно бути виконано за абеткою.
# Приклади:
#
# popularity('apple kiwi pineapple kiwi apple kiwi') -> ['kiwi', 'apple', 'pineapple']
# popularity('aPPle pine Apple kiwi Apple kiwi') -> ['apple', 'kiwi', 'pine']
# popularity('aPPle pine Apple kiwi Apple kiwi') -> ['apple', 'kiwi', 'pine']
# popularity('aab aaa aac aab aac aaa x') -> ['aaa', 'aab', 'aac', 'x']
<<<<<<< HEAD


def popularity(text):
    Words = text.lower().split()
    dWords = dict()
    sortList = list()
    for word in Words:
        if word in dWords:
            dWords[word] = dWords[word] + 1
        else:
            dWords[word] = 1
    sorteddWords = dict(sorted(dWords.items(), key = lambda x: x[0]))
    sortedWords = sorted(sorteddWords.items(), key = lambda x: x[1], reverse=True)
    for word in sortedWords:
        sortList.append(word[0])
    return sortList


print(popularity('apple kiwi pineapple kiwi apple kiwi'))
print(popularity('aPPle pine Apple kiwi Apple kiwi'))
print(popularity('aPPle pine Apple kiwi Apple kiwi'))
print(popularity('aab aaa aac aab aac aaa x'))
=======
>>>>>>> 27d03deae5d520362921d55aeebd5ed86e0a712a
