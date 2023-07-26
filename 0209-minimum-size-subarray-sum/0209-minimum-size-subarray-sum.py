class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Sliding window
        l = 0
        res = float('inf')
        total =0
        

        for r in range(0, len(nums)):
            total+=nums[r]
            while total>=target:
                res = min(res, r-l+1) #length of subarray right-left+1
                # substract left value and increase left pointer
                total -=nums[l]
                l+=1


        return 0 if res==float('inf') else res



