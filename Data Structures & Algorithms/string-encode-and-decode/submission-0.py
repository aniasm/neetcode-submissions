class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s+=(str(len(i))+ '!' + i)
        return s

    def decode(self, s: str) -> List[str]:
        t=0
        word = ''
        strs = []
        x=''
        while t<len(s):
            while s[t]!='!':
                x+=s[t]
                t+=1
            t+=1
            for i in range(int(x)):
                word+=s[t]
                t+=1
            strs.append(word)
            word=''
            x=''
        return strs



