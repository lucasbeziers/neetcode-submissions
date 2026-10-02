class Solution:
    pair = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    def isValid(self, s: str) -> bool:
        open_brackets = []
        for i in range(len(s)):
            char = s[i]
            # add open bracket
            if self.isOpen(char):
                open_brackets.append(char)
            else:
                # check there are brackets
                if len(open_brackets) == 0:
                    return False
                # stop if not correct
                latest_open = open_brackets.pop()
                if latest_open != self.pair[char]:
                    return False
        # check that all open brackets were closed
        return len(open_brackets) == 0

    
    def isOpen(self, s: str) -> bool:
        return (s == "(") or (s == "{") or (s == "[")