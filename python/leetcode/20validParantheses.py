class Solution:
    def isValid(self, s: str) -> bool:
        # O(n) time | O(n) space, where n = len(string)
        # This makes adding additional types of pairs of parantheses easier ==> scalability
        pairing = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        openingBrackets = ['[', '{', '(']
        closingBrackets = [')', '}', ']']

        stack = []

        # consider each character in s
        for c in s:
            if c in openingBrackets:
                stack.append(c)
            elif c in closingBrackets:
                if len(stack) == 0 or stack.pop() != pairing[c]:
                    return False
            # else ignore the symbol since we only want the s
            # to be balanced in terms of brackets

        return len(stack) == 0