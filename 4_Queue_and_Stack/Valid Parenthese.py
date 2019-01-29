class Solution(object):
    def isValid(self, s):
        """
    input: string s
    return: boolean
    """
        # write your solution here
        res = []
        match = {'(': ')', '{': '}', '[': ']'}

        for ss in s:
            if ss in match:
                res.append(ss)
            elif not res or match[res[-1]] != ss:
                return False
            else:
                res.pop()
        return True