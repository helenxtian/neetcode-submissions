class Solution {
public:
    bool isAnagram(string s, string t) {
        // time complexity: O(m+n), space: O(1)
        if (s.size() != t.size()) {
            return false;
        }
        int count[26] = {0};
        for (int i = 0; i < s.size(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        for (int i : count) {
            if (i != 0) {
                return false;
            }
        }
        return true;


        // time complexity: O(m+n), space: O(n)
        /*
        unordered_map<char, int> s_dict;
        unordered_map<char, int> t_dict;

        for (char c : s) {
            s_dict[c]++;
        }
        for (char c : t) {
            t_dict[c]++;
        }

        return s_dict == t_dict;
        */
    }
};
