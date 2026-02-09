import sys
import heapq
input = sys.stdin.readline

def main():
    N = int(input())

    low_heap = []
    high_heap = []
    
    for i in range(N):
        x = int(input())
        if i == 0 or x <= -low_heap[0]: 
            heapq.heappush(low_heap, -x)
        elif x > -low_heap[0] :
            heapq.heappush(high_heap, x)

        if len(low_heap) > len(high_heap) +1:
            heapq.heappush(high_heap, -heapq.heappop(low_heap))
        elif len(low_heap) < len(high_heap):
            heapq.heappush(low_heap, -heapq.heappop(high_heap))
    
        mid = -low_heap[0]

        print(mid)

if __name__ == '__main__':
    main()