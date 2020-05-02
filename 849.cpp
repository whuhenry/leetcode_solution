class Solution {
public:
    int maxDistToClosest(vector<int>& seats) {
        int left = -1, right = -1;
        vector<int> minDist(seats.size(), 20000);
        for (int i = 0; i < seats.size(); ++i) {
            if (seats[i] == 1) {
                left = i;
            } else if (left >= 0) {
                minDist[i] = i - left;
            }
        }

        for (int i = seats.size() - 1; i >= 0; --i) {
            if (seats[i] == 1) {
                right = i;
            } else if (right >= 0) {
                minDist[i] = min(right - i, minDist[i]);
            }
        }

        int result = 0;
        for (int i = 0; i < minDist.size(); ++i) {
            if (seats[i] == 0 && minDist[i] > result) {
                result = minDist[i];
            }
        }

        return result;
    }
};