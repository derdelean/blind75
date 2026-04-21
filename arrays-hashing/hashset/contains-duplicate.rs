/*
Task: Given an integer array nums, return true if any value appears more than once in the array,
otherwise return false

HashSet visited_elements Solution:
Time: O(n) - Each operation takes O(1) checking/scanning array once so O(n)
Space: O(n) - HashSet creation -> Size can be up to the size of input so O(n)

Array to HashSet casting Solution:
Time: O(n) -
Space: O(n) -

Check Array againt HashSet with visited elements
*/

use std::collections::HashSet;

struct Solution;

impl Solution {
    fn hash_set1(nums: Vec<i32>) -> bool {
        let mut visited = HashSet::new();

        for n in nums {
            if visited.contains(&n) {
                return true;
            }
            visited.insert(n);
        }
        false //tail expression rule no semicolon -> preferred way
    }

    fn hash_set2(nums: Vec<i32>) -> bool {
        let set: HashSet<i32> = nums.iter().copied().collect();

        if set.len() != nums.len() {
            return true;
        }
        false
    }
}

fn main() {
    let nums = vec![1, 2, 3, 4, 1];
    let result = Solution::hash_set2(nums);
    println!("{}", result);
}
