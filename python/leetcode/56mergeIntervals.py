from typing import List

class Solution:
    def merge_iteration(self, intervals: List[List[int]]) -> List[List[int]]:
        merging_done = False

        while not merging_done:
            n = len(intervals)
            merging_done = True

            for i in range(n):
                for j in range(i + 1, n):
                    [start_i, end_i] = intervals[i]
                    [start_j, end_j] = intervals[j]

                    if start_j <= start_i <= end_j:
                        if end_i <= end_j:
                            intervals.pop(i)
                        else:
                            intervals.pop(j)
                            # i < j, so index of i is not affected by popping j
                            intervals.pop(i) 
                            intervals.append([start_j, end_i])

                        merging_done = False
                        break

                    if start_j <= end_i <= end_j:
                        if start_j <= start_i:
                            intervals.pop(i)
                        else:
                            intervals.pop(j)
                            # i < j, so index of i is not affected by popping j
                            intervals.pop(i)
                            intervals.append([start_i, end_j])

                        merging_done = False
                        break

                if not merging_done:
                    break

        return intervals

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))

        i = 0

        while i < len(intervals) - 1:
            [_, end_curr] = intervals[i]
            [start_next, end_next] = intervals[i + 1]

            if start_next <= end_curr:
                if end_next <= end_curr:
                    intervals.pop(i + 1)
                else:
                    intervals[i][1] = end_next
                    intervals.pop(i + 1)
            else:
                i += 1

        return intervals

                


intervals1 = [[1,3],[2,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]]

print(Solution().merge(intervals1))
print(Solution().merge(intervals2))