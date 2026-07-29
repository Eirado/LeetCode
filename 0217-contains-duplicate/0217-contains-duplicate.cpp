// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
#include <set>

class Solution {
 public:
  bool containsDuplicate(vector<int>& nums) {
    set<int> uniqueNumbers{};

    for (int i : nums) {
      if (uniqueNumbers.contains(i)) {
        return true;
      } else {
        uniqueNumbers.insert(i);
      }
    }
    return false;
  }
};
// @leet end
