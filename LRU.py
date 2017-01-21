#unoptomized LRU cache implementation
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.used = []
        
    def removeLRU(self):
        ret = -1
        while ret == -1:
            item = self.used.pop(0)
            ret = self.cache.pop(item,-1)
        
    def updateUsed(self,key):
        if key in self.used:
            self.used.remove(key)
        self.used.append(key)
        
    def get(self, key):
        self.updateUsed(key)
        return self.cache.get(key,-1)
        
    def set(self, key, value):
        if(len(self.cache) == self.capacity and key not in self.cache):
            #has to add new value to cache
            self.removeLRU()
    
        self.updateUsed(key)
        self.cache[key] = value
        