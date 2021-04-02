class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        valueIndex = dict()
        for index, value in enumerate(nums):
            if target-value in valueIndex:
                return valueIndex[target-value],index
            else:
                valueIndex[value]=index