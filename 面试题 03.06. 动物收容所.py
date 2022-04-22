import collections
from typing import List

class AnimalShelf:

    def __init__(self):
        self.dog = collections.deque()
        self.cat = collections.deque()
        self.other = collections.deque()
        self.idx = 0


    def enqueue(self, animal: List[int]) -> None:
        animal.append(self.idx)
        if animal[1] == 0:
            self.cat.append(animal)
        elif animal[1] == 1:
            self.dog.append(animal)
        else:
            self.other.append(animal)
        self.idx += 1


    def dequeueAny(self) -> List[int]:
        tmp = []
        if self.cat:
            tmp.append(self.cat[0])
        if self.dog:
            tmp.append(self.dog[0])
        if self.other:
            tmp.append(self.other[0])
        if not tmp:
            return [-1, -1]
        tmp.sort(key=lambda x: (x[2]), reverse=True)
        if tmp[0][1] == 0:
            return self.cat.popleft()[:2]
        elif tmp[0][1] == 1:
            return self.dog.popleft()[:2]
        else:
            return self.other.popleft()[:2]        


    def dequeueDog(self) -> List[int]:
        if self.dog:
            return self.dog.popleft()[:2]
        else:
            return [-1, -1]


    def dequeueCat(self) -> List[int]:
        if self.cat:
            return self.cat.popleft()[:2]
        else:
            return [-1, -1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()