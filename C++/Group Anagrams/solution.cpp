//Given an array of strings,    ---*---Input: ["eat", "tea", "tan", "ate", "nat", "bat"], 
//group anagrams together.      ---*---Output:[ ["ate","eat","tea"], ["nat","tan"],["bat"]]
//input vector<string>  and output vector<vector<string>>


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>keep;
        vector<vector<string>> result;
        
        for(auto str:strs)
        {
            string key = str;
            sort(key.begin(),key.end());
            
            keep[key].push_back(str);
        }
        
        for(auto n : keep)
            result.push_back(n.second);
        
        return result;
    }
};
