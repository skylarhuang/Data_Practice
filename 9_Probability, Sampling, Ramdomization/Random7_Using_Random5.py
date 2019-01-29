class Solution(object):
    def random7(self, random5):
        """
        write your solution here
        you can use random5() for generating
        0 - 4 with equal probability.
        """
        random25 = 5*random5() + random5()
        while random25 > 6:
          random25 = 5*random5() + random5()
        return random25 % 7