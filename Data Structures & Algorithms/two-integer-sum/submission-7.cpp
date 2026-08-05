class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // if seen, then output the index and the previous index
        // so has to be key (number) value (idx) -> (unordered map)

        unordered_map<int, int> previous_nums_idxs;
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (previous_nums_idxs.count(diff)) {
                return {previous_nums_idxs[diff], i};
            }
            previous_nums_idxs[nums[i]] = i;
        }
        return {};
    }
};
