#%%
# 정답 코드
import sys
from collections import deque
import queue

input = sys.stdin.readline

def main():
    N = int(input())
    for _ in range(N):
        n, m = map(int, input().split())
        doc_list = list(map(int, input().split()))
        
        Q = deque() # 덱 생성

        for i in range(n):
            Q.append((doc_list[i], i)) # 기존 인덱스와 함께 튜플로 삽입
        
        Order = 0 # 순서알기 위한 변수 지정

        while len(Q)>0:
            cur_max = max(x[0] for x in Q)
            a = Q.popleft()
            if a[0] < cur_max: Q.append(a)
            else:
                Order += 1 # 출력 순서는 Order +1
                if m == a[1]:
                    print(Order)
                    break

if __name__ == '__main__':
    main()