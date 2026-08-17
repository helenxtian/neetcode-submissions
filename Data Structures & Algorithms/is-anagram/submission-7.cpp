class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        
        int chars[26] = {0};
        for (int i = 0 ; i < s.size(); i++) {
            chars[s[i]-'a']++;
            chars[t[i]-'a']--;
        }

        for (int i : chars) {
            if (i != 0) {
                return false;
            }
        }
        return true;
    }
};
