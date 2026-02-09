#%%
# deque 안 쓰고 한 ver -> 불안정한 코드

import sys
input = sys.stdin.readline

n = int(input())
cards = list(range(1,n+1))
front = 0
rear = n-1

while front != rear:
    front = (front+1)%n
    a = cards[front]
    rear = (rear+1)%n
    cards[rear]=a
    front = (front+1)%n

print(cards[front])

#%%
# 봤을 때 가장 빠르고 정확한 코드

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque(range(1, n+1))

while len(q) > 1:
    q.popleft()          # 맨 위 카드 버림
    q.append(q.popleft())  # 그 다음 카드 맨 뒤로

print(q[0])
