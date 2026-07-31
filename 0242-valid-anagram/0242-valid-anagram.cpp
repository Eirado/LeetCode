// @leet imports start
#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;
// @leet imports end

// @leet start
class Solution {
 public:
  bool isAnagram(string s, string t) {
    if (s.length() != t.length()) {
      return false;
    }
    unordered_map<char, int> dictT{};
    unordered_map<char, int> dictS{};

    for (int i = 0; i < t.length(); ++i) {
      dictS[s[i]]++;
      dictT[t[i]]++;
    }
    return dictS == dictT;
  }
};
// @leet end
