class Pandigital:
    def is_pandigital(self,number: int) -> bool:
        """ Функция для определения панцифрового числа

        :param number: Input data for analyse
        :type number: <int>

        :rtype: bool
        :return: Result analyse input data (true, false)
        """
        if len(set(str(number))) == 10:
            return True
        else:
            return False
