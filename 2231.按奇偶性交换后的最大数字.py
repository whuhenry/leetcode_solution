#
# @lc app=leetcode.cn id=2231 lang=python3
#
# [2231] 按奇偶性交换后的最大数字
#

# @lc code=start

class Solution:
    def largestInteger(self, num: int) -> int:
        src_num_list = list(map(int, str(num)))
        odd_list = []
        even_list = []
        for n in src_num_list:
            if n % 2 == 0:
                even_list.append(n)
            else:
                odd_list.append(n)
        odd_list.sort(reverse=True)
        even_list.sort(reverse=True)
        odd_ptr = 0
        even_ptr = 0

        result = 0
        for n in src_num_list:
            if n % 2 == 0:
                result = result * 10 + even_list[even_ptr]
                even_ptr += 1
            else:
                result = result * 10 + odd_list[odd_ptr]
                odd_ptr += 1

    
        return result

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    print(s.largestInteger(65875))