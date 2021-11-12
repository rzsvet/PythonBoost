# PythonBoost
## Описание
Репозиторий участника кодинг марафона в группе в https://t.me/pythonboost
## Задачи

---

### Кодинг-марафон. Задача № 1.

Приз: 10 баллов.

#### Задание

Создайте функцию, которая принимает две строки и вычисляет расстояние Хэмминга между ними.

#### Дополнительная информация

Расстояние Хэмминга — число позиций, в которых соответствующие символы двух слов одинаковой длины различны.

Например, в строке «ABCB» на четвертой позиции стоит буква «B», а в строке «ABCD» на той же позиции — буква «D». Расстояние Хэмминга между этими строками — 1.

#### Примечание
Исходим из того, что передаваемые строки всегда будут одинаковой длины.

#### Примеры
```
    hamming_distance("abcde", "bcdef") ➞ 5
    hamming_distance("abcde", "abcde") ➞ 0
    hamming_distance("strong", "strung") ➞ 1
    hamming_distance("ABBA", "abba") ➞ 4
```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/rasstoyanie-hemminga/)

---

### Кодинг-марафон. Задача № 2.

Приз: 10 баллов.

#### Задание

22 октября — ДЕНЬ CAPS LOCK. За исключением этого дня, все предложения должны быть в нижнем регистре. Поэтому напишите функцию для нормализации предложения.

Эта функция должна принимать строку. Если строка состоит только из символов верхнего регистра, переведите их в нижний регистр и добавьте в конце восклицательный знак.

#### Примечание
- каждая передаваемая в функцию строка - отдельное предложение
- предложение после нормализации должно начинаться с заглавной буквы
- восклицательный знак добавляем к предложениям, которые переводили из верхнего регистра в нижний.

#### Примеры
```
    normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"

    normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."

    normalize("Let us stay calm, no need to panic.") ➞ "Let us stay calm, no need to panic."
```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/den-caps-lock-zakonchilsya/)

---

### Кодинг-марафон. Задача № 3.

Приз: 10 баллов.

#### Задание

Сталактиты свисают с потолка пещеры, а сталагмиты растут из пола.

Создайте функцию, которая определяет, представляет ли ввод «stalactites» (сталактиты) или «stalagmites» (сталагмиты). Если ввод содержит и сталактиты, и сталагмиты, верните «both» («оба»).

Ввод будет двухмерным списком, где 1 представляет кусок камня, а 0 — воздушное пространство.

#### Примеры
```
    mineralFormation([
      [0, 1, 0, 1],
      [0, 1, 0, 1],
      [0, 0, 0, 1],
      [0, 0, 0, 0]
    ]) ➞ "stalactites"
    
    mineralFormation([
      [0, 0, 0, 0],
      [0, 1, 0, 1],
      [0, 1, 1, 1],
      [0, 1, 1, 1]
    ]) ➞ "stalagmites"
    
    mineralFormation([
      [1, 0, 1, 0],
      [1, 1, 0, 1],
      [0, 1, 1, 1],
      [0, 1, 1, 1]
    ]) ➞ "both"
```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/stalaktity-ili-stalagmity/)

---

### Кодинг-марафон. Задача № 4.

Приз: 10 баллов.

#### Задание

Панцифровое число — целое число (в какой-то выбранной системе счисления), в котором каждая цифра данной системы счисления появляется по крайней мере один раз. 

Для целей нашей задачи мы будем считать панцифровым целое число в десятичной системе, в котором встречается хотя бы раз каждая цифра от 0 до 9.

Напишите функцию, которая будет принимать целое число и возвращать True, если оно является панцифровым, и False — в противном случае.

#### Примечание

Подумайте о свойствах панцифрового числа после удаления всех дубликатов.

#### Примеры
```
    is_pandigital (98140723568910) ➞ True

    is_pandigital (90864523148909) ➞ False: 7 отсутствует.

    is_pandigital (112233445566778899) ➞ False
```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/panczifrovye-chisla/)

---

### Кодинг-марафон. Задача № 5.

Приз: 10 баллов.

#### Задание

Напишите функцию, которая возвращает True, если в переданном числе за каждой последовательностью единиц следует последовательность нулей той же длины.

#### Примечание

Подумайте о свойствах панцифрового числа после удаления всех дубликатов.

#### Примеры
```
    same_length (110011100010) ➞ True

    same_length (101010110) ➞ False

    same_length (111100001100) ➞ True

    same_length (111) ➞ False
```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/ediniczy-i-nuli/)

С решением не согласен. Оно решает только частный случай и вслучае если ввходные данные будут 110100 покажет True, хотя должен показать False

---

### Кодинг-марафон. Задача № 6.

Приз: 10 баллов.

#### Задание

Гарри — почтальон. У него есть почтовый участок размером n * m (матричный / 2D-список). Каждый слот в 2D-списке представляет количество писем в этом месте.

