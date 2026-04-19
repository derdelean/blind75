use std::collection::HashSet;

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
