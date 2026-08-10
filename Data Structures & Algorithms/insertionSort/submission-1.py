# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if len(pairs)==0: return []
        res = [pairs.copy()]
        for j in range(1,len(pairs)):
            i=j
            while ((pairs[i].key < pairs[i-1].key) and i>=1):
                tmp = pairs[i-1]
                pairs[i-1] = pairs[i]
                pairs[i] = tmp
                i-=1
            res.append(pairs.copy())
        return res
