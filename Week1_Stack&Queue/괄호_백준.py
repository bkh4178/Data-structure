#%%
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    # 문제 로직
    for _ in range(n):
        string = input().strip()
        S = []
        valid = True

        for j in range(len(string)):
            if string[j] == '(':
                S.append(string[j])
            else:
                if len(S) == 0 : 
                    valid = False
                    break
                else : 
                    S.pop()

        if valid and len(S)==0 :
            print('YES')
        else : 
            print('NO')
            

if __name__ == "__main__":
    main()

