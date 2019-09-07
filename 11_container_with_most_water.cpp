// O(n) Soluction
// 利用了一个事实，对于一个已经计算得到的Volumn来说，将长边向短边移动时，所得到的Volumn不可能比现在还大

class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0;
        int end = height.size() - 1;
        int maxWater = 0;
        while (start < end) {
            int contain = (end - start) * min(height[start], height[end]);
            maxWater = max(contain, maxWater);
            if (height[start] < height[end]) {
                ++start;
            } else {
                --end;
            }
        }
        return maxWater;
    }
};