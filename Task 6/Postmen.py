class Postmen:
    """
        Класс для выполнения шестого задания "Гарри — почтальон" в марафоне
    """
    __all_path = []  # type: list #param: Приватный список содержит все возможные пути
    __path_index = 0  # type: int #param: Приватный номер текущего пути
    __path_max = 0  # type: int #param: Приватное значение максимальной суммы всех значений встречающихся на пути
    __path_max_index = 0  # type: int #param: Приватный индекс из переменный __all_path, содержащий значение __path_max
    __path = []  # type: list #param: Приватный список для генерации пути

    def __findAllPathsUtil(self, mat: list[list[int]], i: int, j: int, height: int, width: int, step: int) -> None:
        """ Приватная рекурсивная функция для генерации пути по матрице. Без возврата данных

        :param mat: Input matrix for analyse
        :type mat: <list<list<int>>>

        :param i: Param for move down
        :type i: <int>

        :param j: Param for move right
        :type j: <int>

        :param height: Height of matrix
        :type height: <int>

        :param width: Width of matrix
        :type width: <int>

        :param step: Number of step
        :type step: <int>

        """

        # Reached the bottom of the matrix
        # so we are left with only option to move right
        if i == height - 1:
            for k in range(j, width):
                self.__path[step + k - j] = mat[i][k]
            self.__all_path.append([])
            for sd in range(step + width - j):
                self.__all_path[self.__path_index].append(self.__path[sd])
            self.__nextPath()
            return

        # Reached the right corner of the matrix
        # we are left with only the downward movement.
        if j == width - 1:
            for k in range(i, height):
                self.__path[step + k - i] = mat[k][j]
            self.__all_path.append([])
            for sr in range(step + height - i):
                self.__all_path[self.__path_index].append(self.__path[sr])
            self.__nextPath()
            return

        # Add the current cell
        # to the path being generated
        self.__path[step] = mat[i][j]

        # Print all the paths
        # that are possible after moving down
        self.__findAllPathsUtil(mat, i + 1, j, height, width, step + 1)

        # Print all the paths
        # that are possible after moving right
        self.__findAllPathsUtil(mat, i, j + 1, height, width, step + 1)

        # Print all the paths
        # that are possible after moving diagonal
        # printAllPathsUtil(mat, i+1, j+1, height, width, path, step + 1);

    def __findAllPaths(self, mat: list[list[int]], height: int, width: int) -> None:
        """ Приватная функция для генерации всех доступных путей по матрице .
         Поиск пути происходит от левого верхнего угла до правого нижнего угла.
         Без возврата данных.

        :param mat: Input matrix for analyse
        :type mat: <list<list<int>>>

        :param height: Height of matrix
        :type height: <int>

        :param width: Width of matrix
        :type width: <int>

        """
        self.__path = [0] * (height + width)
        self.__findAllPathsUtil(mat, 0, 0, height, width, 0)

    def harry(self, field: list[list[int]]) -> int:
        """ Функция для вывода самой большой суммы чисел встречающейся в матрице.
         В случае если матрица пуста будет возвращено -1

        :param field: Input matrix for analyse
        :type field: <list<list<int>>>

        :rtype: int
        :return: Функция возвращает большую сумму из всех возможных путей матрицы.

        """
        if len(field[0]) == 0:
            return -1
        field_width = len(field[0])
        field_height = len(field)
        self.__init_values()
        self.__findAllPaths(field, field_height, field_width)
        return self.__path_max

    def __nextPath(self) -> None:
        """ Приватная функция для смены шага поиска пути и определения наибольшей суммы шагов

        :param None: Input matrix for analyse
        :type None: <list<list<int>>>

        :rtype: None
        :return: Функция ничего не возвращает.

        """
        if sum(self.__all_path[self.__path_index]) > self.__path_max:
            self.__path_max = sum(self.__all_path[self.__path_index])
            self.__path_index = self.__path_index
        self.__all_path[self.__path_index].append(sum(self.__all_path[self.__path_index]))
        self.__path_index += 1

    def __init_values(self) -> None:
        """ Приватная функция для сброса значений переменных

        :rtype: None
        :return: Функция ничего не возвращает.

        """
        self.__all_path = []
        self.__path_index = 0
        self.__path_max = 0
        self.__path_max_index = 0
        self.__path = []
