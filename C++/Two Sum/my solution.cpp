//Given an array of integers, 
//return indices of the two numbers such that they add up to a specific target.
//not use the same element twice.

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
         vector<int>re;
        
        int n = nums.size();
        int flag = 0;

        
        for(int i = 0; i < n;i++)
        {
            for(int j = i+1; j < n; j++ )
            {
                if(target == nums[i] + nums[j] )
                {
                    flag = 1;
                    re.push_back(i);
                    re.push_back(j);
                      break;
                }
            }
            if(flag)
                break;
        }
        return  re;

    }     
    
};
