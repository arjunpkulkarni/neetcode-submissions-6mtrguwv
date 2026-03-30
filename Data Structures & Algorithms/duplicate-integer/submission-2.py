class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDuplicates = set()

        for num in nums:
            noDuplicates.add(num);
        
        if len(nums) != len(noDuplicates):
            return True
        else:
            return False