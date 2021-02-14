class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        # if not digits:
        #     return []
        # res = [""]
        # phone_list= {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
        #       '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # for i in range(len(digits)):
        #   t= []
        #   for j in phone_list[digits[i]]:
        #     for s in res: 
        #       t.append(s+j)
        #   res = t 
        # return res
        
        #(recursive)
        
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def backtrack(combination,digits):
            if len(digits) == 0:
                output.append(combination)
            else:
                for letter in phone[digits[0]]:
                    backtrack(combination + letter, digits[1:])                 
        output = []
        if digits:
            backtrack("", digits)
        return output
