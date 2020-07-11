#include <vector>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int length1 = nums1.size();
        int length2 = nums2.size();
        bool singleMedian = ((length1 + length2) % 2 ==1);
        int medianIndex1 = (length1 + length2) / 2;
        int medianIndex2 = medianIndex1 - 1;


        if (0 == length1) {
            if (singleMedian) {
                return nums2[medianIndex1];
            } else {
                return (nums2[medianIndex1] + nums2[medianIndex2]) / 2.0;
            }
        } else if (0 == length2) {
            if (singleMedian) {
                return nums1[medianIndex1];
            } else {
                return (nums1[medianIndex1] + nums1[medianIndex2]) / 2.0;
            }
        }

        if (nums2[0] > nums1[length1 - 1]) {
            
        }

        int cur1Now = length1 / 2, cur1Head = 0, cur1End = length1 - 1;
        int cur2Now = length2 / 2, cur2Head = 0, cur2End = length2 - 1;

        while(true) {
            if (nums1[cur1Now] < nums2[cur2Now]) {
                cur1Head = cur1Now;
                cur2End = cur2Now;
                cur1Now = (cur1Now + cur1End) / 2;
                cur2Now = (cur2Now + cur2Head) / 2;
            }else if 
        }
    }
};