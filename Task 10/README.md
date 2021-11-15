# Кодинг-марафон. Задача № 10.

Приз: 10-20 баллов.

## Задание

Лабиринт может быть представлен двухмерной матрицей, где нули представляют области, по которым можно ходить, а единицы - стены. Вы начинаете движение с верхнего левого угла, а выход находится в самой нижней правой ячейке.

Создайте функцию, которая возвращает истину, если вы можете пройти от одного конца лабиринта до другого. Двигаться можно только вверх, вниз, влево и вправо. По диагонали двигаться нельзя.

## Примеры
```
    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0]
    ]) ➞ true
    
    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 0, 1, 0, 0, 1],
      [1, 1, 0, 0, 1, 1, 1]
    ]) ➞ false
    # В этом лабиринте одни тупики!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1]
    ]) ➞ false
    # Выход так близко, но недостижим!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 0]
    ]) ➞ true

```

## Примечание

1. В лабиринте размером m x n вы входите в [0, 0] и выходите в [m-1, n-1].

2. За эту задачу можно будет получить дополнительные 10 балов (т.е. всего 20), если сделать визуализацию алгоритма поиска пути при помощи модуля turtle либо его аналогов.

3. Также эту задачу не обязательно сдавать на repl.it - страницы на гитхабе либо просто файла будет достаточно.

## Официальное решение
[Ссылка на решение](#)