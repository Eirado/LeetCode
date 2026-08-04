// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
    int majorityElement(vector<int>& nums) {
    sort(nums.begin(), nums.end());
     return nums[nums.size() / 2];  
    }
};
// @leet end
