class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums)) # create a array called ans with 2 * len(nums)
        n = len(nums) # create a var called n = len(nums) to track 2n
        for i in range(n): # iterate with index until reach end of nums
            ans[i] = nums[i] # first copy: ans[i] = nums[i]
            ans[i + n] = nums[i] # second copy: ans[i + n] = nums[i]
        
        return ans # return ans