class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        arr2Count = [0 for i in range(len(arr2))]
        for a1 in arr1:
            flag = False
            for i in range(len(arr2)):
                if a1 == arr2[i]:
                    flag = True
                    arr2Count[i] += 1
                    break
            if not flag:
                arr3.append(a1)

        arr4 = []
        for i in range(len(arr2)):
            for j in range(arr2Count[i]):
                arr4.append(arr2[i])
        arr3.sort()
        arr4.extend(arr3)
        
        return arr4
