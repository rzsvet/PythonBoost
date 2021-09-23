def hamming_distance_check(first_word, second_word):
    counter = 0
    for index, letter in enumerate(first_word):
        if letter != second_word[index]: counter += 1
    return counter


def hamming_distance(first_word, second_word):
    if len(first_word) != len(second_word): return -1
    if first_word == second_word:
        return 0
    else:
        return hamming_distance_check(first_word, second_word)


if __name__ == '__main__':
    print(hamming_distance("abcde", "bcdef"))  # 5
    print(hamming_distance("abcde", "abcde"))  # 0
    print(hamming_distance("strong", "strung"))  # 1
    print(hamming_distance("ABBA", "abba"))  # 4
