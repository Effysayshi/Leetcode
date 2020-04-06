//problem: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
//example: Input: [2,2,1]
//         Output: 1

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        
        int n = nums.size();
        for(int i = 0; i < n - 2; i+=2)
            if(nums[i] != nums[i+1])
                return nums[i];

        
        return nums.back();
    }
};
