class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for s in strs:
            anagram_dict[tuple(sorted(s))].append(s)
        return list(anagram_dict.values())