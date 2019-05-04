class Solution {
public:    
    int reverse(int x) {
        int64_t newNum = 0;
        do {
            newNum = newNum * 10 + x % 10;
            x /= 10;
        } while (x != 0);
        
        if ((int64_t)(int32_t)newNum != newNum) {
            return 0;
        } else {
            return (int32_t)newNum;
        }
    }
};