"""
949. Largest Time for Given Digits
Easy

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"

Example 2:

Input: [5,5,5,5]
Output: ""

 

Note:

    A.length == 4
    0 <= A[i] <= 9

"""
from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        for h1, h0, m1, m0 in permutations(sorted(A, reverse=True)):
            if h1*10 + h0 < 24 and m1 < 6:
                return f'{h1}{h0}:{m1}{m0}'
        return ''
