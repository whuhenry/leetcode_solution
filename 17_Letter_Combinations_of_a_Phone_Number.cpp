//使用递归进行全排列，由于递归本身时间复杂度较高，整体效率并不是最优
//讨论区中使用循环依次增加新字母的方式，空间复杂度高一点点（也可能相差不多，毕竟递归的堆栈占用也很高）
//但时间复杂度较低，且代码更加优雅，值得借鉴

class Solution {
public:
    vector<vector<char>> mapNum2Char;
    vector<int> digitNumSeperate;
    vector<string> result;
    
    void addNumber(int index, string curString) {
        for (int i = 0; i < mapNum2Char[digitNumSeperate[index] - 2].size(); ++i) {
            string newString = curString + mapNum2Char[digitNumSeperate[index] - 2][i];
            if (digitNumSeperate.size() == index + 1) {
                result.push_back(newString);
            } else {
                addNumber(index + 1, newString);
            }
        }
    }
    
    
    vector<string> letterCombinations(string digits) {
        if (0 == digits.length()) return result;
        for (int i = 0; i < digits.length(); ++i) {
            digitNumSeperate.push_back(digits[i] - '0');
        }
        mapNum2Char.resize(8);
        
        mapNum2Char[0].push_back('a');
        mapNum2Char[0].push_back('b');
        mapNum2Char[0].push_back('c');
        
        mapNum2Char[1].push_back('d');
        mapNum2Char[1].push_back('e');
        mapNum2Char[1].push_back('f');
        
        mapNum2Char[2].push_back('g');
        mapNum2Char[2].push_back('h');
        mapNum2Char[2].push_back('i');
        
        mapNum2Char[3].push_back('j');
        mapNum2Char[3].push_back('k');
        mapNum2Char[3].push_back('l');
        
        mapNum2Char[4].push_back('m');
        mapNum2Char[4].push_back('n');
        mapNum2Char[4].push_back('o');
        
        mapNum2Char[5].push_back('p');
        mapNum2Char[5].push_back('q');
        mapNum2Char[5].push_back('r');
        mapNum2Char[5].push_back('s');
        
        mapNum2Char[6].push_back('t');
        mapNum2Char[6].push_back('u');
        mapNum2Char[6].push_back('v');
        
        mapNum2Char[7].push_back('w');
        mapNum2Char[7].push_back('x');
        mapNum2Char[7].push_back('y');
        mapNum2Char[7].push_back('z');
        
        addNumber(0, "");
        return result;
    }
};