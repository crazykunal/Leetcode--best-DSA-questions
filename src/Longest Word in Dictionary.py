class TrieNode:
    def __init__(self,letter):
        self.alphabet = letter
        self.children = [None]*26
        self.isLast = False 
class Trie:
    def __init__(self):
        self.root = TrieNode(" ")
    def insert(self,word):
        pointer = self.root 
        for alphabet in word:
            if not pointer.children[ord(alphabet) - ord('a')]:
                pointer.children[ord(alphabet) - ord('a')] = TrieNode(alphabet)
            pointer = pointer.children[ord(alphabet) - ord('a')] 
        pointer.isLast = True
    def solveUtil(self,root,partial,output):
        curr_len = 0 
        for child in root.children:
            if child and child.isLast:
                partial.append(child.alphabet)
                output = self.solveUtil(child,partial,output)
                if len(partial) > len(output):
                    output = "".join(partial)
                partial.pop()
        return output
    def solve(self):
        partial = []
        output = ""
        return self.solveUtil(self.root,partial,output) 

class Solution:
    def longestWord(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.solve() 
