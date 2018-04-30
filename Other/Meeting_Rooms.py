class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        input: int[][] intervals
        return: boolean
        """
        # write your solution here

        start = []
        end = []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])

        if len(intervals) > 1:
            for j in range(len(intervals) - 1):
                if start[j + 1] < end[j]:
                    return False
            return True
        else:
            return True