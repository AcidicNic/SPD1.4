class Solution:
    def twoSum(self, nums, target):
        """ Finds the indexes of two numbers in nums that add to target
        nums: int List
        target: int
        output: int List """
        # for each int in nums
        for i in range(len(nums)):
            # compare it to the following ints in the nums list
            for j in range(i+1, len(nums)):
                # if we found two ints that sum up to target,
                if nums[i] + nums[j] == target:
                    # return the indexes in a list
                    return [i, j]
