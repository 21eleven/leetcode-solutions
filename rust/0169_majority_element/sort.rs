/*
169. Majority Element
Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2*/
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut s = nums;
        s.sort();
        s[s.len() / 2]
    }
}
