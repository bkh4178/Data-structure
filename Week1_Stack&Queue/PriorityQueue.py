#%%
class PriorityQueueBase:
    '''우선순위 큐를 위한 추상 기반 클래스'''
    class Item:
        __slots__ = 'key', 'value'
    
        def __init__(self, k, v):
            self.key = k
            self.value = v
        
        def __lt__(self, other):
            return self.key < other.key
        
    def is_empty(self):
        return len(self) == 0

