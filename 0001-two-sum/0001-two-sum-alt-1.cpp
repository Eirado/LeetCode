// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen{};
    for (int i = 0; i < nums.size(); ++i) {
      int aim{target - nums[i]};
      if (seen.count(aim)) {
        return {i, seen[aim]};
      }
      seen.insert({nums[i], i});
    }
    return {};
  }
};
// @leet end
