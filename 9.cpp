class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        vector<int> digit;
        do {
            digit.push_back(x % 10);
            x = x / 10;
        } while (x != 0);
        
        int count = digit.size();
        bool flag = true;
        for (int i = 0; i < count / 2; ++i) {
            if (digit[i] != digit[count - i - 1]) {
                flag = false;
                break;
            }
        }
        return flag;
    }
};