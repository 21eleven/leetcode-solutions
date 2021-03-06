"""
421. Maximum XOR of Two Numbers in an Array
Medium

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

 

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [0]
Output: 0

Example 3:

Input: nums = [2,4]
Output: 6

Example 4:

Input: nums = [8,10,2]
Output: 10

Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

 

Constraints:

    1 <= nums.length <= 2 * 104
    0 <= nums[i] <= 231 - 1

"""
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maxxor = 0
        mask = 0
        for i in range(32)[::-1]:
            in_play = set()
            mask |= 1 << i
            newxor = maxxor | (1 << i)
            for n in nums:
                in_play.add(n&mask)
            for bit in in_play:
                if bit ^ newxor in in_play:
                    maxxor = newxor
                    break
        return maxxor
        
