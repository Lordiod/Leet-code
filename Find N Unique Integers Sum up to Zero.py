# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/
# Difficulty = Easy

def sumZero(self, n):
        return range(1 - n, n, 2)