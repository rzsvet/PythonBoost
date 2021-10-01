class Formation:
    def mineralFormation(self, matrix: list) -> str:
        """ Функция для определения входного вида списка

        :param matrix: Input data for analyse
        :type matrix: <List>

        :rtype: str
        :return: Result analyse input data (both, stalactites, stalagmites, none)
        """
        is_stalactites = sum(matrix[0])
        is_stalagmites = sum(matrix[-1])
        if is_stalagmites and is_stalactites:
            return "both"
        elif is_stalagmites:
            return "stalagmites"
        elif is_stalactites:
            return "stalactites"
        else:
            return "none"

