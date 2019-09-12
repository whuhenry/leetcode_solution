class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (0 >= n) {
            return false;
        }
        while (n > 1) {
            if (0 != n % 2) {
                return false;
            }
            n /= 2;
        }

        return true;
    }
};