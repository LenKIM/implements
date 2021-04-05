
"""
https://leetcode.com/problems/remove-duplicate-letters
"""


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""

        charset = set(s)
        ordering = sorted(list(charset))

        for c in ordering:
            sub_str = s[s.index(c):]

            if charset == set(sub_str):
                next_str = sub_str.replace(c, '')
                return c + self.removeDuplicateLetters(next_str)

    # 같은 풀이의 다른 코드
    def removeDuplicateLetters_another(self, s: str) -> str:

        init_input = s
        init_order_chars = sorted(list(set(init_input)))

        def get_lexico_dedup(input_str, acc):
            if len(acc) == len(init_order_chars):
                return ''.join(acc)

            res = ""

            ordered_chars = sorted(list(set(input_str)))

            for c in init_order_chars:
                if c not in input_str or c in acc:
                    continue

                c_idx = input_str.index(c)

                sub_str = input_str[c_idx:]

                if set(ordered_chars) == set(sub_str):
                    res = get_lexico_dedup(sub_str.replace(c, ''), acc + [c])
                    if res:
                        break

            return res

        return get_lexico_dedup(init_input, [])
