#%%
# 힙 기반 우선순위 큐 구현, 배열 기반

class PriorityQueueBase:
    '''우선 순위 큐를 위한 추상 기반 클래스'''
    class _Item:
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __lt__(self, other):
            return self._key < other._key
    
    def is_empty(self):
        return len(self) == 0

class HeapPriorityQueue(PriorityQueueBase):
    '''이진 힙으로 구현된 최소 우선순위 큐'''
    # -------- 비공개 메서드 --------
    def _parent(self, j):
        return (j-1)//2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*(j+1)
    
    def _has_left(self, j):
        '''리스트의 끝을 넘는 인덱스인가?'''
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        '''리스트의 끝을 넘는 인덱스인가?'''
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        '''배열의 인덱스 i, j에 있는 원소를 교환'''
        self._data[i], self._data[j] = self._data[j], self._data[i]
    
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent) # 재귀 호출
    
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child) # 재귀 호출
    
    def _hepify(self):
        start = self._parent(len(self._data) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)


    # -------- 공개 메서드 --------
    def __init__(self, contents=()):
        '''빈 우선순위 큐 생성'''
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 0:
            self._heapify()
    
    def __len__(self):
        '''우선순위 큐에 있는 항목 수 반환'''
        return len(self._data)
    
    def add(self, key, value):
        '''키 key와 값 value를 갖는 항목 추가'''
        item = self._Item(key, value)
        self._data.append(item)
        self._upheap(len(self._data) - 1) # 새 항목의 인덱스, 그 위치에서 업힙 수행

    def min(self):
        ''' 최소 키를 갖는 (k, v) 튜플 반환
        비어있을 경우, Empty 예외를 발생시킨다.
        '''
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        
        item = self.data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        ''' 최소 키를 갖는 (k, v) 튜플을 삭제하고 반환
        비어있을 경우, Empty 예외를 발생시킨다.
        '''
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        
        self._swap(0, len(self._data) - 1) # 루트와 마지막 원소 교환
        item = self._data.pop() # 마지막 원소 삭제
        self._downheap(0) # 새로운 루트에서 다운힙 수행
        return (item._key, item._value)

