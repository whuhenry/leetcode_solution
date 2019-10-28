class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        vector<int> lastTempDay;
        vector<int> ans;
        ans.resize(T.size());
        lastTempDay.resize(71);
        for (int i = 0; i <= 70; ++i) {
            lastTempDay[i] = 0;
        }
        for (int i = T.size() - 1; i >= 0; --i) {
            int minDay = 30000;
            for (int j = T[i] - 30 + 1; j <= 70; ++j) {
                if (lastTempDay[j] != 0 && lastTempDay[j] - i < minDay) {
                    minDay = lastTempDay[j] - i;
                }
            }
            if (minDay == 30000) {
                minDay = 0;
            }
            ans[i] = minDay;
            lastTempDay[T[i] - 30] = i;
        }
        return ans;
    }
};