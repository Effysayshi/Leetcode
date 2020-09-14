//Given an integer array arr,                            ---*---Input: arr = [1,2,3]
//count element x such that x + 1 is also in arr.        ---*---Output: 2
//If there're duplicates in arr, count them seperately.  !count the duplicates

class Solution {
public:
    int countElements(vector<int>& arr) {
        unordered_set<int> myset;
        myset.insert(arr.begin(),arr.end());
        
        int cnt =0;
        
        for(auto n:arr)
            if(myset.count(n+1))
                cnt++;
        
        return cnt;
    }
};
