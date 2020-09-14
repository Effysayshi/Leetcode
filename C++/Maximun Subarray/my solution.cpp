//Given an integer array nums,                                     ----*---- Input: [-2,1,-3,4,-1,2,1,-5,4],
//find the contiguous subarray (containing at least one number) 
//which has the largest sum and return its sum.                    ----*---- Output: 6

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max = nums[0];
        int sum;
        
        for(int i = 0; i < nums.size(); i++)
        {
            sum = nums[i];
            max = max>sum ? max : sum;
            for(int j = i+1 ; j < nums.size(); j++)
            {
                sum+= nums[j];
                max = max>sum ? max : sum; 
            }
        }
        return max;
    }
};
