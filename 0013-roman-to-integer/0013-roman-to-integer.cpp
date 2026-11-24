// @leet imports start
#include <bits/stdc++.h>
using namespace std;
// @leet imports end

// @leet start
class Solution {
public:
int romanToInt(string s) {
       int finalNumber {0};
       char previous {};
       unordered_map<char, int> roman {
        {'I', 1},
        {'V', 5},
        {'X', 10},
        {'L', 50}, 
        {'C', 100},
        {'D', 500},
        {'M', 1000}
        };
       for (auto letter: s) {
        if (roman[previous] < roman[letter] ) {

            finalNumber -= roman[previous] * 2;
        }

        finalNumber += roman[letter];
        previous = letter;
       } 
       return finalNumber;
    }
};
// @leet end
