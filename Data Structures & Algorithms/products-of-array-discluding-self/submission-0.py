class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # get the size of list
        n = len(nums)

        # create result array
        res = [1] * n

        # prefix products (left pass)
        # res[i] will store the products of all numbers to the LEFT of i
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        # suffix products (right pass)
        right = 1
        for i in range(n-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

        # we are doing prefix-suffix DP problem        