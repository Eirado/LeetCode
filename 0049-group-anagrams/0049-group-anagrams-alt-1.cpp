// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
 public:
  vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> resultMap{};

    for (int i = 0; i < strs.size(); ++i) {
      string sortedS{strs[i]};
      sort(sortedS.begin(), sortedS.end());

      if (resultMap.count(sortedS) > 0) {
        resultMap[sortedS].push_back(strs[i]);
      }
      resultMap.insert({sortedS, {strs[i]}}); // This solution is wrong because there is a bug here
    }
    vector<vector<string>> result{};
    for (std::pair<const std::string, std::vector<std::string>> pair : resultMap) {
      result.push_back(pair.second);
    }
    return result;
  }
};
// @leet end
