class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        currPal = None
        currLen = 0

        def maxPalindromeLengthOdd(i):
            #print("Starting ODD check")
            valsOut = 1
            currLen = 1
            while ((i - valsOut) >= 0) and ((i + valsOut) < n) and s[i - valsOut] == s[i + valsOut]:
                #print("Comparing: ", s[i - valsOut], " to ", s[i + valsOut])
                currLen += 2
                valsOut += 1
                #print("Current valsOut: ", valsOut)
            valsOut -= 1 # counteract the initial +1
            if currLen == 1:
                valsOut = 0
            #print("Returning the following tuple: ", valsOut, currLen)
            return valsOut, currLen

        def maxPalindromeLengthEven(i):
            #print("Starting EVEN check")
            if (i == n - 1) or (s[i] != s[i+1]):
                return 0, 1
            #print("Checking: ", s[i], " and ", s[i + 1])
            valsOut = 1
            currLen = 2
            while ((i - valsOut) >= 0) and ((i + 1 + valsOut) < n) and s[i - valsOut] == s[i + 1 + valsOut]:
                #print("Comparing: ", s[i - valsOut], " to ", s[i + valsOut + 1])
                currLen += 2
                valsOut += 1
                #print("Current valsOut: ", valsOut)
            valsOut -= 1
            if currLen == 2:
                valsOut = 0
            #print("Returning the following tuple: ", valsOut, currLen)
            return valsOut, currLen
        
        for i in range(len(s)):
            #print("\nChecking: ", s[i])
            valsOutOdd, currLenOdd = maxPalindromeLengthOdd(i)
            #print("Received the following ODD values: ", valsOutOdd, currLenOdd)
            if currLenOdd > currLen:
                currLen = currLenOdd
                currPal = s[i - valsOutOdd:i + valsOutOdd + 1]
                #print("Found the following palindrome: ", currPal)
            valsOutEven, currLenEven = maxPalindromeLengthEven(i)
            #print("Received the following EVEN values: ", valsOutEven, currLenEven)
            if currLenEven > currLen:
                currLen = currLenEven
                currPal = s[i - valsOutEven:i + valsOutEven + 2]
                #print("Found the following palindrome: ", currPal)
        
        return currPal