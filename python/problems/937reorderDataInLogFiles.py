class Solution:
    # O(n^2) time | O(1) space
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            if self.isDigitLog(log):
                digit_logs.append(log)
            else:
                self.insert_into_sorted_array(letter_logs, log)

    def get_identifier(self, log: str):
        return log.split(' ')[0]

    def get_first_contents(self, log: str):
        return log.split(' ')[1]

    # Maybe not needed
    def isLetterLog(self, log: str):
        return self.get_first_contents(log).lower().isalpha()

    def isDigitLog(self, log: str):
        # TODO check that this works
        return '0' <= self.get_first_contents(log) <= '9'

    def insert_into_sorted_array(self, array: list[str], log: str):
        # TODO implement
        pass
        