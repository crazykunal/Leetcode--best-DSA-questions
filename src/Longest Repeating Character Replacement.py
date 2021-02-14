class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = defaultdict(int)
        maxFreq = 0
        maxLength = 0
        start = end = 0
        for end in range(len(s)):
            freqDict[s[end]] += 1
            maxFreq = max(maxFreq, freqDict[s[end]])
            if ((end-start+1) - maxFreq) > k:
                freqDict[s[start]] -= 1
                start += 1
            else:
                maxLength = max(maxLength, end-start+1)
        return maxLength
