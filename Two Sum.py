# https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy
class Solution:
    def twoSum(self ,nums, target):
        numbers = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numbers:
                return [numbers[diff], i]
            numbers[num] = i
        return None
