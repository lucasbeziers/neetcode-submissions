class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for s in strs:
            letters_list = [0 for _ in range(26)]

            for letter in s:
                idx = ord(letter) - 97
                letters_list[idx] += 1
            
            letters = tuple(letters_list)

            if letters in groups:
                groups[letters].append(s)
            else:
                groups[letters] = [s]

        return [groups[group] for group in groups]

