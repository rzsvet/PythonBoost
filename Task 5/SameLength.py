class SameLength:
    def same_length(self, number: int) -> bool:
        """ Функцию, которая возвращает True, если в переданном числе за каждой последовательностью единиц следует
        последовательность нулей той же длины.

        :param number: Input data for analyse
        :type number: <int>

        :rtype: bool
        :return: Result analyse input data (true, false)
        """
        number = str(number)
        counter = [0, 0]
        if int(number, 2) % 2 != 0:
            return False
        if number.count("0") != number.count("1"):
            return False
        for one_number in number:
            if one_number == "1" and counter[0] == 0:
                counter[1] += 1
            elif one_number == "0":
                counter[0] += 1
            else:
                if counter[0] != counter[1]:
                    return False
                counter = [0, 1]
        if counter[0] != counter[1]:
            return False
        return True

    def same_length_second(self, number: int) -> bool:
        """ Функцию, которая возвращает True, если в переданном числе за каждой последовательностью единиц следует
        последовательность нулей той же длины.

        :param number: Input data for analyse
        :type number: <int>

        :rtype: bool
        :return: Result analyse input data (true, false)
        """
        number = str(number)
        if int(number, 2) % 2 != 0:
            return False
        if number.count("0") != number.count("1"):
            return False
        run_loop = True
        while run_loop:
            start_unit = number.find("1")
            start_zero = number.find("0")
            start_unit_after_zero = number.find("1", start_zero)
            if start_unit_after_zero == -1:
                start_unit_after_zero = len(number)
                run_loop = False
            unit = start_zero - start_unit
            zero = start_unit_after_zero - start_zero
            if unit != zero:
                return False
            number = number[start_unit_after_zero:]
        return True
