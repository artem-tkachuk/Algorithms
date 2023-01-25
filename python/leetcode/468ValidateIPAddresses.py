class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self.validIPv4(queryIP):
            return "IPv4"
        elif self.validIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"

    def validIPv4(self, queryIP: str) -> bool:
        # split into individual components
        components = queryIP.split('.')
        # check that we have 4 components
        if len(components) != 4:
            return False
        # check that each component is valid, and terminate early if it's not
        for comp in components:
            # range and type check
            if not(comp.isnumeric() and 0 <= int(comp) <= 255):
                return False
            # leading zeros
            if comp[0] == '0' and len(comp) > 1:
                return False
        # after we have checked everything, return True
        return True


    def validIPv6(self, queryIP: str) -> bool:
        # split into individual components
        components = queryIP.split(':')
        # check that we have 8 components
        if len(components) != 8:
            return False
        # check that each component is valid, and terminate early if it's not
        for comp in components:
            # check for non alpha-numeric characters and length of x_i
            if not(1 <= len(comp) <= 4):
                return False
            # check that 
            if not all([ch.isnumeric() or 'a' <= ch.lower() <= 'f' for ch in comp]):
                return False
        # after we have checked everything, return True
        return True

print(Solution().validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))