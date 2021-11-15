class Labirint:
    """
        Класс для выполнения десятого задания "Лабиринт" в марафоне
    """

    def can_exit(self, matrix: list[list[int]]) -> bool:
        """ Вычисление возможности дойти до финиша

        :param matrix: Входная матрица для проверки
        :type matrix: <list<list<int>>>

        :rtype: <bool>
        :return: Функция возвращает возможности дойти до финиша.

        """
        
        self.matrix = matrix
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])

        if self.matrix[-1][-1] == 1:
            return False

        self.matrix[0][0] = 1
        self.__find_path(0, 0)

        if self.matrix[-1][-1] == 0:
            return False
        else:
            return True

    def __find_path(self, i_row: int, i_column: int) -> None:
        """ Приватная рекурсивная функция проставляет вес соседних клеток

        :param i_row: Индекс ряда
        :type i_row: <int>

        :param i_column: Индекс столбца
        :type i_column: <int>

        :rtype: <None>
        :return: Функция ничего не возвращает.

        """
        weight = self.matrix[i_row][i_column]
        if i_row - 1 >= 0:
            if self.matrix[i_row - 1][i_column] == 0:
                self.matrix[i_row - 1][i_column] += weight + 1
                self.__find_path(i_row - 1, i_column)
        if i_row + 1 < self.rows:
            if self.matrix[i_row + 1][i_column] == 0:
                self.matrix[i_row + 1][i_column] += weight + 1
                self.__find_path(i_row + 1, i_column)
        if i_column - 1 >= 0:
            if self.matrix[i_row][i_column - 1] == 0:
                self.matrix[i_row][i_column - 1] += weight + 1
                self.__find_path(i_row, i_column - 1)
        if i_column + 1 < self.columns:
            if self.matrix[i_row][i_column + 1] == 0:
                self.matrix[i_row][i_column + 1] += weight + 1
                self.__find_path(i_row, i_column + 1)
