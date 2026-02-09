#%%
MAX_QSIZE = 10 # 원형 큐의 크기
class CircularQueue:
    def __init__(self):
        self.front = 0 # 큐의 맨 앞쪽 위치
        self.rear = 0 # 큐의 맨 뒤쪽 위치
        self.items = [None]*MAX_QSIZE # 항목 저장용 리스트
    def isEmpty(self) : return self.front == self.rear
    def isFull(self) : return self.front == (self.rear +1)%MAX_QSIZE
    def clear(self) : self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
        
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1)% MAX_QSIZE
            return self.items[self.front]
    
    def peek(item):
        if not self.isEmpty():
            return self.items[(self.front +1)%MAX_QSIZE]
    
    def size(self):
        return (self.rear - self.front + MAX_QSIZE)%MAX_QSIZE
    
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1 : self.rear +1]
        else:
            out = self.items[self.front+1 : MAX_QSIZE] + self.items[0:self.rear+1]
        print('[front = %s, rear = %s=d] ==> '%(self.front, self.rear), out)
