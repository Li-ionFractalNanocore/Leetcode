from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        id_to_employee = {employee.id: employee for employee in employees}
        def dfs(now):
            employee = id_to_employee[now]
            return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)
        return dfs(id)
        