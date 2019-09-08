class Solution {
public:
    bool isValid(string s) {
        int length = s.length();
        if (length % 2 != 0) {
            return false;
        }
        
        stack<char> charStack;
        for (int i = 0; i < length; ++i) {
            if (charStack.empty()) {
                charStack.push(s[i]);
            } else {
                if (match(charStack.top(), s[i])) {
                    charStack.pop();
                } else {
                    charStack.push(s[i]);
                }
            }
        }
        
        return charStack.empty();
    }
    
    bool match(char &c1, char &c2) {
        if ((c1 == '(' && c2 == ')')
            || (c1 == '{' && c2 == '}')
            || (c1 == '[' && c2 == ']'))
                {
                    return true;
                }
                else {
                    return false;
                }
    }
};