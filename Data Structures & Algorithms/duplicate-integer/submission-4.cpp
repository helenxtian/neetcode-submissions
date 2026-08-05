class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        /*
        create hash table to record the numbers that show up
        key = number, value = times it shows up
        if value > 1 at any point, return true
        */

        unordered_set<int> seen;
        for (int i : nums) {
            if (seen.count(i)) {
                return true;
            }
            seen.insert(i);
        }
        return false;
    }
};