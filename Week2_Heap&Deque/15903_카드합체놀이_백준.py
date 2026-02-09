#%%
import sys
input = sys.stdin.readline
import heapq

def main():
    n, m = map(int, input().split()) # 첫째줄 불러오기
    arr = list(map(int, input().split())) # 둘째줄 불러오기
    heapq.heapify(arr)

    for _ in range(m):
        a1, a2 = heapq.heappop(arr), heapq.heappop(arr)
        s = a1 + a2
        heapq.heappush(arr, s)
        heapq.heappush(arr, s)
    
    print(sum(arr))
        

if __name__ == "__main__":
    main()