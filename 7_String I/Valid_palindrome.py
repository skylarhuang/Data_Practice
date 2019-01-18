class Solution(object):
    def valid(self, input):
        """
    input: string input
    return: boolean
    """
        # write your solution here
        word_new = ''.join(ch if ch.isalnum() else '' for ch in input)

        letter = list(word_new)
        result = True

        for i in range(len(letter) // 2):
            if letter[i] != letter[(len(letter) - 1 - i)]:
                result = False

        return result