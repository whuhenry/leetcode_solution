class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> result;
        int headptr = 0;
        int tailptr = 0;
        while(headptr < nums.size()) {
            tailptr = headptr;
            while(tailptr + 1  < nums.size()) {
                long diff = long(nums[tailptr + 1]) - long(nums[tailptr]);
                if (diff != 1) {
                    break;
                }
                ++tailptr;
            }

            stringstream ss;
            ss << nums[headptr];
            if (tailptr != headptr) {
                ss << "->" << nums[tailptr];
            }
            result.push_back(ss.str());
            headptr = tailptr + 1;
        }
        return result;
    }
};