class Solution {
public:
    int climbStairs(int n) {
        if (0 == n) {
            return 0;
        } else if (1 == n) {
            return 1;
        }

        int *a = new int[n];

        for (int i = 0; i < n; ++i) {
            a[i] = 0;
        }
        a[0] = 1;
        a[1] = 2;
        for (int i = 2; i < n; ++i) {
            a[i] = a[i - 1] + a[i - 2];
        }
        
        int result = a[n - 1];

        delete[] a;

        return result;
    }
};