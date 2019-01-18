def remove(input, t):
    """
    input: string input, string t
    return: String
    """
    # write your solution here

    String = input

    for char in t:
        String = input.replace(char, '')
        input = String

    return String