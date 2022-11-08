# O(n log(n)) time | O(1) space
# Iterative solution that converts numbers to binary
import math 

class IterativeSolution:
    def countBits(self, n: int) -> list[int]:
        ans = []

        for i in range(0, n + 1):
            ans.append(self.count1sInBinaryRep(i))

        return ans
        

    def count1sInBinaryRep(self, num: int) -> int:
        ones = 0
        
        while num != 0:
            if num % 2 == 1:
                ones += 1
            num = num // 2
        
        return ones

# Dynamic programming solution
class DPComplicatedSolution:
    def countBits(self, n: int) -> list[int]:
        if n < 0:
            raise Exception('Invalid arguments!')
        upper_bound = int(math.pow(2, math.ceil(math.log(n + 1, 2))))
        bits_counter_upper_bound = self.countBitsHelper(upper_bound)
        return bits_counter_upper_bound[:n + 1]

    # We can assume n % 2 == 0 and n >= 0
    def countBitsHelper(self, n: int) -> list[int]:
        if n == 1:
            return [0]
        subsize = n // 2
        subproblem = self.countBitsHelper(subsize)
        return subproblem + list(map(lambda x, y: x + y, subproblem, [1] * subsize))

# O(n) time, O(1) space – not counting the resulting array
class DPNeetCodeSimpleSolution:
    def countBit(self, n: int) -> list[int]:
        dp = [0]
        offset = 1

        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            dp.append(dp[i - offset] + 1)

        return dp