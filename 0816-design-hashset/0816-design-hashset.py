class MyHashSet:

    capacity = 10**4

    def __init__(self):
        self.data = [None] * self.capacity

    def add(self, key: int) -> None:

        h = hash(key)
        index = h % self.capacity

        if self.data[index] is not None:
            if key not in self.data[index]:
                self.data[index].append(key)
        else:
            self.data[index] = [key]
       

    def remove(self, key: int) -> None:
        h = hash(key)
        index = h % self.capacity

        if self.data[index] is not None:
            if key in self.data[index]:
                self.data[index].remove(key)

    def contains(self, key: int) -> bool:
        h = hash(key)
        index = h % self.capacity

        if self.data[index] is not None and  key in self.data[index]:
                return True 
        else: 
            return False


        
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)