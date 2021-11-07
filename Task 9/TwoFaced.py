class TwoFaced:
    """
        Класс для выполнения девятого задания "Двуликий" в марафоне
    """

    def translator(self, text: str) -> str:
        """ Вычисление матрицы для сапёра

        :param text: Входной текст для преобразования
        :type text: <str>

        :rtype: <str>
        :return: Функция возвращает каждую букву в формате «двуликого кода».

        """

        a_byte_array = bytearray(text, "utf8")
        byte_list = []

        for byte in a_byte_array:
            byte_list.append(self.__two_faced_converter(bin(byte).replace("0b", "")))
        return ' '.join(byte_list)

    def __two_faced_converter(self, bin_letter: str) -> str:
        """ Приватная функция преобразование буквы в двоичноом коде в формат «двуликого кода»

        :param bin_letter: Входная строка с бинарным кодом символа
        :type bin_letter: <str>

        :rtype: <str>
        :return: Функция возвращает букву в формате «двуликого кода».

        """

        bin_letter = "0" * (8 - len(bin_letter)) + bin_letter
        code_text = "двуликий"
        for index, letter in enumerate(bin_letter):
            if bin_letter[index] == "1":
                code_text = code_text[:index] + code_text[index].upper() + code_text[index + 1:]

        return code_text