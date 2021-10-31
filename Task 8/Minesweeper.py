import numpy as np

class Minesweeper:
    """
        Класс для выполнения восьмого задания "Сапёр" в марафоне
    """

    def num_grid(self, matrix: list[list[str]]) -> list[list[str]]:
        """ Вычисление матрицы для сапёра

        :param matrix: Input matrix for analyse
        :type matrix: <list<list<str>>>

        :rtype: <list<list<str>>>
        :return: Функция возвращает цифры карты сапёра.

        """

        matrix = np.array(matrix)
        for num_x, matrix_line in enumerate(matrix):
            for num_y, value in enumerate(matrix_line):
                if value == "-":
                    finder = matrix[
                         num_x - 1 if num_x > 0 else 0:
                         num_x + 2 if num_x < len(matrix) else len(matrix) - 1
                         ,
                         num_y - 1 if num_y > 0 else 0:
                         num_y + 2 if num_y < len(matrix_line) else len(matrix_line) - 1
                    ]
                    matrix[num_x][num_y] = np.count_nonzero(finder == "#")
        return matrix.tolist()