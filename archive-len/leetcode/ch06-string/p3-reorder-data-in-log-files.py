"""
https://leetcode.com/problems/reorder-data-in-log-files/
"""
class Solution(object):

    def reorder_log_files(self, logs):
        letters = []
        nums = []
        for log in logs:
            log_split = log.split(" ")
            if log_split[1].isalpha():
                letters.append((" ".join(log_split[1:]), log_split[0]))
            else:
                nums.append(log)
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters] + nums
