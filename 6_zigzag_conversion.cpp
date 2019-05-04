class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        string news = s;
        int length = s.length();
        int zigSize = numRows + numRows - 2;
        int zigCount = length / zigSize;
        if (length % zigSize != 0) {
            ++zigCount;
        }
        
        int index = 0;
        for (int i = 0; i < numRows; ++i) {
            for (int j = 0; j <zigCount; ++j) {
                if (0 == i) {
                    news[index] = s[j * zigSize];
                    ++index;
                } else {
                    int srcIndex = j * zigSize + i;
                    if (srcIndex >= length) {
                        continue;
                    } else {
                        news[index] = s[srcIndex];
                        ++index;
                    }
                    
                    if (numRows - 1 != i) {
                        int srcIndex = j * zigSize + numRows - 1 + numRows - i - 1;
                        if (srcIndex >= length) {
                            continue;
                        } else {
                            news[index] = s[srcIndex];
                            ++index;
                        }
                    }
                }
            }
        }
        return news;
    }
};