class Solution:
    def decodeString(self, s: str) -> str:
        res=""
        countS=[]
        resS=[]
        i=0
        while(i<len(s)):
            if(s[i].isdigit()):
                c=0
                while(s[i].isdigit()):
                    c=10*c+int(s[i])
                    i+=1
                countS.append(c)
            elif(s[i]=="["):
                resS.append(res)
                res=""
                i+=1
            elif(s[i]=="]"):
                t=""
                if(resS):
                    t=resS.pop()
                n=countS.pop()
                for j in range(n):
                    t+=res
                res=t
                i+=1
            else:
                res+=s[i]
                i+=1
        return res
        
        # stack = []; curNum = 0; curString = ''
        # for c in s:
        #     if c == '[':
        #         stack.append(curString)
        #         stack.append(curNum)
        #         curString = ''
        #         curNum = 0
        #     elif c == ']':
        #         num = stack.pop()
        #         prevString = stack.pop()
        #         curString = prevString + num*curString
        #     elif c.isdigit():
        #         curNum = curNum*10 + int(c)
        #     else:
        #         curString += c
        # return curString 
