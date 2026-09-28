class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)

        # Check same length
        if s_length != t_length:
            return False

        hashmap_s = {}
        hashmap_t = {}

        # Populate s
        for char in s:
            if char not in hashmap_s:
                hashmap_s[char] = 1
            else:
                hashmap_s[char] += 1

        # Populate t
        for char in t:
            if char not in hashmap_t:
                hashmap_t[char] = 1
            else:
                hashmap_t[char] += 1
        
        # Compare 1
        for char in hashmap_t:
            if char not in hashmap_s:
                return False
            if hashmap_t[char] != hashmap_s[char]:
                return False
        
        # Compare 2
        for char in hashmap_s:
            if char not in hashmap_t:
                return False
            if hashmap_s[char] != hashmap_t[char]:
                return False
        
        return True
