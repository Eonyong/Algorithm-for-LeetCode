class Solution:
    def isValid(self, s: str) -> bool:
        op = []
        for item in s:
            if item in ['(', '{', '[']:
                op.append(item)
            else:
                if op:
                    i = op.pop()
                    if (item == ')' and i == '(') or (item == '}' and i == '{') or (item == ']' and i == '['):
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            if not op:
                return True
            else:
                return False