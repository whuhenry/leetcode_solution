class Solution {
public:
    int myAtoi(string str) {
        int length = str.length();
        
        int scalefactor = 1;
        int start = -1;
        //handle start whitespace
        for (int i = 0; i < length; ++i) {
            if (' ' == str[i]) {
                continue;
            } else {
                start = i;
                break;
            }            
        }
        
        if (-1 == start) {
            return 0;
        }
        
        // handle +/-
        if ('+' == str[start]) {
            ++start;
        } else if ('-' == str[start]) {
            scalefactor = -1;
            ++start;
        }
        
        // handle as many number as possible
        int64_t num = 0;
        for (int i = start; i < length; ++i) {
            if (str[i] >= '0' && str[i] <= '9') {
                num = num * 10 + (str[i] - '0');
                if (num * scalefactor > INT_MAX) {
                    return INT_MAX;
                } else if (num * scalefactor < INT_MIN) {
                    return INT_MIN;
                }
            } else {
                break;
            }
        }
        return int32_t(num * scalefactor);
    }
};