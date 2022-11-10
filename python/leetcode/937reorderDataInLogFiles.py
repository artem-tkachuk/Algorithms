# O(M* N^2) time | O(M * N) space
class LiteralSlowSortSolution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []
        # go over each log and insert to appropriate array depending on its type 
        for log in logs:
            if self.isDigitLog(log):
                digit_logs.append(log)
            else:
                # self.insert_into_sorted_array(letter_logs, log)
                letter_logs.append(log)
        # return the appended arrays
        # sort letter logs
        letter_logs.sort(key=lambda log: (self.get_contents(log), self.get_id(log)))

        return letter_logs + digit_logs

    def get_id(self, log: str):
        return log.split(' ')[0]

    def get_contents(self, log: str):
        return " ".join(log.split(' ')[1:])

    def get_first_token_from_contents(self, log: str):
        return log.split(' ')[1]

    def isDigitLog(self, log: str):
        # TODO check that this works
        return self.get_first_token_from_contents(log).isnumeric()

    # Can also do binary search on this
    def insert_into_sorted_array(self, array: list[str], log: str):
        # current length of the array
        m = len(array)
        inserted = False
        # linear search for the proper place in the letters array
        for i in range(m):
            content, curr_content = self.get_contents(log), self.get_contents(array[i])
            id, curr_id = self.get_id(log), self.get_id(array[i])

            if (content < curr_content) or (content == curr_content and id < curr_id):
                array.insert(i, log)
                inserted = True
                break

        if not inserted:
            array.append(log)
        
        
# O(M * N * log(N)) time | O(M * N) space
class PythonicSolution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        return sorted(logs, key=self.get_key)

    def get_key(self, log: str):
        id, contents = log.split(' ', maxsplit=1)
        return (1, None, None) if contents[0].isnumeric() else (0, contents, id)

# O(M * N * log(N)) time | O(M * N) space
class OneLinerSolution:
     def reorderLogFiles(self, logs: list[str]) -> list[str]:
        return sorted(logs, key=lambda log: (1, None, None) if log.split(' ', maxsplit=1)[1][0].isnumeric() else (0, log.split(' ', maxsplit=1)[1], log.split(' ', maxsplit=1)[0]))


# Testing
print(LiteralSlowSortSolution().reorderLogFiles(
    ["a1 9 2 3 1",
    "g1 act car",
    "zo4 4 7",
    "ab1 off key dog",
    "a8 act zoo",
    "a2 act car"]
))


# Expected: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Received: ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']