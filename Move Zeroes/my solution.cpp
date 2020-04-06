//Given an array nums,                                               ---*---Input: [0,1,0,3,12]
//write a function to move all 0's to the end of it                  ---*---Output: [1,3,12,0,0]
//while maintaining the relative order of the non-zero elements.

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
       
       for(int i = 0,j=0; i < nums.size(); i++)
           if(nums[i])
               swap(nums[i],nums[j++]);

    }
};
