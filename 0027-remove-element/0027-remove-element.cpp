// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
 public:
  int removeElement(vector<int>& nums, int val) {
    int k{0};
    int y{static_cast<int>(nums.size()) - 1};

    while (k <= y) {
      if (nums[k] == val) {
        nums[k] = nums[y--];
      } else {
        ++k;
      }
    }
    return k;
  }  // 1, 2 , 4  2, 2
};
// @leet end
