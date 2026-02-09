#%%
'''
Stack의 Docstring
'''
class Empty(Exception):
    pass

class ArrayStack:
    '''pyhthon list를 기본 저장소로 사용하는 LIFO 스택 구현'''
    def __init__(self) :
        '''빈 스택 생성'''
        self.data = []

    def __len__(self) :
        return len(self.data)
    
    def is_empty(self):
        return len(self.data) == 0
    
    def push(self, e) :
        self.data.append(e)

    def top(self) :
        if self.is_empty() != 0 :
            raise Empty('Stack is empty')
        return self.data[-1]

    def pop(self) :
        if self.is_empty() :
            raise Empty('Stack is empty')
        return self.data.pop()


#%%
'''
예시 1. Stack을 이용한 데이터 반전
'''
def reverse_file(filename):
    S = ArrayStack()
    original = open(filename)
    for line in original :
        S.push(line.rstrip('\n'))
    original.close()

    output = open(filename, 'w')
    while not S.is_empty():
        output.write(S.pop() + '\n')
    output.close()


#%%
def is_matched(expr):
    ''' 모든 괄호가 매칭되면 True, 그렇지 않으면 False 반환 '''
    lefty = '({['
    righty = ']})'
    S= ArrayStack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty(): return False
            if righty.index(c) != lefty.index(S.pop()): 
                return False
    return S.is_empty()

def is_matched_html(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1: return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty(): return False
            if tag[1:] != S.pop() : return False
        j = raw.find('<',k+1)
    return S.is_empty()

