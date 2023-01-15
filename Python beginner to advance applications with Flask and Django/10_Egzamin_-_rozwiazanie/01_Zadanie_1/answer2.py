def name_sorter(names):
    """Sort names and separate males and females.

    :param list names: list of names
    :rtype: dict
    :return: dict with separate names.
    """
    result = {
        'female': [],
        'male': []
    }

    for name in names:
        if name[-1] == 'a':
            result['female'].append(name)
        else:
            result['male'].append(name)
    return result


if __name__ == '__main__':
    input_data = ["Andrzej", "Henryk", "Alicja", "Cezary", "Barbara"]
    print(name_sorter(input_data))
