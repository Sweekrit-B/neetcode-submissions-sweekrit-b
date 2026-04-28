class Solution:
    def numDecodings(self, s: str) -> int:
        num_ways = [0] * len(s)
        if s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        elif int(s[0:2]) > 26 and s[1] == '0':
            return 0
        elif int(s[0:2]) > 26:
            num_ways[0] = 1
            num_ways[1] = 1
        elif s[1] == '0':
            num_ways[0] = 1
            num_ways[1] = 1
        else:
            num_ways[0] = 1
            num_ways[1] = 2
        
        for i in range(2, len(s)):
            # print("Last two digit: ", s[i-1:i+1], "; numerical: ", int(s[i-1:i+1]))
            if (not 10 <= int(s[i-1:i+1]) <= 26) and (s[i] == '0'):
                num_ways[i] = 0
            elif (not 10 <= int(s[i-1:i+1]) <= 26):
                num_ways[i] = num_ways[i-1]
            elif s[i] == '0':
                num_ways[i] = num_ways[i-2]
            else:
                num_ways[i] = num_ways[i-1] + num_ways[i-2]

        print(num_ways)
        return num_ways[-1]