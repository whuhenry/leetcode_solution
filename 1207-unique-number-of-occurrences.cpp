class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int> occurrence;
        for (int i = 0; i < arr.size(); ++i) {
            if (0 == occurrence.count(arr[i])) {
                occurrence[arr[i]] = 1;
            } else {
                occurrence[arr[i]] += 1;
            }
        }

        set<int> count;
        for (auto &occurrencePair : occurrence) {
            if (count.find(occurrencePair.second) == count.end()) {
                count.insert(occurrencePair.second);
            } else {
                return false;
            }
        }

        return true;
    }
};