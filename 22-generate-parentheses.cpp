#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    void generate(int leftCount, int rightCount) {
        if (maxCount == leftCount && maxCount == rightCount) {
            result.push_back(generatedSequence);
        } else {
            if (leftCount < maxCount) {
                generatedSequence.push_back('(');
                generate(leftCount + 1, rightCount);
                generatedSequence.pop_back();
            }
            if (rightCount < leftCount) {
                generatedSequence.push_back(')');
                generate(leftCount, rightCount + 1);
                generatedSequence.pop_back();
            }
        }
    }

    vector<string> generateParenthesis(int n) {
        if (0 >= n){
            return result;
        }
        maxCount = n;
        generatedSequence = "";

        generate(0, 0);

        return result;
    }

    vector<string> result;
    int maxCount;
    string generatedSequence;
};