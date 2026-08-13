class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums:
                k= nums.index(target-nums[i])
                if k!=i:
                    if i>k:
                        return [k,i]
                    return [i,k]
        # return [0,1]