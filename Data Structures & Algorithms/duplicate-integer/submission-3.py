class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # init a set 

        seen = set()
        # loop through nums 

        for num in nums: 
            if num in seen:
                return True
            seen.add(num)

        return False
        # if nums[i] exist in set return true 
        # else add and return false at end 