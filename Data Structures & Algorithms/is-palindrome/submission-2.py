class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_s = len(s)

        # Trivial case
        if len(s) == 1:
            return True

        i = 0
        j = len(s) - 1

        while (i < j):
            # handle space
            skip_i = not s[i].isalnum()
            skip_j = not s[j].isalnum()
            if skip_i:
                i += 1
            if skip_j:
                j -= 1
            if skip_i or skip_j:
                continue
            
            # only alphanumeric
            char_i = s[i].lower()
            char_j = s[j].lower()
            if char_i != char_j:
                return False
            
            i += 1
            j -= 1
        
        return True
            