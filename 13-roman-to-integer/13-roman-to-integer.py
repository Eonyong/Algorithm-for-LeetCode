class Solution:
    def romanToInt(self, s: str) -> int:
        one_word = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        two_word = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        answer = 0
        idx = 0
        while idx < len(s):
            if idx + 1 < len(s) and s[idx] + s[idx + 1] in ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']:
                answer += two_word[s[idx] + s[idx + 1]]
                idx += 2
            else:
                answer += one_word[s[idx]]
                idx += 1
        else:
            return answer