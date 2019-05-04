class Solution {
public:
    string intToRoman(int num) {
        vector<int> seperateNum;
        while (num != 0) {
            seperateNum.push_back(num % 10);
            num /= 10;
        }
        
        int length = seperateNum.size();       
        stringstream ss;
        for (int i = length - 1; i >= 0; --i) {
            switch (i) {
                case 3:
                {
                    for (int j = 0; j < seperateNum[i]; ++j) {
                        ss << 'M';
                    }
                }
                    break;
                case 2:
                {
                    if (4 == seperateNum[i]) {
                        ss << "CD";
                    } else if (9 == seperateNum[i]) {
                        ss << "CM";
                    } else if (seperateNum[i] < 5) {
                        for (int j = 0; j < seperateNum[i]; ++j) {
                            ss << 'C';
                        }
                    } else if (seperateNum[i] >= 5) {
                        ss << 'D';
                        for (int j = 0; j < seperateNum[i] - 5; ++j) {
                            ss << 'C';
                        }
                    }
                }
                    break;
                case 1:
                {
                    if (4 == seperateNum[i]) {
                        ss << "XL";
                    } else if (9 == seperateNum[i]) {
                        ss << "XC";
                    } else if (seperateNum[i] < 5) {
                        for (int j = 0; j < seperateNum[i]; ++j) {
                            ss << 'X';
                        }
                    } else if (seperateNum[i] >= 5) {
                        ss << 'L';
                        for (int j = 0; j < seperateNum[i] - 5; ++j) {
                            ss << 'X';
                        }
                    }
                }
                    break;
                case 0:
                {
                    if (4 == seperateNum[i]) {
                        ss << "IV";
                    } else if (9 == seperateNum[i]) {
                        ss << "IX";
                    } else if (seperateNum[i] < 5) {
                        for (int j = 0; j < seperateNum[i]; ++j) {
                            ss << 'I';
                        }
                    } else if (seperateNum[i] >= 5) {
                        ss << 'V';
                        for (int j = 0; j < seperateNum[i] - 5; ++j) {
                            ss << 'I';
                        }
                    }
                }
                    break;
            }
        }
        
        return ss.str();
    }
};