Гарри может идти только вправо и вниз. Он начинает обход в (0, 0) и заканчивает в (n-1, m-1). n представляет высоту, а m — длину матрицы.

Письма Гарри может брать только там, где находится.

Напишите функцию, возвращающую максимальное количество писем, которое Гарри может подобрать.

#### Примечание
Если матрица пуста, вернуть -1.

#### Примеры
```
    harry([[5, 2], [5, 2]]) ➞ 12
    # (5+5+2)
    
    harry([
      [1, 2, 3, 4, 5],
      [6, 7, 8, 9, 10],
      [11, 12, 13, 14, 15]
    ]) ➞ 72
    # (1+6+11+12+13+14+15)
    
    harry([[]]) ➞ -1

```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/pochtalon-i-sbor-pisem/)

---

### Кодинг-марафон. Задача № 7.

Приз: 10 баллов.

#### Задание

Есть список названий животных:
```pycon
animals = ["dog", "cat", "bat", "cock", "cow", "pig", "fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat"]
``` 
Напишите функцию, которая будет принимать строку txt и возвращать максимальное количество названий животных, которые возможно собрать из символов строки.

#### Примеры
```
    txt = "goatcode"
    count_animals(txt) ➞ 2
    
    # первое животное = "dog"
    # оставшиеся символы в строке = "atcoe",
    # второе животное = "cat".
    # count = 2 (верно)
    
    # если взять  сперва  "goat", 
    # оставшиеся символы в строке = "code",
    # т.е. больше нельзя составить имен животных
    # count = 1 (неверно)
    
    
    count_animals("goatcode") ➞ 2
    # "dog", "cat"
    
    count_animals("cockdogwdufrbir") ➞ 4
    # "cow", "duck", "frog", "bird"
    
    count_animals("dogdogdogdogdog") ➞ 5

```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/skolko-zhivotnyh/)

---

### Кодинг-марафон. Задача № 8.

Приз: 10 баллов.

#### Задание

Эта задача основана на игре сапер.
Создайте функцию, которая принимает сетку из  "#" и "-". Каждая решетка (#) представляет мину, а каждое тире (-) - место без мин. 

Верните список, в котором каждое тире заменено цифрой, обозначающей количество мин, непосредственно примыкающих к нему (по горизонтали, вертикали и диагоналям).

#### Примеры
```
    num_grid ([
      [«-», «-», «-», «-», «-»],
      [«-», «-», «-», «-», «-»],
      [«-», «-», «#», «-», «-»],
      [«-», «-», «-», «-», «-»],
      [«-», «-», «-», «-», «-»]
    ]) ➞ [
      [«0», «0», «0», «0», «0»],
      [«0», «1», «1», «1», «0»],
      [«0», «1», «#», «1», «0»],
      [«0», «1», «1», «1», «0»],
      [«0», «0», «0», «0», «0»],
    ]
    
    num_grid ([
      [«-», «-», «-», «-», «#»],
      [«-», «-», «-», «-», «-»],
      [«-», «-», «#», «-», «-»],
      [«-», «-», «-», «-», «-»],
      ["#", "-", "-", "-", "-"]
    ]) ➞ [
      [«0», «0», «0», «1», «#»],
      [«0», «1», «1», «2», «1»],
      [«0», «1», «#», «1», «0»],
      [«1», «2», «1», «1», «0»],
      [«#», «1», «0», «0», «0»]
    ]
    
    num_grid ([
      [«-», «-», «-», «#», «#»],
      [«-», «#», «-», «-», «-»],
      [«-», «-», «#», «-», «-»],
      [«-», «#», «#», «-», «-»],
      [«-», «-», «-», «-», «-»]
    ]) ➞ [
      [«1», «1», «2», «#», «#»],
      [«1», «#», «3», «3», «2»],
      [«2», «4», «#», «2», «0»],
      [«1», «#», «#», «2», «0»],
      [«1», «2», «2», «1», «0»],
    ]

```
#### Официальное решение
[Ссылка на решение](https://pythonist.ru/sapyor/)

---

### Кодинг-марафон. Задача № 9.

Приз: 10 баллов.

#### Задание

Слово «двуликий» состоит из 8 букв. Байт в двоичном формате имеет 8 бит. Байт может представлять символ.

Мы можем использовать слово «двуликий» для выражения слов в двоичном формате, если используем заглавные буквы как единицы, а строчные — как нули.

Создайте функцию, которая будет переводить слово в виде обычного текста в «двуликий код».

#### Примеры
```
    translator("Hi") ➞ "дВулИкий дВУлИкиЙ"
    translator("123") ➞ "двУЛикиЙ двУЛикИй двУЛикИЙ"

```

#### Примечание

Переводите слова, написанные латиницей, и цифры. За перевод кириллицы - дополнительный балл.

#### Официальное решение
[Ссылка на решение](https://pythonist.ru/dvulikij-kod/)
