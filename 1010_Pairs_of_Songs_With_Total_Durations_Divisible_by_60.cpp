class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        int count = time.size();
        int sum = 0;
        int mod60[60] = {0};
        for (int i = 0; i < count; ++i) {
            ++mod60[time[i] % 60];
        }
        sum += mod60[0] * (mod60[0] - 1) / 2;
        sum += mod60[30] * (mod60[30] - 1) / 2;
        for (int i = 1; i < 30; ++i) {
            sum += mod60[i] * mod60[60 - i];
        }
        return sum;
    }
};