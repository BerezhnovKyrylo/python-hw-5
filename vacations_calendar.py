# Створіть модуль vacations_calendar який повинен містити глобально обʼявлену змінну зі списком всіх українських державних свят (дати і назва).
# Повинен бути створений модуль vacations_calendar. Технічно це файл vacations_calendar.py.
# В модулі vacations_calendar повинна бути створена глобальна змінна calendar.
# Змінна calendar повинна містити словник (dict) всіх українських державних свят. дата ->
# назва або назва -> дата - що буде ключом ви обираєте самостійно. Обидва варіанти будуть зараховані.
# Словник calendar повинен бути типу dict, але типи внутрішніх данних ви обираєте самостійно.
# Будь який варіант вважається допустимим. Головне досягти працездатності функції check (дивіться наступну умову).
# В модулі vacations_calendar заборонено писати будь яку глобальну логіку.
# Якщо ви хочете протестувати ваш код, ви повинні це робити в іншому модулі, або прибрати логіку перед пушом в репозиторій.
# Створіть модуль vacations_checker який повинен містити глобально обʼявлену функцію def check(date_str)
# яка здатна виконати перевірку певної дати на те чи є вона державним святом чи ні.
# В модулі vacations_checker заборонено створювати якісь змінні які будуть містити інформацію про свята.
# Функція check повинна використовувати змінну calendar з модулю vacations_calendar.
# Функція приймає строчку наступного формату 'DD/MM/YYYY',
# наприклад '27/07/2022' - 27 липня 2022 року і повертає None (NoneType) або назву свята (str).
# Вважаємо що свята кожен рік в один і той самий день. Тобто, умовно,
# пасха не переноситься. Ви можете самі обрати статичний день для свят які зазвичай переносяться, або не включати їх зовсім.
# Головне показати логіку, а не коректність українських свят.
# Вважаємо що свята не змінюються від року в рік. Тобто ті свята які є в цьому році були і 3 роки назад.
# В модулі vacations_checker заборонено писати будь яку глобальну логіку.
# Якщо ви хочете протестувати ваш код, ви повинні це робити в іншому модулі, або прибрати логіку перед пушом в репозиторій.
# Приклади:
#
# check('27/07/2022') -> None
# check('28/07/2022') -> 'День Української Державності'
# check('28/07/2020') -> 'День Української Державності'

calendar = {
    '01/01' : 'Новий Рік',
    '07/01' : 'Різдво',
    '08/03' : 'Жіночий День',
    '09/05' : 'День Перемоги',
    '28/07' : 'День Державності',
    '24/08' : 'День Незалежності',
    '15/10' : 'День Захисників України',
    '25/12' : 'Різдво'
}