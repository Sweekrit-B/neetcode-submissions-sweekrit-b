class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_letters = {}
        for s_ch in s:
            s_letters[s_ch] = 1 + s_letters.get(s_ch, 0)
        # print(s_letters)
        for t_ch in t:
            if s_letters.get(t_ch, 0) == 0:
                return False
            s_letters[t_ch] -= 1
        return sum(s_letters.values()) == 0
        