class Pandigital:
    def is_pandigital(self,number: int) -> bool:
        """ Функция для определения панцифрового числа

        :param number: Input data for analyse
        :type number: <int>

        :rtype: bool
        :return: Result analyse input data (true, false)
        """
        return len(set(str(number))) == 10