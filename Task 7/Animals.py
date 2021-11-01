import random


class Animals:
    """
        Класс для поиска животных
    """
    __animals = ["dog", "cat", "bat", "cock", "cow", "pig",
                 "fox", "ant", "bird", "lion", "wolf", "deer",
                 "bear", "frog", "hen", "mole", "duck", "goat"]  # type: list #param: Приватный список животных
    __counts = []

    def count_animals(self, text: str) -> int:
        """ Функция, которая возращает максимальное значение найденных животных

        :param text: Input matrix for analyse
        :type text: <str>

        :rtype: int
        :return: Функция возвращает большую сумму из всех возможных путей матрицы.

        """

        self.__cycle_finder(text, self.__animals, 0)
        self.__cycle_finder(text, reversed(self.__animals), 0)
        self.__cycle_finder(text, random.sample(self.__animals, len(self.__animals)), 0)

        return max(self.__counts)

    def __cycle_finder(self, text: str, animals: list, count: int) -> None:
        """ Приватная рекурсивная функция, которая ведёт подсчёт найденных животных

        :param text: Input text for find animals
        :type text: <str>

        :param animals: Input list of animals
        :type animals: <list>

        :param count: Found animals counter
        :type count: <int>

        :rtype: None
        :return: Функция ничего не возвращает.

        """
        for animal in animals:
            text_temp = text
            for char in animal:
                text_temp = text_temp.replace(char, "", 1)
            if len(text) == (len(text_temp) + len(animal)):
                self.__cycle_finder(text_temp, animals, count + 1)
        self.__counts.append(count)

