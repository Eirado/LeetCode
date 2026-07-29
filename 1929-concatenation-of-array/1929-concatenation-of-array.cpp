// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
 public:
  vector<int> getConcatenation(vector<int>& nums) {
    vector<int> ans{nums};
    ans.insert(ans.end(), nums.begin(), nums.end());
    return ans;
  }
};
/ @leet end
