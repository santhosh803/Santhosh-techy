class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        index_value = 0
        for i in key:
            index_value += ord(i)

        return index_value % 10
    
    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if element[0]==key and len(element)==2:
                self.arr[h][index] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))
                

    def __getitem__(self, key):
        h = self.get_hash(key)
        found = False
        for element in self.arr[h]:
            if element[0]==key:
                found = True
                return element[1]
            
        if not found:
            print('Given key is invalid')
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            if element[0]==key:
                found = True
                del self.arr[h][index]
                break

        if not found:
            print('Given key is not present')


t = HashTable()
t['March 1'] = 123
t['March 2'] = 13
t['March 3'] = 44
t['March 4'] = 37
t['March 1'] = 45
t['March 17'] = 1 
print(t['March 3'])
print(t.arr)
t['March 6'] = 5
print(t.arr)
del t['March 17']
print(t.arr)