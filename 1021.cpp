class Solution {
public:
    string removeOuterParentheses(string S) {
        stack<char> ss;
        string ans = "";
        for (int i = 0; i < S.size(); ++i) {
            if (ss.empty()) {
                ss.push(S[i]);
            } else if (ss.top() == '(' && S[i] == ')') {
                ss.pop();
                if (!ss.empty()) {
                    ans += ')';
                }
            } else {
                ss.push(S[i]);
                ans += S[i];
            }
        }
        return ans;
    }
};