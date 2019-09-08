#include <vector>
using namespace std;

class Solution {
public:
    int distanceBetweenBusStops(vector<int>& distance, int start, int destination) {
        int sum = 0;
        int sumStart2Des = 0;
        if (start > destination) {
            std::swap(start, destination);
        }
        for (int i = 0; i < distance.size(); ++i) {
            sum += distance[i];
            if (i >= start && i < destination) {
                sumStart2Des += distance[i];
            }
        }

        if (sum - sumStart2Des < sumStart2Des) {
            sumStart2Des = sum - sumStart2Des;
        }

        return sumStart2Des;
    }
};