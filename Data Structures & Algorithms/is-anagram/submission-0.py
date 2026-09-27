class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False

        n = len_s
        letters_s = {}
        letters_t = {}
        for i in range(n):
            letter_s = s[i]
            if letter_s not in letters_s:
                letters_s[letter_s] = 1
            else:
                letters_s[letter_s] += 1
            
            letter_t = t[i]
            if letter_t not in letters_t:
                letters_t[letter_t] = 1
            else:
                letters_t[letter_t] += 1
        
        return letters_s == letters_t
            
