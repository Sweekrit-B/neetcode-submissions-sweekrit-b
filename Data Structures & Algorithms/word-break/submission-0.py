class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        starting_points = [0]

        for ix in range(len(s)):
            for sp in starting_points:
                # print(f"Currently looking at {s[sp:ix + 1]}")
                if s[sp:ix + 1] in wordDict:
                    # print(f"{s[sp:ix + 1]} in wordDict")
                    starting_points.append(ix + 1)
                    break
        
        print(starting_points)
        if starting_points[-1] == len(s):
            return True
        return False