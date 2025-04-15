#https://leetcode.com/problems/contains-duplicate/description/
# Difficulty = Easy

def containsDuplicate(self, nums):
    set_nums = set()
    for num in nums:
        if num in set_nums:
            return True
        set_nums.add(num)
    return False

def containsDuplicate(self, nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True
    return False