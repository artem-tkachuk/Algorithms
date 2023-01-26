from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        valid_IPs = []
        # Put the first dot
        for i in range(1, 4):
            # 
            curr_si = self.insertDotAt(s, i)
            # Insert the second dot in all possible locations
            # n + 1 because we have already inserted one dot
            for j in range(i + 2, n + 1):
                curr_sj = self.insertDotAt(curr_si, j)
                # Insert the third dot in all possible places
                # n + 2 since we have already added two dots
                for k in range(j + 2, n + 2):
                    final_IP = self.insertDotAt(curr_sj, k)
                    # validate the final IP address
                    if self.validateIPv4Address(final_IP):
                        # append to the final output list if it is a valid one
                        valid_IPs.append(final_IP)

        return valid_IPs

    def insertDotAt(s, i):
        return s[:i] + '.' + s[i:]


    def validateIPv4Address(self, s: str) -> bool:
        tokens = s.split('.')

        if len(tokens) != 4:
            return False

        for tok in tokens:
            if not(tok.isnumeric() and 0 <= int(tok) <= 255):
                return False
            if tok[0] == '0' and len(tok) > 1:
                return False

        return True

print(Solution().restoreIpAddresses('19216811'))