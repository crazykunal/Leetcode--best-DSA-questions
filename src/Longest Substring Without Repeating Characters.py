class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
# O(n2)
        
#         max_len = 0
#         seen = set()
#         for i in range(len(s)):
#             for char in s[i:]:
#                 if char in seen:
#                     break
#                 else:
#                     seen.add(char)
#             if max_len < len(seen):
#                 max_len = len(seen)
#             seen = set()
#         return max_len

# O(2n)

        # max_len = 0
        # seen = set()
        # n, i, j = len(s), 0, 0
        # while i < n and j < n:
        #     if s[j] in seen:
        #         seen.remove(s[i])
        #         i += 1
        #     else:
        #         seen.add(s[j])
        #         max_len = max(max_len, len(seen))
        #         j += 1
        # return max_len
        
#O(n) using ascii
    
        # a=[-1]*256
        # m,start=0,0
        # for i in range(len(s)):
        #     start=max(a[ord(s[i])]+1,start)
        #     a[ord(s[i])]=i
        #     m=max(m,i-start+1)
        # return m

# O(n) best solution
        
        d = {}
        result = start = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(d[c] + 1, start)
            result = max(i - start + 1, result)
            d[c] = i
        return result
    
        

    
