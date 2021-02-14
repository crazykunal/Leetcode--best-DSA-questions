#(class Trienode is my code)
class TrieNode:
    def __init__(self):
        self.isLeaf=False
        self.character={}
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # (horizontal scanning)
           
        # if(len(strs)==0):
        #     return ""
        # prefix=strs[0]
        # for i in range(1,len(strs)):
        #     while(strs[i].find(prefix)!=0):
        #         prefix=prefix[0:len(prefix)-1]
        #         if(not prefix):
        #             return ""
        # return prefix
        
        
        # (vertical scanning)
        
        # if(len(strs)==0):
        #     return ""
        # for i in range(len(strs[0])):
        #     c=strs[0][i]
        #     for j in range(1,len(strs)):
        #         if(i==len(strs[j]) or strs[j][i]!=c):
        #             return strs[0][:i]
        # return strs[0]
        
        # (divide and conquer)
        
        # def commonPrefix(left,right):
        #     min1=min(len(left),len(right))
        #     for i in range(0,min1):
        #         if(left[i]!=right[i]):
        #             return left[:i]
        #     return left[0:min1]
        # def longestCommonPrefix1(strs,l,r):
        #     if(l==r):
        #         return strs[l]
        #     else:
        #         mid=(l+r)//2
        #         lcpLeft=longestCommonPrefix1(strs,l,mid)
        #         lcpRight=longestCommonPrefix1(strs,mid+1,r)
        #         return commonPrefix(lcpLeft,lcpRight)
        # if(len(strs)==0):
        #     return ""
        # return longestCommonPrefix1(strs,0,len(strs)-1)
        
        # (Binary Search)
        
        # def isCommonPrefix(strs,len1):
        #     str1=strs[0][:len1]
        #     for i in range(1,len(strs)):
        #         if(not strs[i].startswith(str1)):
        #             return False
        #     return True
        # import sys
        # if(len(strs)==0):
        #     return ""
        # minLen=sys.maxsize
        # for str in strs:
        #     minLen=min(minLen,len(str))
        # low=1
        # high=minLen
        # while(low<=high):
        #     mid=(low+high)//2
        #     if(isCommonPrefix(strs,mid)):
        #         low=mid+1
        #     else:
        #         high=mid-1
        # return strs[0][0:(low+high)//2]



        def insert(str,root):
            t=root
            for i in str:
                # t = t.character.setdefault(key[i], TrieNode())
                if(i not in t.character):
                    t.character[i]=TrieNode()
                t=t.character[i]
            t.isLeaf=True
            
        root=TrieNode()
        for s in strs:
            insert(s,root)
        lcp=""
        curr=root
        while(curr and  not curr.isLeaf and len(curr.character)==1):
            for k,v in curr.character.items():
                lcp+=k
                curr=v
        return lcp
        
        # if not strs:
        #     return ""
        # shortest = min(strs,key=len)
        # for i, ch in enumerate(shortest):
        #     for other in strs:
        #         if other[i] != ch:
        #             return shortest[:i]
        # return shortest 
        
        
        # if not strs:
        #     return ""
        # minS = min(strs)
        # maxS = max(strs)
        # for i,x in enumerate(minS):
        #     if x != maxS[i]:
        #         return maxS[:i]
        # return minS
    
