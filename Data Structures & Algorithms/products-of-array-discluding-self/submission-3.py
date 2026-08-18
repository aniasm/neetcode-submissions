class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        output =[]
        z=0
        p=False
        for i in nums:
            if i == 0:
                z+=1
                continue
            prod = prod* i
            p=True
        if z==1 and p:
            for j in nums:
                if j==0:
                    output.append(prod)
                else:
                    output.append(0)
        elif z>1:
            return [0]*len(nums)
        else:
            for j in nums:
                output.append(prod//j)
        return output

        