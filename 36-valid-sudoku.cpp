class Solution {
public:
    bool flags[9];
    void resetFlags(){
        for (int i = 0; i < 9; ++i) {
            flags[i] = false;
        }
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        //per rows
        for (int i = 0; i < 9; ++i) {
            resetFlags();
            for (int j = 0; j < 9; ++j) {
                if ('.' == board[i][j]) {
                    continue;
                } else {
                    int num = board[i][j] - '1';
                    if (flags[num]) {
                        return false;
                    } else {
                        flags[num] = true;
                    }
                }
            }            
        }

        //per col
        for (int j = 0; j < 9; ++j){
            resetFlags();
            for (int i = 0; i < 9; ++i) {
                if ('.' == board[i][j]) {
                    continue;
                } else {
                    int num = board[i][j] - '1';
                    if (flags[num]) {
                        return false;
                    } else {
                        flags[num] = true;
                    }
                }
            }
            
        }

        //per block
        for (int k = 0; k < 9; ++k) {
            int sr = k / 3 * 3;
            int sc = k % 3 * 3;
            resetFlags();
            for (int i = sr; i < sr + 3; ++i) {
                for (int j = sc; j < sc + 3; ++j) {
                    if ('.' == board[i][j]) {
                        continue;
                    } else {
                        int num = board[i][j] - '1';
                        if (flags[num]) {
                            return false;
                        } else {
                            flags[num] = true;
                        }
                    }
                }
            }
        }

        return true;
    }
};