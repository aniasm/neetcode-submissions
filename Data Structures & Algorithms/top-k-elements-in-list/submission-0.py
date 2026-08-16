class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq={}
        res =[]
        for i in nums:
            frq[i]=(frq.get(i,0))+1
        
        for l in range(k):
            x=max(frq, key=frq.get)
            res.append(x)
            frq[x]=-1
        return res
        