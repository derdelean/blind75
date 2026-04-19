/*
Task: Given an integer array nums, return true if any value appears more than once in the array,
otherwise return false

Time: O(n) - Each operation takes O(1) checking/scanning array once so O(n)
Space: O(n) - HashSet creation -> Size can be up to the size of input so O(n)

Check Array againt HashSet with visited elements
*/

use std::collections::HashSet;

struct Solution;

impl Solution {
    fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut visited = HashSet::new();

        for n in nums {
            if visited.contains(&n) {
                return true;
            }
            visited.insert(n);
        }
        false
    }
}
