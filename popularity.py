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

def popularity(text):
    if not(isinstance(text, str)):
        return 'Введіть рядок'
    text = text.strip()
    if (len(text) == 0):
        return 'Аргумент не вказаний'
    listWords = text.lower().split()
    dictWords = dict()
    sortedList = list()
    for word in listWords:
        if word in dictWords:
            dictWords[word] = dictWords[word] + 1
        else:
            dictWords[word] = 1
    sortedDictWords = dict(sorted(dictWords.items(), key = lambda x: x[0]))
    sortedListWords = sorted(sortedDictWords.items(), key = lambda x: x[1], reverse=True)
    for word in sortedListWords:
        sortedList.append(word[0])
    return sortedList

print(popularity('apple kiwi pineapple kiwi apple kiwi'))
print(popularity('123213421414'))
print(popularity('aPPle pine Apple kiwi Apple kiwi'))
print(popularity('aab aaa aac aab aac aaa x'))
