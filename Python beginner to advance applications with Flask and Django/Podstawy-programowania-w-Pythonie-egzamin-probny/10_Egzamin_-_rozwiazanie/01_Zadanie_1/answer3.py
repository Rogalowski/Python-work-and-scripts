def check_palindrome(text):
    """Check if given text is palindrome.

    :param str text: some text
    :rtype: bool
    :return: True if given text is palindrome False elsewhere
    """
    text = text.lower().replace(' ', '')
    return text == text[::-1]


if __name__ == '__main__':
    print(check_palindrome("Kobyła ma mały bok"))
    print(check_palindrome("To nie jest palindrom"))
