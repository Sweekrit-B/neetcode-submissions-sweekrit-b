class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # neetcode
        adj = {c:set() for w in words for c in w}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visit = {} # false = visited, true = current path
        res = []

        def dfs(c):
            if c in visit:
                return visit[c] # if returns true, we saw something in the current path

            visit[c] = True # set the c as in the current path
            
            for nei in adj[c]: # check every neighbor
                if dfs(nei):
                    return True

            visit[c] = False # remove the current path
            res.append(c) # add the value
        
        for c in adj:
            if dfs(c):
                return ""
        
        return "".join(res[::-1])
