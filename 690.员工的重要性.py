#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性
#

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from typing import List

class Solution:
    def bfs(self, employee):
        if employee is None:
            return 0
        sub_sum = 0
        for sub in employee.subordinates:
            sub_sum += self.bfs(self.employees_dict[sub])
        return employee.importance + sub_sum


    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.employees_dict = {}
        for employee in employees:
            self.employees_dict[employee.id] = employee
        return self.bfs(self.employees_dict[id])
        
# @lc code=end

