import re
from typing import List

"""
https://leetcode.com/problems/reorder-data-in-log-files
"""


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs, digit_logs = [], []
        
        for log in logs:
            tokens = log.split(" ")
            if re.match("^[0-9]+", tokens[1]):
                digit_logs.append(log)
            else:
                letter_logs.append(" ".join(tokens[1:]) + " " + tokens[0])
        
        new_letter_logs = []
        letter_logs.sort()
        for log in letter_logs:
            tokens = log.split(" ")
            new_letter_logs.append(tokens[-1] + " " + " ".join(tokens[:-1]))
                         
        return new_letter_logs + digit_logs
