class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        vector<int> ans;
        ans.resize(10000 * 2 + 1);
        for (int i = -10000; i <= 10000; i++) {
            ans[i + 10000] = 0;
        }

        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] - difference >= -10000 and arr[i] - difference <= 10000) {
                ans[arr[i] + 10000] = ans[arr[i] - difference + 10000] + 1;
            } else {
                ans[arr[i] + 10000] = 1;
            }
        }

        int maxlen = 0;
        for (int i = -10000; i <= 10000; ++i) {
            if (ans[i + 10000] > maxlen) {
                maxlen = ans[i + 10000];
            }
        }
        return maxlen;
    }
};