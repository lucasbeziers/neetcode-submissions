class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)

        # Check same length
        if s_length != t_length:
            return False

        hashmap_s = {}
        hashmap_t = {}

        # Populate
        for i in range(s_length):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0)
        
        # Compare
        return hashmap_s == hashmap_t 
